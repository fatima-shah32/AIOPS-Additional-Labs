import joblib
import pandas as pd

model = joblib.load("results/build_failure_model.pkl")

new_build_features = pd.DataFrame({
    "build_duration": [150],
    "commit_size": [5],
    "previous_failures": [2]
})

prediction = model.predict(new_build_features)[0]

if prediction == 0:
    print("Build is predicted to FAIL. Notify developer before continuing.")
else:
    print("Build is predicted to SUCCEED. Proceeding with CI pipeline.")
