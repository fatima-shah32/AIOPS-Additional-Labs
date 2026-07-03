# Lab 04: CI/CD Pipeline Enhancement with Jenkins and Machine Learning

## Objective

Set up a Jenkins CI/CD pipeline and train a machine learning model to predict build outcomes.

## Tools Used

- Jenkins
- Python
- Scikit-learn
- Pandas
- Joblib
- Random Forest Classifier

## ML Features

```text
Build_Time
Tests_Passed
Tests_Failed

Target
Build_Outcome
1 = Success
0 = Failure
Tasks Performed
Installed Jenkins
Created lab folder
Created Python virtual environment
Installed ML libraries
Created build history dataset
Trained RandomForestClassifier
Saved trained model
Created prediction script
Created Jenkinsfile pipeline
Archived prediction results in Jenkins
Files
train_model.py
predict_build_outcome.py
Jenkinsfile
build_history.csv
build_outcome_model.pkl
model_training_report.txt
prediction_result.txt
README.md
Jenkins Pipeline Stages
Setup Python Environment
Train ML Model
Build
Test
Predict Build Outcome
Conclusion

This lab demonstrated how Jenkins CI/CD can be enhanced using machine learning. The ML model predicts whether a build is likely to succeed or fail based on build time and test results.
