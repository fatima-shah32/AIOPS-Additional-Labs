import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("=== Lab 03: ML-driven Continuous Integration in DevOps ===")

data = {
    "build_number": [1,2,3,4,5,6,7,8,9,10],
    "build_duration": [120,150,180,100,200,50,90,220,130,170],
    "commit_size": [5,8,2,3,10,1,4,12,6,9],
    "previous_failures": [0,1,1,0,2,1,0,3,1,2],
    "build_status": [1,0,0,1,0,0,1,0,1,0]
}

df = pd.DataFrame(data)
df.to_csv("results/build_history.csv", index=False)

X = df[["build_duration", "commit_size", "previous_failures"]]
y = df["build_status"]

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
report = classification_report(y_test, y_pred, zero_division=0)

print("Model Accuracy:", round(accuracy, 4))
print(report)

joblib.dump(model, "results/build_failure_model.pkl")

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
plt.imshow(cm)
plt.title("Build Failure Prediction Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.xticks([0, 1], ["Failure", "Success"])
plt.yticks([0, 1], ["Failure", "Success"])
plt.colorbar()
plt.tight_layout()
plt.savefig("results/confusion_matrix.png")
plt.close()

new_build = pd.DataFrame({
    "build_duration": [150],
    "commit_size": [5],
    "previous_failures": [2]
})

prediction = model.predict(new_build)[0]

result = "Success" if prediction == 1 else "Failure"

print("New Build Prediction:", result)

with open("reports/final_report.txt", "w") as file:
    file.write("Lab 03: ML-driven Continuous Integration in DevOps\n\n")
    file.write("Objective:\n")
    file.write("Predict CI build failures using machine learning.\n\n")
    file.write("Model Used: RandomForestClassifier\n")
    file.write(f"Accuracy: {accuracy:.4f}\n\n")
    file.write("Classification Report:\n")
    file.write(report)
    file.write("\n\nNew Build Prediction: " + result)

print("Lab completed successfully.")
