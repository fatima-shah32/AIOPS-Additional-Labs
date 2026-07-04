import os
import random
import string
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from cryptography.fernet import Fernet
from sklearn.preprocessing import LabelEncoder

print("=== Lab 02: Secure Cloud Data Storage with ML-enhanced Encryption ===")

# Local simulated OpenStack object storage
os.makedirs("cloud_storage/secure-data-storage", exist_ok=True)

# Generate training data
def generate_random_data(num_samples=1000, length=10):
    characters = string.ascii_lowercase + string.digits
    return [
        ''.join(random.choices(characters, k=length))
        for _ in range(num_samples)
    ]

data = generate_random_data()

df = pd.DataFrame({"sample_data": data})
df.to_csv("results/sample_training_data.csv", index=False)

# Encode characters
all_chars = list(string.ascii_lowercase + string.digits)
encoder = LabelEncoder()
encoder.fit(all_chars)

encoded_data = []

for sample in data:
    encoded_sample = encoder.transform(list(sample))
    encoded_data.append(encoded_sample)

X = np.array(encoded_data, dtype=np.float32)
y = X

# Normalize data
X = X / X.max()
y = y / y.max()

print("Training data shape:", X.shape)

# Build ML autoencoder model
input_dim = X.shape[1]

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(input_dim,)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(input_dim, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

model.summary()

history = model.fit(
    X,
    y,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

model.save("results/ml_encryption_model.keras")

# Generate real encryption key using cryptography
encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)

with open("results/encryption_key.txt", "wb") as key_file:
    key_file.write(encryption_key)

# ML-assisted encryption simulation
sample_text = "securedata"

sample_encoded = encoder.transform(list(sample_text))
sample_scaled = np.array([sample_encoded], dtype=np.float32) / max(encoder.transform(all_chars))

ml_output = model.predict(sample_scaled, verbose=0)

# Convert ML output to string and encrypt using Fernet
ml_output_string = str(ml_output.tolist())

encrypted_data = cipher.encrypt(ml_output_string.encode())

object_name = "encrypted_sample_1.txt"
object_path = f"cloud_storage/secure-data-storage/{object_name}"

with open(object_path, "wb") as file:
    file.write(encrypted_data)

print("\nEncrypted object stored at:", object_path)

# Retrieve and decrypt
with open(object_path, "rb") as file:
    stored_encrypted_data = file.read()

decrypted_data = cipher.decrypt(stored_encrypted_data).decode()

print("\nOriginal Text:", sample_text)
print("Encrypted Data:", encrypted_data[:80], b"...")
print("Decrypted ML Output:", decrypted_data[:100], "...")

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv("results/training_history.csv", index=False)

# Plot loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("ML Encryption Model Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/ml_encryption_loss.png")
plt.close()

# Save storage log
storage_log = pd.DataFrame({
    "object_name": [object_name],
    "storage_path": [object_path],
    "encryption_method": ["ML-assisted + Fernet encryption"],
    "status": ["Stored Successfully"]
})

storage_log.to_csv("results/storage_log.csv", index=False)

# Report
with open("reports/final_report.txt", "w") as report:
    report.write("Lab 02: Secure Cloud Data Storage with ML-enhanced Encryption\n\n")
    report.write("Objective:\n")
    report.write("Design and implement a cloud-based storage system with ML-enhanced encryption.\n\n")
    report.write("Storage System:\n")
    report.write("Local simulated OpenStack object storage.\n\n")
    report.write("Encryption Method:\n")
    report.write("TensorFlow autoencoder simulation with Fernet encryption.\n\n")
    report.write("Files Generated:\n")
    report.write("- sample_training_data.csv\n")
    report.write("- ml_encryption_model.keras\n")
    report.write("- encryption_key.txt\n")
    report.write("- encrypted_sample_1.txt\n")
    report.write("- training_history.csv\n")
    report.write("- ml_encryption_loss.png\n")
    report.write("- storage_log.csv\n\n")
    report.write("Conclusion:\n")
    report.write("The lab successfully simulated secure cloud storage with ML-enhanced encryption.\n")

print("\nFiles saved successfully.")
print("Lab completed successfully.")
