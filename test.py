import time, json
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd 
from json import loads as toDict
from zoomus import ZoomClient

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()

ZOOM_KEY = 'kmf79qbLTSWBDBYEYT-OmA'
ZOOM_SECRET = 'nnTZNHB1d5edjvLoxGjDGvls8JJIhcAfjP2V'

client = ZoomClient(ZOOM_KEY, ZOOM_SECRET)


user_list_response = client.user.list()
user_list = json.loads(user_list_response.content)

zoom_meeting = None
for user in user_list['users']:
    user_id = user['id']
    #print(json.loads(client.meeting.list(user_id=user_id).content))



zoom_meeting = client.meeting.create(topic="Meeting", type=2, duration=30, user_id=user_id, agenda="", host_id = user_id, settings={'join_before_host': True})
t = ((zoom_meeting.json()))
print(t)