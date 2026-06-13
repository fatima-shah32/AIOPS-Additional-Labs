import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing, make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


try:
    # Load California housing dataset
    data = fetch_california_housing()

    df = pd.DataFrame(
        data.data,
        columns=data.feature_names
    )

    df["target"] = data.target

    print("California Housing Dataset Loaded Successfully")

except Exception as e:
    print("California dataset could not be loaded.")
    print("Using synthetic regression dataset instead.")
    print("Reason:", e)

    # Backup dataset if internet is not available
    X_data, y_data = make_regression(
        n_samples=1000,
        n_features=8,
        noise=20,
        random_state=42
    )

    feature_names = [
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude"
    ]

    df = pd.DataFrame(
        X_data,
        columns=feature_names
    )

    df["target"] = y_data


print("\nFirst 5 rows of dataset:")
print(df.head())

# Split features and target
X = df.drop("target", axis=1)
y = df["target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Initialize model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model parameters
print("\nModel Coefficients:")
print(model.coef_)

print("\nModel Intercept:")
print(model.intercept_)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2_score = model.score(X_test, y_test)

print("\nMean Squared Error MSE:")
print(mse)

print("\nR-squared Score:")
print(r2_score)

print("\nLab Completed Successfully")
