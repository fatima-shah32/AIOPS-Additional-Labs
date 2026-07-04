import random
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from prometheus_client import Gauge, start_http_server

print("=== Lab 05: Real-time Anomaly Detection in Cloud Infrastructure ===")

def generate_logs(num_logs=1000):
    logs = []
    start_time = datetime(2023, 1, 1)

    for i in range(num_logs):
        timestamp = start_time + timedelta(minutes=i)

        cpu_usage = random.uniform(10, 80)
        memory_usage = random.uniform(20, 70)
        response_time = random.uniform(100, 200)

        if i % 100 == 0:
            cpu_usage = random.uniform(85, 100)
            memory_usage = random.uniform(75, 95)
            response_time = random.uniform(250, 500)

        logs.append([timestamp, cpu_usage, memory_usage, response_time])

    return pd.DataFrame(
        logs,
        columns=["timestamp", "cpu_usage", "memory_usage", "response_time"]
    )

df_logs = generate_logs()
df_logs.to_csv("results/cloud_infrastructure_logs.csv", index=False)

features = df_logs[["cpu_usage", "memory_usage", "response_time"]]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(scaled_features)

df_logs["anomaly"] = model.predict(scaled_features)
df_logs["anomaly_label"] = df_logs["anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

df_logs.to_csv("results/anomaly_detection_results.csv", index=False)

anomalies = df_logs[df_logs["anomaly"] == -1]

print("\nTotal Logs:", len(df_logs))
print("Detected Anomalies:", len(anomalies))
print("\nSample anomalies:")
print(anomalies.head())

plt.figure(figsize=(10, 5))
plt.plot(df_logs["timestamp"], df_logs["cpu_usage"], label="CPU Usage")
plt.scatter(
    anomalies["timestamp"],
    anomalies["cpu_usage"],
    label="Anomaly",
    marker="x"
)
plt.title("CPU Usage Anomaly Detection")
plt.xlabel("Timestamp")
plt.ylabel("CPU Usage")
plt.legend()
plt.tight_layout()
plt.savefig("results/cpu_anomalies.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(df_logs["timestamp"], df_logs["memory_usage"], label="Memory Usage")
plt.scatter(
    anomalies["timestamp"],
    anomalies["memory_usage"],
    label="Anomaly",
    marker="x"
)
plt.title("Memory Usage Anomaly Detection")
plt.xlabel("Timestamp")
plt.ylabel("Memory Usage")
plt.legend()
plt.tight_layout()
plt.savefig("results/memory_anomalies.png")
plt.close()

# Prometheus metrics simulation
cpu_gauge = Gauge("cloud_cpu_usage", "Simulated cloud CPU usage")
memory_gauge = Gauge("cloud_memory_usage", "Simulated cloud memory usage")
response_gauge = Gauge("cloud_response_time", "Simulated response time")
anomaly_gauge = Gauge("cloud_anomaly_detected", "1 if anomaly detected, 0 if normal")

with open("reports/final_report.txt", "w") as report:
    report.write("Lab 05: Real-time Anomaly Detection in Cloud Infrastructure\n\n")
    report.write("Objective:\n")
    report.write("Monitor cloud infrastructure and detect anomalies using machine learning.\n\n")
    report.write("Model Used:\n")
    report.write("Isolation Forest\n\n")
    report.write(f"Total Logs: {len(df_logs)}\n")
    report.write(f"Detected Anomalies: {len(anomalies)}\n\n")
    report.write("Generated Files:\n")
    report.write("- cloud_infrastructure_logs.csv\n")
    report.write("- anomaly_detection_results.csv\n")
    report.write("- cpu_anomalies.png\n")
    report.write("- memory_anomalies.png\n\n")
    report.write("Conclusion:\n")
    report.write("The ML model successfully detected abnormal infrastructure behavior.\n")

print("\nStarting Prometheus metrics server on port 8000.")
print("Open http://localhost:8000/metrics")
print("Press CTRL+C to stop.")

start_http_server(8000)

for _, row in df_logs.tail(20).iterrows():
    cpu_gauge.set(row["cpu_usage"])
    memory_gauge.set(row["memory_usage"])
    response_gauge.set(row["response_time"])
    anomaly_gauge.set(1 if row["anomaly"] == -1 else 0)

    print(
        f"CPU={row['cpu_usage']:.2f}, "
        f"Memory={row['memory_usage']:.2f}, "
        f"Response={row['response_time']:.2f}, "
        f"Status={row['anomaly_label']}"
    )

    time.sleep(2)
