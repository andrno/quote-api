import json
import random

QUOTES = [
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Stay hungry, stay foolish.",
    "Action is the foundational key to all success."
]

def lambda_handler(event, context):
    name = event.get('queryStringParameters', {}).get('name', 'friend')
    quote = random.choice(QUOTES)
    return {
        'statusCode': 200,
        'body': json.dumps({ "message": f"Hi {name}, your quote is: '{quote}'" }),
        'headers': { "Content-Type": "application/json" }
    }