import pandas as pd
import matplotlib.pyplot as plt
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# =========================
# Simulated Incident Logs
# =========================

incident_logs = [
    "2025-07-01 08:23:45 - ERROR - System crash on server 'web-server-01' due to memory overflow.",
    "2025-07-01 09:15:32 - WARNING - CPU usage exceeds 85% on server 'database-server-03'.",
    "2025-07-01 10:03:11 - INFO - Successful login attempt by user 'admin' on server 'auth-server-01'.",
    "2025-07-01 11:42:59 - ERROR - Security breach detected in 'api-server-04', unauthorized access attempt.",
    "2025-07-01 12:12:15 - INFO - Backup completed successfully on 'backup-server-01'.",
    "2025-07-01 13:25:33 - ERROR - Database connection failure on 'db-server-02'."
]

df = pd.DataFrame(incident_logs, columns=["log_message"])

# =========================
# Extract Information
# =========================

def extract_info(log):

    doc = nlp(log)

    date_time = log.split(" - ")[0]
    parts = log.split(" - ")

    incident_type = parts[1] if len(parts) > 1 else "UNKNOWN"

    server = None
    for word in log.split():
        if "server" in word:
            server = word.replace("'", "").replace(",", "")

    issue = parts[2] if len(parts) > 2 else ""

    return date_time, incident_type, server, issue

df[['date_time', 'incident_type', 'server', 'issue_description']] = df['log_message'].apply(
    lambda x: pd.Series(extract_info(x))
)

# =========================
# Categorization
# =========================

def categorize(issue):

    issue = issue.lower()

    if "security" in issue or "unauthorized" in issue:
        return "Security"

    elif "cpu" in issue or "memory" in issue:
        return "Performance"

    elif "database" in issue:
        return "System"

    else:
        return "General"

df["incident_category"] = df["issue_description"].apply(categorize)

print("\n=== INCIDENT REPORT TABLE ===\n")
print(df)

# =========================
# Save Output
# =========================

df.to_csv("incident_report.csv", index=False)

# =========================
# Visualization
# =========================

counts = df["incident_category"].value_counts()

plt.figure(figsize=(8, 6))
counts.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Incident Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("incident_category_distribution.png")

print("\nFiles generated:")
print("- incident_report.csv")
print("- incident_category_distribution.png")
