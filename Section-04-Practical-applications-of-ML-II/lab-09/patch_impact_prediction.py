import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

print("="*60)
print("Lab 09 : Automating Security Patch Testing with ML")
print("="*60)

# ---------------------------------------------------
# Simulated Patch Dataset
# ---------------------------------------------------

data = {
    "Patch_ID": ["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10"],
    "Severity": ["Critical","High","Medium","Critical","Low","High","Medium","Critical","Low","High"],
    "Patch_Type":["OS","Application","Network","OS","Application","Network","OS","Application","Network","OS"],
    "Patch_Size_MB":[50,30,100,25,20,70,80,45,35,60],
    "System_Behavior_Post_Patch":[10,5,2,-5,0,3,8,-2,1,6]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset\n")
print(df)

# ---------------------------------------------------
# Encode categorical variables
# ---------------------------------------------------

severity_map = {
    "Critical":3,
    "High":2,
    "Medium":1,
    "Low":0
}

patch_map = {
    "OS":2,
    "Application":1,
    "Network":0
}

df["Severity"] = df["Severity"].map(severity_map)
df["Patch_Type"] = df["Patch_Type"].map(patch_map)

print("\nEncoded Dataset\n")
print(df)

# ---------------------------------------------------
# Features and Target
# ---------------------------------------------------

X = df[["Severity","Patch_Type","Patch_Size_MB"]]

y = df["System_Behavior_Post_Patch"]

# ---------------------------------------------------
# Split Dataset
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ---------------------------------------------------
# Train Model
# ---------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

y_pred = model.predict(X_test)

# ---------------------------------------------------
# Evaluation
# ---------------------------------------------------

mse = mean_squared_error(y_test,y_pred)

r2 = r2_score(y_test,y_pred)

print("\nModel Performance")
print("-------------------------")
print("Mean Squared Error :", round(mse,3))
print("R2 Score           :", round(r2,3))

# ---------------------------------------------------
# Predict New Patch
# ---------------------------------------------------

new_patch = pd.DataFrame({
    "Severity":[3],
    "Patch_Type":[2],
    "Patch_Size_MB":[50]
})

prediction = model.predict(new_patch)

print("\nPredicted Impact of New Patch")

print("Predicted System Behavior :", round(prediction[0],2))

# ---------------------------------------------------
# Plot
# ---------------------------------------------------

plt.figure(figsize=(6,5))

plt.scatter(y_test,y_pred,color="blue")

plt.plot(
    [min(y_test),max(y_test)],
    [min(y_test),max(y_test)],
    color="red"
)

plt.xlabel("Actual")

plt.ylabel("Predicted")

plt.title("Patch Impact Prediction")

plt.grid(True)

plt.savefig("patch_prediction.png")

plt.show()

print("\nGraph saved as patch_prediction.png")

# ---------------------------------------------------
# Save report
# ---------------------------------------------------

with open("report.txt","w") as f:

    f.write("Lab 09 - Automating Security Patch Testing with ML\n\n")

    f.write("Dataset Size : {}\n".format(len(df)))

    f.write("Mean Squared Error : {:.3f}\n".format(mse))

    f.write("R2 Score : {:.3f}\n".format(r2))

    f.write("Predicted Impact : {:.2f}\n".format(prediction[0]))

print("Report saved as report.txt")
