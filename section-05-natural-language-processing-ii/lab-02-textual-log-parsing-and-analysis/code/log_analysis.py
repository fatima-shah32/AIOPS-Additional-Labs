import matplotlib
matplotlib.use('Agg')
import re
import matplotlib.pyplot as plt
from collections import Counter

# Read log file
with open("../datasets/system_logs.txt", "r") as file:
    logs = file.read()

# Regex pattern
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), (\w+),.*User '(\w+)' .*from IP (\d+\.\d+\.\d+\.\d+)"

# Extract data
log_data = re.findall(pattern, logs)

# Store entries
log_entries = [
    (timestamp, log_level, user, ip)
    for timestamp, log_level, user, ip in log_data
]

print("\nExtracted Log Entries:\n")

for entry in log_entries:
    print(entry)

# -----------------------------
# Visualization 1
# Log Level Distribution
# -----------------------------

log_levels = [log[1] for log in log_entries]

plt.figure(figsize=(8, 6))
plt.hist(log_levels, bins=len(set(log_levels)))

plt.title("Log Level Distribution")
plt.xlabel("Log Level")
plt.ylabel("Frequency")

plt.savefig("../reports/log_level_distribution.png")

print("\nSaved: log_level_distribution.png")

# -----------------------------
# Visualization 2
# User Activity by IP
# -----------------------------

user_ip_mapping = [(log[2], log[3]) for log in log_entries]

user_ip_count = Counter(user_ip_mapping)

users, ip_counts = zip(*user_ip_count.items())

user_ip_pairs = [
    f"{user} - {ip}"
    for user, ip in users
]

plt.figure(figsize=(10, 6))

plt.barh(user_ip_pairs, ip_counts)

plt.title("User Activity by IP")
plt.xlabel("Number of Events")
plt.ylabel("User - IP Pair")

plt.savefig("../reports/user_activity_by_ip.png")

print("Saved: user_activity_by_ip.png")

# -----------------------------
# Failed Login Detection
# -----------------------------

failed_login_pattern = r"failed to login"

failed_logins = re.findall(failed_login_pattern, logs)

print(f"\nFailed login attempts: {len(failed_logins)}")
