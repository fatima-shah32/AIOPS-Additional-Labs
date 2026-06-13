import numpy as np

# Function to implement linear regression using Normal Equation
def linear_regression(X, y):
    # Add bias/intercept column
    X_b = np.c_[np.ones((X.shape[0], 1)), X]

    # Normal Equation: theta = (X.T X)^-1 X.T y
    theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    return theta


# Function to calculate Mean Squared Error
def mean_squared_error(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()


# Create simple dataset
np.random.seed(42)

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Train model
theta = linear_regression(X, y)

print("Calculated model parameters theta:")
print(theta)

print("\nIntercept:", theta[0][0])
print("Slope:", theta[1][0])

# Make predictions
X_b = np.c_[np.ones((X.shape[0], 1)), X]
y_pred = X_b.dot(theta)

# Evaluate model
mse = mean_squared_error(y, y_pred)

print("\nMean Squared Error MSE:")
print(mse)

print("\nLab Completed Successfully")
