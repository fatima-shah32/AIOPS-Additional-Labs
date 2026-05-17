import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# Threat Intelligence Reports
# =====================================================

threat_reports = [
    "A new variant of the Trojan horse malware has been detected, which exploits a vulnerability in web browsers.",

    "A spear-phishing attack has been identified targeting corporate email accounts with a fake invoice attached.",

    "Ransomware attacks are on the rise, with attackers demanding payment in Bitcoin from victims.",

    "A vulnerability in the SSL/TLS protocol has been discovered, allowing man-in-the-middle attacks.",

    "Phishing emails impersonating well-known banking institutions are being sent to customers, asking for login credentials."
]

# =====================================================
# Tokenization Function
# =====================================================

def tokenize_text(text):

    with open("temp.txt", "w") as file:
        file.write(text)

    tokens = text.split()

    return tokens

# =====================================================
# POS Tagging and NER Function
# =====================================================

def pos_tag_and_ner(text):

    words = text.split()

    pos_tags = []

    for word in words:
        if word.lower() in ["attack", "attacks", "malware", "phishing", "ransomware"]:
            pos_tags.append((word, "NN"))
        else:
            pos_tags.append((word, "WORD"))

    named_entities = []

    for word in words:
        if "bitcoin" in word.lower():
            named_entities.append(word)

    return pos_tags, named_entities

# =====================================================
# Categorization Function
# =====================================================

def categorize_report(text):

    text = text.lower()

    if "malware" in text:
        return "Malware"

    elif "phishing" in text:
        return "Phishing"

    elif "ransomware" in text:
        return "Ransomware"

    else:
        return "General Threat"

# =====================================================
# Process Reports
# =====================================================

results = []

categories = []

for report in threat_reports:

    tokens = tokenize_text(report)

    pos_tags, entities = pos_tag_and_ner(report)

    category = categorize_report(report)

    categories.append(category)

    results.append({
        "report": report,
        "tokens": tokens,
        "pos_tags": pos_tags,
        "named_entities": entities,
        "category": category
    })

# =====================================================
# Create DataFrame
# =====================================================

df = pd.DataFrame(results)

print("\n========== THREAT REPORT ANALYSIS ==========\n")

print(df[["report", "category"]])

# =====================================================
# Save CSV Results
# =====================================================

df.to_csv("threat_report_analysis.csv", index=False)

# =====================================================
# Visualize Category Distribution
# =====================================================

category_counts = pd.Series(categories).value_counts()

plt.figure(figsize=(8, 6))

category_counts.plot(
    kind='bar',
    color='skyblue',
    edgecolor='black'
)

plt.title("Threat Report Categories Distribution")

plt.xlabel("Category")

plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("threat_categories_distribution.png")

print("\n========== FILES GENERATED ==========")

print("1. threat_report_analysis.csv")

print("2. threat_categories_distribution.png")
