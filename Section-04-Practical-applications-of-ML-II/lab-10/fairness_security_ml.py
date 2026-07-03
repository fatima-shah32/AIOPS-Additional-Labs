import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from aif360.datasets import StandardDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import DisparateImpactRemover

print("=== Lab 10: Ethics & Fairness in Security ML Models ===")

# Simulated security dataset
data = {
    "feature1": [0.1, 0.2, 0.3, 0.5, 0.9, 1.2, 1.3, 1.5, 0.4, 0.8],
    "feature2": [10, 20, 30, 50, 80, 100, 120, 140, 35, 70],
    "gender":   [1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    "label":    [0, 0, 0, 1, 1, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
df.to_csv("security_fairness_dataset.csv", index=False)

print("\nDataset:")
print(df)

# Train security model
X = df[["feature1", "feature2", "gender"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy, 2))

# AIF360 dataset
dataset = StandardDataset(
    df,
    label_name="label",
    favorable_classes=[0],
    protected_attribute_names=["gender"],
    privileged_classes=[[1]],
    categorical_features=[],
    features_to_drop=[]
)

privileged_groups = [{"gender": 1}]
unprivileged_groups = [{"gender": 0}]

# Dataset fairness metrics
dataset_metric = BinaryLabelDatasetMetric(
    dataset,
    unprivileged_groups=unprivileged_groups,
    privileged_groups=privileged_groups
)

disparate_impact_before = dataset_metric.disparate_impact()
statistical_parity_before = dataset_metric.statistical_parity_difference()

print("\nFairness Metrics Before Mitigation:")
print("Disparate Impact:", disparate_impact_before)
print("Statistical Parity Difference:", statistical_parity_before)

# Apply Disparate Impact Remover
di_remover = DisparateImpactRemover(repair_level=1.0)
transformed_dataset = di_remover.fit_transform(dataset)

# Metrics after mitigation
transformed_metric = BinaryLabelDatasetMetric(
    transformed_dataset,
    unprivileged_groups=unprivileged_groups,
    privileged_groups=privileged_groups
)

disparate_impact_after = transformed_metric.disparate_impact()
statistical_parity_after = transformed_metric.statistical_parity_difference()

print("\nFairness Metrics After Mitigation:")
print("Disparate Impact:", disparate_impact_after)
print("Statistical Parity Difference:", statistical_parity_after)

# Save results
results_df = pd.DataFrame({
    "Metric": [
        "Disparate Impact",
        "Statistical Parity Difference"
    ],
    "Before_Mitigation": [
        disparate_impact_before,
        statistical_parity_before
    ],
    "After_Mitigation": [
        disparate_impact_after,
        statistical_parity_after
    ]
})

results_df.to_csv("fairness_metrics_results.csv", index=False)

# Plot fairness comparison
plt.figure(figsize=(8, 5))
plt.bar(
    ["DI Before", "DI After"],
    [disparate_impact_before, disparate_impact_after]
)
plt.title("Disparate Impact Before and After Mitigation")
plt.ylabel("Disparate Impact")
plt.tight_layout()
plt.savefig("fairness_disparate_impact.png")
plt.close()

# Save report
with open("fairness_security_report.txt", "w") as file:
    file.write("Lab 10: Ethics & Fairness in Security ML Models\n\n")
    file.write("Objective:\n")
    file.write("Evaluate and improve fairness of a security ML model using AI Fairness 360.\n\n")
    file.write("Model Used: RandomForestClassifier\n")
    file.write("Protected Attribute: gender\n")
    file.write("Privileged Group: gender = 1\n")
    file.write("Unprivileged Group: gender = 0\n\n")
    file.write(f"Model Accuracy: {accuracy:.2f}\n\n")
    file.write("Fairness Metrics Before Mitigation:\n")
    file.write(f"Disparate Impact: {disparate_impact_before}\n")
    file.write(f"Statistical Parity Difference: {statistical_parity_before}\n\n")
    file.write("Fairness Metrics After Mitigation:\n")
    file.write(f"Disparate Impact: {disparate_impact_after}\n")
    file.write(f"Statistical Parity Difference: {statistical_parity_after}\n\n")
    file.write("Conclusion:\n")
    file.write("AI Fairness 360 helps evaluate fairness in ML models and apply mitigation methods to reduce bias.\n")

print("\nFiles saved:")
print("security_fairness_dataset.csv")
print("fairness_metrics_results.csv")
print("fairness_disparate_impact.png")
print("fairness_security_report.txt")

print("\nLab completed successfully.")
