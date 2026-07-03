import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import IsolationForest

print("=== Lab 01: Anomaly Detection for Network Security ===")

# Simulate normal network traffic
np.random.seed(42)

normal_traffic = np.random.normal(
    loc=100,
    scale=20,
    size=(1000, 2)
)

# Simulate anomalous network traffic
anomaly_traffic = np.random.normal(
    loc=300,
    scale=50,
    size=(50, 2)
)

# Combine data
network_data = np.vstack([
    normal_traffic,
    anomaly_traffic
])

df = pd.DataFrame(
    network_data,
    columns=["Packet_Size", "Duration"]
)

print("\nSample Network Traffic Data:")
print(df.head())

# Train Isolation Forest model
model = IsolationForest(
    contamination=0.05,
    random_state=42
)

model.fit(df)

# Predict anomalies
predictions = model.predict(df)

df["Anomaly"] = predictions

# Convert labels for readability
df["Status"] = df["Anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

print("\nDetection Summary:")
print(df["Status"].value_counts())

# Save results
df.to_csv("network_anomaly_results.csv", index=False)

# Visualize anomalies
plt.figure(figsize=(10, 6))
plt.scatter(
    df["Packet_Size"],
    df["Duration"],
    c=df["Anomaly"],
    cmap="coolwarm",
    marker="o"
)

plt.xlabel("Packet Size")
plt.ylabel("Duration")
plt.title("Anomaly Detection in Network Traffic using Isolation Forest")
plt.tight_layout()
plt.savefig("network_anomaly_plot.png")
plt.close()

# Save report
with open("anomaly_detection_report.txt", "w") as file:
    file.write("Lab 01: Anomaly Detection for Network Security\n\n")
    file.write("Model Used: Isolation Forest\n")
    file.write("Dataset: Simulated network traffic data\n")
    file.write("Features: Packet_Size, Duration\n")
    file.write("Contamination Rate: 0.05\n\n")
    file.write("Detection Summary:\n")
    file.write(str(df["Status"].value_counts()))
    file.write("\n\nConclusion:\n")
    file.write("Isolation Forest successfully detected anomalous network traffic patterns.\n")

print("\nFiles saved:")
print("network_anomaly_results.csv")
print("network_anomaly_plot.png")
print("anomaly_detection_report.txt")

print("\nLab completed successfully.")
