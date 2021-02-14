from flask import Flask
from flask import request
import json
from json import loads as toDict
from zoomus import ZoomClient

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
    

app = Flask(__name__)

'''

# initialize firestore instance
firestore_db = firestore.client()# add data

firestore_db.collection(u'meetings').add({'song': 'Imagine', 'artist': 'John Lennon'})# read data
snapshots = list(firestore_db.collection(u'songs').get())
for snapshot in snapshots:
    print(snapshot.to_dict())
'''

@app.route('/')
def status():
    return ''


@app.route('/health')
def health():
    return json.dumps({'status': 'ok'})


@app.route('/meeting', methods=['POST'])
def meeting():
    data = (request.data.decode())

    
    d = json.loads(json.dumps(data))
    print(d)
    
    client = ZoomClient('kmf79qbLTSWBDBYEYT-OmA', 'nnTZNHB1d5edjvLoxGjDGvls8JJIhcAfjP2V')

    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)

    for user in user_list['users']:
        user_id = user['id']
        print(json.loads(client.meeting.list(user_id=user_id).content))

        zoom_meeting = client.meeting.create(topic="Meeting", type=2, duration=30, user_id=user_id, agenda="", host_id = user_id)
        return str(zoom_meeting)

    return json.dumps({'status': 'ok'})

app.run()
