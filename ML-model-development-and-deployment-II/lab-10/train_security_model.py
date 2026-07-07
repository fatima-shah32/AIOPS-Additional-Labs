import pandas as pd

from sklearn.ensemble import RandomForestClassifier

import joblib

data={

"cpu_usage":[30,40,50,60,70],

"packet_size":[1000,1500,2000,2500,3000],

"anomaly_score":[0.1,0.2,0.3,0.4,0.5],

"label":[0,1,0,1,0]

}

df=pd.DataFrame(data)

X=df[["cpu_usage","packet_size","anomaly_score"]]

y=df["label"]

model=RandomForestClassifier(random_state=42)

model.fit(X,y)

joblib.dump(model,"trained_model.pkl")

print("Security Model Saved Successfully")
