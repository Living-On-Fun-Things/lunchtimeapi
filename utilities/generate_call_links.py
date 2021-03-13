import time, json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd 
from json import loads as toDict
from zoomus import ZoomClient

ZOOM_KEY = ''
ZOOM_SECRET = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
REGION_NAME = ''

dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key= AWS_SECRET_ACCESS_KEY)
table = dynamodb.Table('lunchtimeio_community_meetings')



def create_zoom_calls():
    while true:
        date = pd.Timestamp.now() 
        hour = date.hour 
        print("Hour: ", hour) 

            
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

            zoom_meeting = client.meeting.create(topic="Meeting", type=2, duration=30, user_id=user_id, agenda="", host_id = user_id, settings={'host_video': False, 'participant_video': True, 'join_before_host': True, 'waiting_room': False, 'jbh_time': 0})
            t = ((zoom_meeting.json()))

            table.update_item(Key={'timeslots': str(hour)}, UpdateExpression="set zoomlink=:r", ExpressionAttributeValues={':r': str(t['join_url'])}, ReturnValues="UPDATED_NEW")
            print('Updated with zoomlink')

            for x in range(0,24):
                if x != hour:
                    table.update_item(Key={'timeslots': str(x)}, UpdateExpression="set zoomlink=:r", ExpressionAttributeValues={':r': 'WAIT'}, ReturnValues="UPDATED_NEW")

            print('Finished writing')


if __name__ == '__main__':
    create_zoom_calls()