import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import spacy

# =====================================================
# Load spaCy Model
# =====================================================

nlp = spacy.load("en_core_web_sm")

# =====================================================
# Sample Documentation
# =====================================================

documentation = """
# Project Documentation

## Introduction
This project automates the deployment pipeline for the system.
It includes a CI/CD setup using Jenkins, GitHub Actions, and Docker.

## Setup
1. Clone the repository.
2. Install dependencies.
3. Run docker-compose up to start the application.

## Best Practices
- Ensure all tests pass before merging pull requests.
- Use Docker for local development to ensure consistency.

## Troubleshooting
If you encounter issues with Docker containers,
try restarting the service using docker-compose restart.
"""

# =====================================================
# Completeness Check
# =====================================================

required_sections = [
    "Introduction",
    "Setup",
    "Best Practices",
    "Troubleshooting"
]

def check_completeness(documentation, required_sections):

    missing_sections = [
        section for section in required_sections
        if section.lower() not in documentation.lower()
    ]

    return missing_sections

missing_sections = check_completeness(
    documentation,
    required_sections
)

print("\n========== COMPLETENESS CHECK ==========\n")

print("Missing Sections:", missing_sections)

# =====================================================
# Consistency Check
# =====================================================

def check_consistency(documentation):

    words = re.findall(
        r'\b\w+\b',
        documentation.lower()
    )

    word_counts = Counter(words)

    repeated_words = {
        word: count
        for word, count in word_counts.items()
        if count > 1
    }

    return repeated_words

repeated_words = check_consistency(documentation)

print("\n========== CONSISTENCY CHECK ==========\n")

print("Repeated Words:", repeated_words)

# =====================================================
# Clarity Check
# =====================================================

def check_clarity(documentation):

    doc = nlp(documentation)

    long_sentences = [
        sent.text.strip()
        for sent in doc.sents
        if len(sent.text.split()) > 20
    ]

    entities = [ent.text for ent in doc.ents]

    return long_sentences, entities

long_sentences, entities = check_clarity(documentation)

print("\n========== CLARITY CHECK ==========\n")

print("Long Sentences:")
print(long_sentences)

print("\nEntities:")
print(entities)

# =====================================================
# Save Results
# =====================================================

results = {
    "missing_sections": [str(missing_sections)],
    "entities": [str(entities)],
    "long_sentences": [str(long_sentences)]
}

df = pd.DataFrame(results)

df.to_csv(
    "documentation_quality_results.csv",
    index=False
)

# =====================================================
# Visualization 1
# Documentation Completeness
# =====================================================

section_status = [
    0 if section in missing_sections else 1
    for section in required_sections
]

plt.figure(figsize=(8, 6))

plt.bar(
    required_sections,
    section_status,
    color='lightblue',
    edgecolor='black'
)

plt.title("Documentation Completeness Check")

plt.xlabel("Sections")

plt.ylabel("Present (1) / Missing (0)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "documentation_completeness_chart.png"
)

# =====================================================
# Visualization 2
# Repeated Words
# =====================================================

if repeated_words:

    plt.figure(figsize=(10, 6))

    plt.bar(
        repeated_words.keys(),
        repeated_words.values(),
        color='lightcoral',
        edgecolor='black'
    )

    plt.title("Repeated Words in Documentation")

    plt.xlabel("Words")

    plt.ylabel("Frequency")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "documentation_repeated_words_chart.png"
    )

print("\n========== FILES GENERATED ==========")

print("1. documentation_quality_results.csv")

print("2. documentation_completeness_chart.png")

print("3. documentation_repeated_words_chart.png")
