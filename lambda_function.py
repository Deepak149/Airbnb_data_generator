import json
import boto3
import random
from datetime import datetime, timedelta

sqs_client = boto3.client('sqs')

QUEUE_URL = 'https://sqs.us-west-1.amazonaws.com/533267281198/aws-de-sq'

def generate_booking_data():
    start_date = datetime.now() + timedelta(days=random.randint(1, 30)) 
    end_date = start_date + timedelta(days=random.randint(1, 5)) 
    return {
        "booking_id": random.randint(1000, 9999),
        "user_id": random.randint(100, 999),
        "startDate": start_date.strftime("%Y-%m-%d"),
        "endDate": end_date.strftime("%Y-%m-%d"),
        "price" : random.randint(10000, 99999)
    }
    
def lambda_handler(event, context):
    i=0
    while(i<1):
        sales_order = generate_booking_data()
        print(sales_order)
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(sales_order)
        )
        i += 1