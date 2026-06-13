import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Load dataset
column_names = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "class"
]

df = pd.read_csv(
    "iris.csv",
    header=None,
    names=column_names
)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Simulate missing values
df.loc[2, 'sepal_length'] = None
df.loc[5, 'petal_width'] = None

print("\n===== DATASET WITH MISSING VALUES =====")
print(df.head(10))

# Handle missing values
df['sepal_length'] = df['sepal_length'].fillna(
    df['sepal_length'].mean()
)

df['petal_width'] = df['petal_width'].fillna(
    df['petal_width'].mean()
)

print("\n===== AFTER HANDLING MISSING VALUES =====")
print(df.head(10))

# Normalize data
numerical_columns = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width'
]

scaler = MinMaxScaler()

df[numerical_columns] = scaler.fit_transform(
    df[numerical_columns]
)

print("\n===== AFTER NORMALIZATION =====")
print(df.head())

# Features and labels
X = df[numerical_columns]
y = df['class']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n===== DATA SPLIT =====")
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
