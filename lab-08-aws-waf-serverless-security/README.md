# Lab 8: AWS WAF for Serverless Application Security

## Objective
Simulate AWS WAF rules to detect and block SQL injection attacks against serverless applications.

---

## Tools Used
- Ubuntu Linux
- Python 3
- Regex pattern matching
- Simulated AWS WAF security rules

---

## Folder Structure

lab-08-aws-waf-serverless-security/
├── reports
├── screenshots
└── scripts

---

## Scripts

### waf_sql_injection_rule.py
Simulates AWS WAF SQL injection detection logic.

### simulate_attack.py
Simulates malicious and clean HTTP requests to test WAF behavior.

---

## Simulated Attacks

- SQL Injection using OR 1=1
- UNION SELECT SQL injection attack
- Clean login request

---

## Outcome

Successfully simulated:
- AWS WAF SQL injection filtering
- Attack detection
- Request blocking
- Secure request validation
