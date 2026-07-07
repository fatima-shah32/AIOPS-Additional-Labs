import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

print("="*60)
print("ML Enhanced Intrusion Detection using Snort")
print("="*60)

data = {

"src_ip":[
"192.168.1.1",
"192.168.1.2",
"10.0.0.1",
"10.0.0.2",
"172.16.0.1"
],

"dst_ip":[
"192.168.1.10",
"192.168.1.15",
"10.0.0.15",
"10.0.0.10",
"172.16.0.10"
],

"protocol":[1,2,1,3,1],

"src_port":[80,53,443,22,8080],

"dst_port":[443,53,80,22,443],

"packet_size":[1200,200,500,150,1000],

"duration":[30,20,100,10,60],

"label":[0,1,0,0,1]

}

df=pd.DataFrame(data)

df.to_csv("results/intrusion_logs.csv",index=False)

X=df[['protocol','src_port','dst_port','packet_size','duration']]
y=df['label']

X_train,X_test,y_train,y_test=train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

model=RandomForestClassifier(
n_estimators=100,
random_state=42
)

model.fit(X_train,y_train)

prediction=model.predict(X_test)

print("\nAccuracy")
print(accuracy_score(y_test,prediction))

print("\nClassification Report")
print(classification_report(y_test,prediction))

prediction_df=X_test.copy()
prediction_df["Actual"]=y_test
prediction_df["Prediction"]=prediction

prediction_df.to_csv(
"results/prediction_results.csv",
index=False
)

cm=confusion_matrix(y_test,prediction)

plt.imshow(cm,cmap="Blues")
plt.title("Confusion Matrix")
plt.colorbar()
plt.savefig("results/confusion_matrix.png")
plt.close()

importance=model.feature_importances_

plt.bar(
X.columns,
importance
)

plt.title("Feature Importance")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("results/feature_importance.png")

plt.close()

sample=[1,8080,443,1200,30]

result=model.predict([sample])[0]

print("\nPrediction on New Packet")

if result==1:

    print("Suspicious Traffic Detected")

else:

    print("Traffic is Normal")

with open("reports/final_report.txt","w") as f:

    f.write("Lab 06\n")
    f.write("ML Enhanced IDS using Snort\n\n")
    f.write("Model : Random Forest\n")
    f.write(f"Accuracy : {accuracy_score(y_test,prediction)}\n")
    f.write("Outputs generated successfully.\n")

print("\nLab Completed Successfully")
