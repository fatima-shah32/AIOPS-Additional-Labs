import pandas as pd
import spacy
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =========================
# STEP 1: DATASET (FIXED + BALANCED)
# =========================

data = {
    "user_story": [
        "As a user, I want to log in using Google authentication.",
        "As a user, I want to log in using email and password.",
        "As a user, I want to reset my password.",
        "As a developer, I want to implement secure authentication system.",
        
        "As an admin, I want to manage user roles and permissions.",
        "As an admin, I want to delete inactive users.",
        "As an admin, I want to create new user accounts.",
        "As an admin, I want to assign roles to users.",
        
        "As a user, I want to search products in the system.",
        "As a user, I want to filter search results.",
        "As a user, I want to sort products by price.",
        "As a user, I want to view product recommendations.",
        
        "As a developer, I want to improve system performance using caching.",
        "As a developer, I want to optimize API response time.",
        "As a developer, I want to reduce server latency.",
        "As a developer, I want to improve database query performance."
    ],
    "category": [
        "Authentication",
        "Authentication",
        "Authentication",
        "Authentication",

        "User Management",
        "User Management",
        "User Management",
        "User Management",

        "Search",
        "Search",
        "Search",
        "Search",

        "Performance",
        "Performance",
        "Performance",
        "Performance"
    ]
}

df = pd.DataFrame(data)

print("\n===== DATASET =====")
print(df)

print("\nCategory Distribution:")
print(df["category"].value_counts())

# =========================
# STEP 2: NLP (spaCy)
# =========================

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    pos_tags = [token.pos_ for token in doc]
    return tokens, pos_tags

df["tokens"], df["pos_tags"] = zip(*df["user_story"].map(preprocess))

print("\n===== NLP OUTPUT SAMPLE =====")
print(df[["user_story", "tokens", "pos_tags"]].head())

# =========================
# STEP 3: TF-IDF VECTORIZATION
# =========================

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["user_story"])
y = df["category"]

# =========================
# STEP 4: TRAIN MODEL (FIXED SPLIT)
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n===== MODEL RESULTS =====")
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=1))

# =========================
# STEP 5: CONFUSION MATRIX
# =========================

cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

plt.figure(figsize=(6, 4))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=model.classes_,
    yticklabels=model.classes_
)

plt.title("Confusion Matrix - User Story Classification")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.tight_layout()

# ✅ SAVE IMAGE INSTEAD OF SHOW
plt.savefig("screenshots/confusion_matrix.png", dpi=300)
print("Confusion matrix saved in screenshots folder")
