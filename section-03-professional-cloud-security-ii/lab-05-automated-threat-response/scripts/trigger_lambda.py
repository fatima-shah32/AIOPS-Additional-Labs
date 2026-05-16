from lambda_response import lambda_handler

cloudwatch_event = {
    "alarmName": "HighCPUUsageAlarm",
    "trigger": {
        "metricName": "CPUUtilization",
        "threshold": 80,
        "currentValue": 90
    },
    "state": "ALARM"
}

print("Simulating CloudWatch alarm...")

response = lambda_handler(cloudwatch_event, None)

print("\nLambda function response:")
print(response)
