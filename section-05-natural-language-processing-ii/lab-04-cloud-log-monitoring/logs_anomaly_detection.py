import pandas as pd
import spacy
import matplotlib.pyplot as plt

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Simulated cloud logs
logs = [
    "Error: Pod 'web-server' crashed due to memory exhaustion",
    "Warning: CPU usage for 'database' exceeds 85% threshold",
    "Info: Pod 'load-balancer' started successfully",
    "Error: Pod 'api-server' failed to start due to missing configuration",
    "Info: 'worker' pod is running at 90% efficiency",
    "Warning: 'database' pod memory usage increased by 20%",
    "Error: 'auth-service' failed with a 500 error",
    "Info: 'auth-service' restarted successfully after failure"
]

df = pd.DataFrame(logs, columns=["log_message"])

# NLP preprocessing
def process_log(text):
    doc = nlp(text)
    return [token.text for token in doc if not token.is_stop]

df["processed_log"] = df["log_message"].apply(process_log)

# Simple anomaly detection
df["error_count"] = df["log_message"].str.lower().str.count("error")
df["warning_count"] = df["log_message"].str.lower().str.count("warning")

df["anomaly"] = (df["error_count"] + df["warning_count"]) >= 1

print(df)

# Visualization
plt.figure()
df["anomaly"].value_counts().plot(kind="bar")
plt.title("Cloud Log Anomaly Detection")
plt.xlabel("Anomaly")
plt.ylabel("Count")

plt.savefig("anomaly_chart.png")
plt.show()
