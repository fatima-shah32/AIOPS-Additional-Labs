import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Dataset (Phishing + Legitimate Emails)
# -----------------------------
data = {
    'email': [
        'Dear customer, you have won a $1000 gift card. Click here to claim it!',
        'Your invoice for this month is attached. Please review it and make the payment.',
        'Urgent: Your bank account has been compromised. Click here to secure it immediately.',
        'We are reaching out to confirm your appointment for tomorrow.',
        'Congratulations! You have a package waiting for pickup. Click here to track.',
        'Reminder: Your subscription to XYZ service will renew tomorrow.',
        'You have been selected for a lottery prize. Submit your details now.',
        'Meeting scheduled with team at 3 PM today in office.',
        'Security alert: suspicious login detected. Verify your account now.',
        'Please find attached project report for your review.'
    ],
    'label': [
        'phishing',
        'legitimate',
        'phishing',
        'legitimate',
        'phishing',
        'legitimate',
        'phishing',
        'legitimate',
        'phishing',
        'legitimate'
    ]
}

df = pd.DataFrame(data)

print("\nDataset:\n")
print(df)

# -----------------------------
# Text Cleaning
# -----------------------------
df['cleaned_email'] = df['email'].str.lower()

X = df['cleaned_email']
y = df['label']

# -----------------------------
# TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X)

print("\nFeature shape:", X_vectorized.shape)

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

print("Train size:", X_train.shape)
print("Test size:", X_test.shape)

# -----------------------------
# Model Training (Logistic Regression)
# -----------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -----------------------------
# Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d",
            xticklabels=['legitimate', 'phishing'],
            yticklabels=['legitimate', 'phishing'])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
