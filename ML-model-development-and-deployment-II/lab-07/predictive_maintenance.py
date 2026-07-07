import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

print("="*60)
print("Predictive Maintenance using Machine Learning")
print("="*60)

np.random.seed(42)

data = {
    "usage_hours": np.random.randint(500,5000,1000),
    "operating_temperature": np.random.uniform(20,80,1000),
    "last_maintenance": np.random.randint(100,1000,1000),
    "failure_status": np.random.choice([0,1],1000,p=[0.8,0.2])
}

df = pd.DataFrame(data)

df.to_csv("results/maintenance_dataset.csv",index=False)

print(df.head())

X = df[['usage_hours',
        'operating_temperature',
        'last_maintenance']]

y = df['failure_status']

X_train,X_test,y_train,y_test=train_test_split(
X,
y,
test_size=0.20,
random_state=42
)

print("\nTraining Samples :",len(X_train))
print("Testing Samples :",len(X_test))

model=LogisticRegression(max_iter=1000)

model.fit(X_train,y_train)

prediction=model.predict(X_test)

accuracy=accuracy_score(y_test,prediction)

print("\nAccuracy :",accuracy)

print("\nClassification Report\n")

print(classification_report(y_test,prediction))

prediction_df=X_test.copy()

prediction_df["Actual"]=y_test

prediction_df["Prediction"]=prediction

prediction_df.to_csv(
"results/prediction_results.csv",
index=False
)

cm=confusion_matrix(y_test,prediction)

disp=ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot(cmap=plt.cm.Blues)

plt.title("Confusion Matrix")

plt.savefig("results/confusion_matrix.png")

plt.close()

new_component=np.array([[3500,70,300]])

failure_probability=model.predict_proba(new_component)[0][1]

print("\nFailure Probability :",round(failure_probability,2))

if failure_probability>0.70:

    print("Component likely to fail.")
    print("Initiate Proactive Maintenance.")

else:

    print("Component operating normally.")

with open("reports/final_report.txt","w") as report:

    report.write("Lab 07\n")
    report.write("Predictive Maintenance ML Model\n\n")
    report.write(f"Accuracy : {accuracy}\n")
    report.write(f"Failure Probability : {failure_probability}\n")
    report.write("Dataset Generated Successfully\n")
    report.write("Prediction Completed Successfully\n")

print("\nLab Completed Successfully")
