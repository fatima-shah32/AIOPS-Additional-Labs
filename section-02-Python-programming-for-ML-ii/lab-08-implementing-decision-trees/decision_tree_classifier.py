from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

print("Dataset loaded successfully")
print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("Total samples:", len(X))

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# Initialize Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)

# Train model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("\nPredicted labels:")
print(y_pred)

print("\nActual labels:")
print(y_test)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nLab Completed Successfully")
