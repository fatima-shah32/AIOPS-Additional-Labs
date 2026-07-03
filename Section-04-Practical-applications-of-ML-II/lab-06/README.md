# Lab 06: Intrusion Detection with Snort and Machine Learning

## Objective

Set up Snort IDS and train a machine learning classifier to detect true positives and false positives from IDS alerts.

## Tools Used

- Snort IDS
- Python
- Pandas
- Scikit-learn
- Joblib
- Matplotlib

## Model Used

RandomForestClassifier

## Tasks Performed

1. Installed Snort IDS
2. Created Python virtual environment
3. Simulated Snort alert dataset
4. Encoded alert types using LabelEncoder
5. Trained Random Forest classifier
6. Classified alerts as true positive or false positive
7. Saved model and encoder
8. Generated prediction CSV, chart, and report

## Files

```text
snort_ml_false_positive.py
snort_alert_dataset.csv
snort_false_positive_model.pkl
alert_label_encoder.pkl
snort_ml_predictions.csv
snort_alert_distribution.png
snort_ml_report.txt
README.md

Conclusion

This lab demonstrated how Snort IDS can be enhanced with machine learning to reduce false positives and improve intrusion detection workflows.
