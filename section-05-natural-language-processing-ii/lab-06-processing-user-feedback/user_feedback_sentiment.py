import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# =====================================================
# Simulated User Feedback Data
# =====================================================

feedback_data = {
    'user_feedback': [
        'The service is great, very happy with the performance!',
        'I am disappointed, the system crashes frequently.',
        'Good support, but the response time could be improved.',
        'Terrible experience, I will not use this again.',
        'Love the new update, it makes things easier!',
        'It was okay, nothing special but not bad either.',
        'Worst experience ever, everything is slow and unresponsive.',
        'Fantastic, everything works as expected, great job!',
        'The system is slow, but it gets the job done eventually.',
        'Happy with the service, but I wish there were more features.'
    ]
}

# =====================================================
# Create DataFrame
# =====================================================

df_feedback = pd.DataFrame(feedback_data)

print("\n========== USER FEEDBACK ==========\n")
print(df_feedback)

# =====================================================
# Sentiment Analysis Function
# =====================================================

def get_sentiment(text):

    blob = TextBlob(text)

    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    return polarity, subjectivity

# =====================================================
# Apply Sentiment Analysis
# =====================================================

df_feedback['polarity'], df_feedback['subjectivity'] = zip(
    *df_feedback['user_feedback'].apply(get_sentiment)
)

print("\n========== SENTIMENT ANALYSIS OUTPUT ==========\n")
print(df_feedback)

# =====================================================
# Save Results
# =====================================================

df_feedback.to_csv(
    "feedback_sentiment_results.csv",
    index=False
)

# =====================================================
# Bar Plot Visualization
# =====================================================

plt.figure(figsize=(10, 6))

plt.barh(
    df_feedback['user_feedback'],
    df_feedback['polarity'],
    color='skyblue',
    edgecolor='black'
)

plt.xlabel("Polarity")
plt.ylabel("User Feedback")
plt.title("Sentiment Polarity of User Feedback")

plt.tight_layout()

plt.savefig("sentiment_polarity_barplot.png")

# =====================================================
# Scatter Plot Visualization
# =====================================================

plt.figure(figsize=(8, 6))

plt.scatter(
    df_feedback['polarity'],
    df_feedback['subjectivity'],
    color='purple',
    alpha=0.7
)

plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.title("Polarity vs Subjectivity")

plt.grid(True)

plt.tight_layout()

plt.savefig("polarity_vs_subjectivity_scatter.png")

print("\n========== FILES GENERATED ==========")
print("1. feedback_sentiment_results.csv")
print("2. sentiment_polarity_barplot.png")
print("3. polarity_vs_subjectivity_scatter.png")
