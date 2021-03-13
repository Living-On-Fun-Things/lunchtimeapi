import time, json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd 
from json import loads as toDict


ZOOM_KEY = ''
ZOOM_SECRET = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
REGION_NAME = ''

dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME,aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key= AWS_SECRET_ACCESS_KEY)
table = dynamodb.Table('lunchtimeio_community_counter')

def create_zoom_calls():
    for hour in range(0,24):

        print("Hour: ", hour) 
        table.update_item(Key={'timeslot': str(hour)}, UpdateExpression="set interest=:r", ExpressionAttributeValues={':r': 0}, ReturnValues="UPDATED_NEW")


if __name__ == '__main__':
    create_zoom_calls()
