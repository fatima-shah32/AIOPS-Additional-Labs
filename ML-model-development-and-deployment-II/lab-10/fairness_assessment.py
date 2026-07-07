import pandas as pd

import joblib

try:

    from aif360.datasets import StandardDataset

    from aif360.metrics import BinaryLabelDatasetMetric

    from aif360.algorithms.preprocessing import Reweighing

    FAIRNESS=True

except:

    FAIRNESS=False

model=joblib.load("trained_model.pkl")

data={

"cpu_usage":[30,40,50,60,70],

"packet_size":[1000,1500,2000,2500,3000],

"anomaly_score":[0.1,0.2,0.3,0.4,0.5],

"gender":["Male","Female","Male","Female","Male"],

"label":[0,1,0,1,0]

}

df=pd.DataFrame(data)

print(df)

prediction=model.predict(

df[["cpu_usage","packet_size","anomaly_score"]]

)

print("\nPredictions")

print(prediction)

if FAIRNESS:

    dataset=StandardDataset(

        df,

        label_name="label",

        protected_attribute_names=["gender"],

        privileged_classes=[["Male"]]

    )

    metric=BinaryLabelDatasetMetric(

        dataset,

        privileged_groups=[{"gender":1}],

        unprivileged_groups=[{"gender":0}]

    )

    print("\nDisparate Impact")

    print(metric.disparate_impact())

    print("\nMean Difference")

    print(metric.mean_difference())

    reweigher=Reweighing(

        privileged_groups=[{"gender":1}],

        unprivileged_groups=[{"gender":0}]

    )

    transformed=reweigher.fit_transform(dataset)

    transformed_df=pd.DataFrame(

        transformed.features,

        columns=transformed.feature_names

    )

    transformed_df.to_csv(

        "results/transformed_dataset.csv",

        index=False

    )

    report=f"""

Disparate Impact : {metric.disparate_impact()}

Mean Difference : {metric.mean_difference()}

"""

else:

    report="""

AIF360 not installed.

Bias assessment skipped.

Model prediction completed successfully.

"""

with open(

"results/fairness_metrics.txt","w"

) as file:

    file.write(report)

with open(

"reports/final_report.txt","w"

) as reportfile:

    reportfile.write("""

Lab 10

Ethics Transparency and Bias

Completed Successfully

""")

print("\nLab Completed Successfully")
