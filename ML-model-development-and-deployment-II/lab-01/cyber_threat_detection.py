import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

print("=== Lab 01: Advanced Cyber Threat Detection ===")

data_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/KDD%20Cup%201999%20Data/kddcup.data_10_percent.csv"

columns = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root",
    "num_file_creations", "num_shells", "num_access_files",
    "num_outbound_cmds", "is_hot_login", "is_guest_login", "count",
    "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate",
    "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
    "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"
]

print("\nLoading dataset...")
df = pd.read_csv(data_url, header=None, names=columns)

# Use a smaller sample for beginner cloud machines
df = df.sample(n=20000, random_state=42)

print("Dataset shape:", df.shape)
df.to_csv("results/raw_sample_kdd.csv", index=False)

# Convert labels into binary classes
# normal = 0, attack = 1
df["binary_label"] = df["label"].apply(lambda x: 0 if x == "normal." else 1)

# Encode categorical columns
label_encoders = {}

for column in ["protocol_type", "service", "flag"]:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    label_encoders[column] = encoder

print("\nMissing values:")
print(df.isnull().sum().sum())

# Features and target
X = df.drop(["label", "binary_label"], axis=1)
y = df["binary_label"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# Random Forest model
print("\nTraining Random Forest model...")

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_predictions)

rf_report = classification_report(y_test, rf_predictions)

print("\nRandom Forest Accuracy:", round(rf_accuracy, 4))
print(rf_report)

with open("reports/random_forest_report.txt", "w") as file:
    file.write("Random Forest Cyber Threat Detection Report\n\n")
    file.write(f"Accuracy: {rf_accuracy:.4f}\n\n")
    file.write(rf_report)

# TensorFlow model
print("\nTraining TensorFlow deep learning model...")

tf_model = Sequential([
    Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(32, activation="relu"),
    Dense(16, activation="relu"),
    Dense(1, activation="sigmoid")
])

tf_model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

history = tf_model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=64,
    validation_data=(X_test, y_test),
    verbose=1
)

test_loss, test_accuracy = tf_model.evaluate(X_test, y_test, verbose=0)

print("\nTensorFlow Test Accuracy:", round(test_accuracy, 4))

tf_model.save("results/cyber_threat_detection_model.keras")

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv("results/tensorflow_training_history.csv", index=False)

# Plot TensorFlow accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("TensorFlow Cyber Threat Detection Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/tensorflow_accuracy.png")
plt.close()

# Plot TensorFlow loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("TensorFlow Cyber Threat Detection Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/tensorflow_loss.png")
plt.close()

# Compare models
comparison_df = pd.DataFrame({
    "Model": ["Random Forest", "TensorFlow Neural Network"],
    "Accuracy": [rf_accuracy, test_accuracy]
})

comparison_df.to_csv("results/model_comparison.csv", index=False)

plt.figure(figsize=(7, 5))
plt.bar(comparison_df["Model"], comparison_df["Accuracy"])
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig("results/model_comparison.png")
plt.close()

with open("reports/final_report.txt", "w") as file:
    file.write("Lab 01: Advanced Cyber Threat Detection with Open-source ML Frameworks\n\n")
    file.write("Objective:\n")
    file.write("Implement and optimize machine learning models for cyber threat detection.\n\n")
    file.write("Dataset:\n")
    file.write("KDD Cup 1999 10 percent dataset sample.\n\n")
    file.write("Preprocessing:\n")
    file.write("- Encoded categorical features\n")
    file.write("- Converted labels into binary classification\n")
    file.write("- Applied StandardScaler\n")
    file.write("- Split data into training and testing sets\n\n")
    file.write("Models Trained:\n")
    file.write("1. Random Forest Classifier\n")
    file.write("2. TensorFlow Neural Network\n\n")
    file.write(f"Random Forest Accuracy: {rf_accuracy:.4f}\n")
    file.write(f"TensorFlow Accuracy: {test_accuracy:.4f}\n\n")
    file.write("Conclusion:\n")
    file.write("Both models successfully classified network traffic as normal or anomalous.\n")

print("\nFiles saved:")
print("results/raw_sample_kdd.csv")
print("results/cyber_threat_detection_model.keras")
print("results/tensorflow_accuracy.png")
print("results/tensorflow_loss.png")
print("results/model_comparison.csv")
print("results/model_comparison.png")
print("reports/random_forest_report.txt")
print("reports/final_report.txt")

print("\nLab completed successfully.")
