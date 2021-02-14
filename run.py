from flask import Flask
from flask import request, jsonify
import json
from json import loads as toDict
from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()


app = Flask(__name__)
CORS(app)

@app.route('/')
def status():
    return ''


@app.route('/health')
def get():
    data = {'status': 'ok'}
    return jsonify(data)


@app.route('/meeting', methods=['POST'])
def meeting():
    
    data = (request.data.decode())

    time = (json.loads(data)['time'])
    
    snapshots = (firestore_db.collection(u'meetings').document(str(time)).get())

    return snapshots.to_dict()


app.run()
