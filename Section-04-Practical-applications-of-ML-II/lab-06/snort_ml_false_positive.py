import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

print("=== Lab 06: Intrusion Detection with Snort and Machine Learning ===")

data = {
    "alert_type": [
        "DoS",
        "Port Scan",
        "DoS",
        "SQL Injection",
        "Port Scan",
        "Malware",
        "Brute Force",
        "Port Scan",
        "DoS",
        "SQL Injection"
    ],
    "alert_details": [
        "SYN flood detected",
        "Multiple port scans",
        "ICMP flood",
        "SQL injection attempt",
        "Scan from suspicious IP",
        "Malware signature detected",
        "Repeated failed login attempts",
        "Internal scan by admin tool",
        "Large packet burst",
        "Test SQL pattern from scanner"
    ],
    "label": [1, 0, 1, 1, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
df.to_csv("snort_alert_dataset.csv", index=False)

label_encoder = LabelEncoder()
df["alert_type_encoded"] = label_encoder.fit_transform(df["alert_type"])

X = df[["alert_type_encoded"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy, 2))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

joblib.dump(model, "snort_false_positive_model.pkl")
joblib.dump(label_encoder, "alert_label_encoder.pkl")

def classify_alert(alert_type):
    if alert_type not in label_encoder.classes_:
        return "Unknown Alert Type"

    encoded_alert = label_encoder.transform([alert_type])[0]
    prediction = model.predict([[encoded_alert]])[0]

    if prediction == 1:
        return "True Positive"
    else:
        return "False Positive"

sample_alerts = ["DoS", "Port Scan", "SQL Injection", "Malware"]

results = []

for alert in sample_alerts:
    result = classify_alert(alert)
    results.append({
        "Alert_Type": alert,
        "Classification": result
    })
    print(f"{alert}: {result}")

results_df = pd.DataFrame(results)
results_df.to_csv("snort_ml_predictions.csv", index=False)

df["label_text"] = df["label"].map({
    1: "True Positive",
    0: "False Positive"
})

count_data = df["label_text"].value_counts()

plt.figure(figsize=(7, 5))
count_data.plot(kind="bar")
plt.title("Snort Alert Classification Distribution")
plt.xlabel("Alert Classification")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("snort_alert_distribution.png")
plt.close()

with open("snort_ml_report.txt", "w") as file:
    file.write("Lab 06: Intrusion Detection with Snort and Machine Learning\n\n")
    file.write("Objective:\n")
    file.write("Use Snort IDS and machine learning to classify alerts as true positives or false positives.\n\n")
    file.write("Model Used: RandomForestClassifier\n")
    file.write("Feature Used: alert_type_encoded\n")
    file.write(f"Model Accuracy: {accuracy:.2f}\n\n")
    file.write("Sample Predictions:\n")
    file.write(results_df.to_string(index=False))
    file.write("\n\nConclusion:\n")
    file.write("The ML model can classify Snort alert types and help reduce false positives.\n")

print("\nFiles saved:")
print("snort_alert_dataset.csv")
print("snort_false_positive_model.pkl")
print("alert_label_encoder.pkl")
print("snort_ml_predictions.csv")
print("snort_alert_distribution.png")
print("snort_ml_report.txt")

print("\nLab completed successfully.")
