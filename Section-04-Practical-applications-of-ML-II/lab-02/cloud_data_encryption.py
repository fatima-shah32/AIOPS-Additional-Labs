import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

print("=== Lab 02: Cloud Data Encryption with TensorFlow ===")

# Sample plaintext
plaintext = "Hello TensorFlow"

# Convert text to binary string
def text_to_binary(text):
    return ''.join(format(ord(char), "08b") for char in text)

# Convert binary string back to text
def binary_to_text(binary_string):
    chars = [
        binary_string[i:i + 8]
        for i in range(0, len(binary_string), 8)
    ]

    return ''.join(
        chr(int(char, 2))
        for char in chars
        if len(char) == 8
    )

# Simple encryption by bit inversion
def simple_encrypt(binary_string):
    return ''.join(
        "1" if bit == "0" else "0"
        for bit in binary_string
    )

# Convert plaintext to binary
binary_plaintext = text_to_binary(plaintext)

# Create encrypted target
encrypted_binary = simple_encrypt(binary_plaintext)

print("\nPlaintext:", plaintext)
print("Binary Plaintext:", binary_plaintext)
print("Encrypted Binary:", encrypted_binary)

# Prepare training data
X = np.array(
    [[int(bit) for bit in binary_plaintext]],
    dtype=np.float32
)

y = np.array(
    [[int(bit) for bit in encrypted_binary]],
    dtype=np.float32
)

input_dim = X.shape[1]

print("\nInput Shape:", X.shape)
print("Output Shape:", y.shape)

# Build neural network encryption model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation="relu", input_shape=(input_dim,)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(input_dim, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("\nModel Summary:")
model.summary()

# Train model
history = model.fit(
    X,
    y,
    epochs=300,
    batch_size=1,
    verbose=1
)

# Predict encrypted output
predicted_output = model.predict(X)

# Convert predictions to binary
predicted_binary = ''.join(
    "1" if value >= 0.5 else "0"
    for value in predicted_output[0]
)

# Decrypt predicted binary by reversing bit inversion
decrypted_binary = simple_encrypt(predicted_binary)
decrypted_text = binary_to_text(decrypted_binary)

print("\nPredicted Encrypted Binary:")
print(predicted_binary)

print("\nDecrypted Text:")
print(decrypted_text)

# Save results
results_df = pd.DataFrame({
    "Plaintext": [plaintext],
    "Binary_Plaintext": [binary_plaintext],
    "Encrypted_Binary_Target": [encrypted_binary],
    "Predicted_Encrypted_Binary": [predicted_binary],
    "Decrypted_Text": [decrypted_text]
})

results_df.to_csv("encryption_results.csv", index=False)

# Plot training loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.title("Neural Network Encryption Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("encryption_training_loss.png")
plt.close()

# Plot original vs predicted encrypted bits
plt.figure(figsize=(10, 5))
plt.plot(y[0], label="Target Encrypted Bits")
plt.plot(predicted_output[0], label="Predicted Encrypted Output")
plt.title("Target vs Predicted Encrypted Data")
plt.xlabel("Bit Index")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.savefig("encrypted_output_comparison.png")
plt.close()

# Save model
model.save("cloud_encryption_model.keras")

# Save report
with open("cloud_encryption_report.txt", "w") as file:
    file.write("Lab 02: Cloud Data Encryption with TensorFlow\n\n")
    file.write("Objective:\n")
    file.write("Design and implement a neural network model for simulating cloud data encryption.\n\n")

    file.write("Plaintext:\n")
    file.write(plaintext + "\n\n")

    file.write("Binary Plaintext:\n")
    file.write(binary_plaintext + "\n\n")

    file.write("Encrypted Binary Target:\n")
    file.write(encrypted_binary + "\n\n")

    file.write("Predicted Encrypted Binary:\n")
    file.write(predicted_binary + "\n\n")

    file.write("Decrypted Text:\n")
    file.write(decrypted_text + "\n\n")

    file.write("Conclusion:\n")
    file.write("A TensorFlow neural network was trained to learn a simple binary encryption mapping.\n")
    file.write("This is a learning simulation and not a replacement for real cryptographic encryption.\n")

print("\nFiles saved:")
print("cloud_encryption_model.keras")
print("encryption_results.csv")
print("encryption_training_loss.png")
print("encrypted_output_comparison.png")
print("cloud_encryption_report.txt")

print("\nLab completed successfully.")
