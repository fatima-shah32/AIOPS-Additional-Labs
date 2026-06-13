from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = datasets.load_iris()

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

# Basic SVM model with linear kernel
basic_model = SVC(kernel="linear", random_state=42)

# Train basic model
basic_model.fit(X_train, y_train)

# Predict using basic model
basic_y_pred = basic_model.predict(X_test)

# Evaluate basic model
basic_accuracy = accuracy_score(y_test, basic_y_pred)

print("\nBasic SVM Model Accuracy:")
print(f"{basic_accuracy * 100:.2f}%")

# Hyperparameter tuning using GridSearchCV
param_grid = {
    "C": [0.1, 1, 10],
    "kernel": ["linear", "rbf"],
    "gamma": ["scale", "auto"]
}

svm_model = SVC(random_state=42)

grid_search = GridSearchCV(
    estimator=svm_model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    verbose=1
)

# Train GridSearchCV
grid_search.fit(X_train, y_train)

print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest Cross-validation Accuracy:")
print(grid_search.best_score_)

# Evaluate best model
best_model = grid_search.best_estimator_
tuned_y_pred = best_model.predict(X_test)

tuned_accuracy = accuracy_score(y_test, tuned_y_pred)

print("\nModel Accuracy After Tuning:")
print(f"{tuned_accuracy * 100:.2f}%")

print("\nPredicted Labels:")
print(tuned_y_pred)

print("\nActual Labels:")
print(y_test)

print("\nLab Completed Successfully")
