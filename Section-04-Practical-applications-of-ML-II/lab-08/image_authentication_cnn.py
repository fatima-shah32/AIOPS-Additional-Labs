import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

print("=== Lab 08: Image-Based Authentication using CNN ===")

# Create simulated user image dataset
os.makedirs("dataset/user1", exist_ok=True)
os.makedirs("dataset/user2", exist_ok=True)

img_size = (64, 64)

# Generate simple synthetic images for user1 and user2
for i in range(30):
    img_user1 = np.zeros((64, 64, 3), dtype=np.uint8)
    img_user1[:, :, 0] = 255
    cv2.circle(img_user1, (32, 32), 15 + i % 5, (255, 255, 255), -1)
    cv2.imwrite(f"dataset/user1/img_{i}.jpg", img_user1)

    img_user2 = np.zeros((64, 64, 3), dtype=np.uint8)
    img_user2[:, :, 1] = 255
    cv2.rectangle(img_user2, (15, 15), (45, 45), (255, 255, 255), -1)
    cv2.imwrite(f"dataset/user2/img_{i}.jpg", img_user2)

print("\nSynthetic dataset created successfully.")

def load_images_from_directory(directory, img_size=(64, 64)):
    images = []
    labels = []
    label_dict = {}
    label_count = 0

    for folder in sorted(os.listdir(directory)):
        folder_path = os.path.join(directory, folder)

        if os.path.isdir(folder_path):
            label_dict[label_count] = folder

            for img_name in os.listdir(folder_path):
                img_path = os.path.join(folder_path, img_name)

                img = cv2.imread(img_path)

                if img is None:
                    continue

                img = cv2.resize(img, img_size)
                images.append(img)
                labels.append(label_count)

            label_count += 1

    images = np.array(images, dtype="float32") / 255.0
    labels = np.array(labels)

    return images, labels, label_dict

images, labels, label_dict = load_images_from_directory("dataset", img_size)

print("\nLoaded images shape:", images.shape)
print("Labels shape:", labels.shape)
print("Label dictionary:", label_dict)

X_train, X_test, y_train, y_test = train_test_split(
    images,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)

def create_cnn_model(input_shape=(64, 64, 3), num_classes=2):
    model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=input_shape),
        MaxPooling2D(pool_size=(2, 2)),

        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),

        Flatten(),

        Dense(128, activation="relu"),
        Dropout(0.5),

        Dense(num_classes, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

model = create_cnn_model(
    input_shape=(64, 64, 3),
    num_classes=len(label_dict)
)

print("\nModel Summary:")
model.summary()

history = model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=8,
    validation_data=(X_test, y_test),
    verbose=1
)

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

print("\nTest Accuracy:", round(test_acc, 4))

def authenticate_user(model, image_path, label_dict):
    img = cv2.imread(image_path)

    if img is None:
        return "Image not found"

    img = cv2.resize(img, (64, 64))
    img = np.expand_dims(img, axis=0) / 255.0

    prediction = model.predict(img, verbose=0)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)

    predicted_user = label_dict[predicted_class]

    return predicted_user, confidence

sample_image_path = "dataset/user1/img_0.jpg"
authenticated_user, confidence = authenticate_user(
    model,
    sample_image_path,
    label_dict
)

print("\nAuthentication Result:")
print("Authenticated User:", authenticated_user)
print("Confidence:", round(float(confidence), 4))

# Save model
model.save("image_authentication_cnn.keras")

# Save label dictionary
label_df = pd.DataFrame({
    "label": list(label_dict.keys()),
    "user": list(label_dict.values())
})

label_df.to_csv("label_dictionary.csv", index=False)

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv("training_history.csv", index=False)

# Plot accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("CNN Image Authentication Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("authentication_accuracy.png")
plt.close()

# Plot loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("CNN Image Authentication Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("authentication_loss.png")
plt.close()

# Save report
with open("image_authentication_report.txt", "w") as file:
    file.write("Lab 08: Image-Based Authentication using CNN\n\n")
    file.write("Objective:\n")
    file.write("Design and implement a CNN for image-based authentication.\n\n")
    file.write("Dataset:\n")
    file.write("Synthetic user image dataset with two users.\n\n")
    file.write("Model Architecture:\n")
    file.write("Conv2D -> MaxPooling -> Conv2D -> MaxPooling -> Flatten -> Dense -> Dropout -> Softmax\n\n")
    file.write(f"Test Accuracy: {test_acc:.4f}\n")
    file.write(f"Sample Authentication User: {authenticated_user}\n")
    file.write(f"Confidence: {confidence:.4f}\n\n")
    file.write("Conclusion:\n")
    file.write("The CNN learned to classify user-specific images and authenticate users based on image input.\n")

print("\nFiles saved:")
print("image_authentication_cnn.keras")
print("label_dictionary.csv")
print("training_history.csv")
print("authentication_accuracy.png")
print("authentication_loss.png")
print("image_authentication_report.txt")

print("\nLab completed successfully.")
