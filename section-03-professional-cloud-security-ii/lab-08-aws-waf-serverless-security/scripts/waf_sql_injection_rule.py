import re

# Simulated AWS WAF SQL Injection Detection Rule

sql_injection_pattern = r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|--)\b|\b(UNION|OR|AND)\b.*\b(SELECT|FROM|WHERE)\b)"

def check_sql_injection(request):
    if re.search(sql_injection_pattern, request, re.IGNORECASE):
        return True
    return False

# Example request
request_data = "username=admin' OR 1=1 --"

print("Checking request:")
print(request_data)
print()

if check_sql_injection(request_data):
    print("SQL Injection detected! Blocking request.")
else:
    print("Request is clean.")
