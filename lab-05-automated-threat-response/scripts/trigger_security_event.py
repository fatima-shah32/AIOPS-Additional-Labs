import json
from lambda_response import lambda_handler

with open('security_event.json', 'r') as file:
    security_event = json.load(file)

print("Simulating security event...")

response = lambda_handler(security_event, None)

print("\nLambda function response to security event:")
print(response)
