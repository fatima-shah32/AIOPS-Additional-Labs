import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create synthetic dataset for regression
np.random.seed(42)

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training set size:", len(X_train))
print("Validation set size:", len(X_val))

# Initialize Linear Regression model
model = LinearRegression()

# Implement 5-fold cross-validation
kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

mse_scores = []

for train_index, val_index in kf.split(X):
    X_train_cv = X[train_index]
    X_val_cv = X[val_index]

    y_train_cv = y[train_index]
    y_val_cv = y[val_index]

    # Train model
    model.fit(X_train_cv, y_train_cv)

    # Predict validation fold
    y_pred = model.predict(X_val_cv)

    # Calculate MSE
    mse = mean_squared_error(y_val_cv, y_pred)
    mse_scores.append(mse)

print("\nMean Squared Error for each fold:")
print(mse_scores)

print("\nAverage MSE across all folds:")
print(np.mean(mse_scores))

# Train model on training set
model.fit(X_train, y_train)

# Predict validation set
y_pred_val = model.predict(X_val)

# Calculate validation MSE
mse_val = mean_squared_error(y_val, y_pred_val)

print("\nMean Squared Error on validation set:")
print(mse_val)

print("\nLab Completed Successfully")
