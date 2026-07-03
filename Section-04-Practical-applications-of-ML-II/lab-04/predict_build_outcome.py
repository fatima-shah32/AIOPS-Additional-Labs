import pandas as pd
import joblib

print("=== Predicting Jenkins Build Outcome ===")

model = joblib.load("build_outcome_model.pkl")

new_build_data = pd.DataFrame({
    "Build_Time": [15],
    "Tests_Passed": [50],
    "Tests_Failed": [2]
})

prediction = model.predict(new_build_data)[0]

result = "Success" if prediction == 1 else "Failure"

print("Build Data:")
print(new_build_data)

print("\nPredicted Build Outcome:", result)

with open("prediction_result.txt", "w") as file:
    file.write("Predicted Build Outcome: " + result + "\n")
