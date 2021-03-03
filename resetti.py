import time, json
import boto3
from boto3.dynamodb.conditions import Key, Attr

import pandas as pd 
from json import loads as toDict
from zoomus import ZoomClient

dynamodb = boto3.resource('dynamodb', region_name="eu-west-1",aws_access_key_id="AKIAVHIWAVD7RSBS7U5Q", aws_secret_access_key= "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")
table = dynamodb.Table('lunchtimeio_community_meetings')

ZOOM_KEY = 'kmf79qbLTSWBDBYEYT-OmA'
ZOOM_SECRET = 'nnTZNHB1d5edjvLoxGjDGvls8JJIhcAfjP2V'

def sleeper():
    while True:
        date = pd.Timestamp.now() 
        hour = date.hour 
        print("Hour: ", hour) 

        hour = 12

            
        response = table.query(KeyConditionExpression=Key('timeslots').eq(str(hour)))

        print(response)
        data = response['Items'][0]['zoomlink']

        print(data)
        if (data == 'WAIT'):

            client = ZoomClient(ZOOM_KEY, ZOOM_SECRET)
            user_list_response = client.user.list()
            user_list = json.loads(user_list_response.content)

            zoom_meeting = None
            for user in user_list['users']:
                user_id = user['id']

            zoom_meeting = client.meeting.create(topic="Meeting", type=2, duration=30, user_id=user_id, agenda="", host_id = user_id, settings={'join_before_host': True})
            t = ((zoom_meeting.json()))

            table.update_item(Key={'timeslots': str(hour)}, UpdateExpression="set zoomlink=:r", ExpressionAttributeValues={':r': str(t['join_url'])}, ReturnValues="UPDATED_NEW")
            print('Updated with zoomlink')

            for x in range(0,24):
                if x != hour:
                    table.update_item(Key={'timeslots': str(x)}, UpdateExpression="set zoomlink=:r", ExpressionAttributeValues={':r': 'WAIT'}, ReturnValues="UPDATED_NEW")

            print('Finished writing')

        print('Before: %s' % date)
        time.sleep(5)
        print('After: %s\n' % date)
 
 
try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()
