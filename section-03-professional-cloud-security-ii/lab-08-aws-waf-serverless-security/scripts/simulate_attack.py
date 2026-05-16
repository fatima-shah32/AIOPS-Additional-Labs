import re

# Simulated AWS WAF SQL Injection Rule

sql_injection_pattern = r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|--)\b|\b(UNION|OR|AND)\b.*\b(SELECT|FROM|WHERE)\b)"

def check_sql_injection(request):
    if re.search(sql_injection_pattern, request, re.IGNORECASE):
        return True
    return False

# Simulated Requests

attack_1 = "username=admin' OR 1=1 --"
attack_2 = "username=admin UNION SELECT password FROM users WHERE user_id=1"
clean_request = "username=admin&password=securepassword"

requests = [attack_1, attack_2, clean_request]

print("=========================================")
print("Simulating AWS WAF Attack Detection")
print("=========================================")

for req in requests:
    print(f"\nChecking request: {req}")

    if check_sql_injection(req):
        print("SQL Injection detected! Blocking request.")
    else:
        print("Request is clean.")
