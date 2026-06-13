import numpy as np
import tensorflow as tf

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# One-hot encode labels
try:
    encoder = OneHotEncoder(sparse_output=False)
except TypeError:
    encoder = OneHotEncoder(sparse=False)

y_onehot = encoder.fit_transform(y.reshape(-1, 1))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_onehot,
    test_size=0.2,
    random_state=42
)

# Build neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")
])

# Compile model
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Train model
model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=16,
    verbose=1
)

# Evaluate model
test_loss, test_acc = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"\nTest accuracy: {test_acc * 100:.2f}%")

# Make predictions
y_pred = model.predict(X_test)

y_pred_classes = np.argmax(y_pred, axis=1)
y_test_classes = np.argmax(y_test, axis=1)

# Accuracy using sklearn
accuracy = accuracy_score(y_test_classes, y_pred_classes)

print(f"Accuracy on test set using sklearn: {accuracy * 100:.2f}%")

print("\nLab Completed Successfully")
