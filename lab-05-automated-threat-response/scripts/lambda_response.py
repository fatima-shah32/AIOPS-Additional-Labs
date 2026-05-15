import json

def lambda_handler(event, context):
    print("Lambda function triggered by event:")
    print(json.dumps(event, indent=4))

    response = "Security event received, taking automated action!"

    return response
