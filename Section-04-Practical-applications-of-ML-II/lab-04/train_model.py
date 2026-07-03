import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("=== Training Build Outcome Prediction Model ===")

data = {
    "Build_Time": [15, 12, 10, 20, 18, 9, 22, 11, 14, 25],
    "Tests_Passed": [50, 45, 55, 40, 42, 60, 35, 58, 52, 30],
    "Tests_Failed": [2, 5, 0, 7, 6, 0, 9, 1, 2, 10],
    "Build_Outcome": [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df[["Build_Time", "Tests_Passed", "Tests_Failed"]]
y = df["Build_Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

joblib.dump(model, "build_outcome_model.pkl")

df.to_csv("build_history.csv", index=False)

with open("model_training_report.txt", "w") as file:
    file.write("Lab 04: CI/CD Pipeline Enhancement with Jenkins and ML\n\n")
    file.write("Model Used: RandomForestClassifier\n")
    file.write("Features: Build_Time, Tests_Passed, Tests_Failed\n")
    file.write("Target: Build_Outcome\n\n")
    file.write(f"Model Accuracy: {accuracy:.2f}\n")

print("Model saved as build_outcome_model.pkl")
print(f"Model Accuracy: {accuracy:.2f}")
print("Training completed successfully.")
