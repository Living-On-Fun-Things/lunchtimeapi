from flask import Flask
from flask import request, jsonify
import json
from json import loads
from flask_cors import CORS
import boto3
from boto3.dynamodb.conditions import Key, Attr

ZOOM_KEY = ''
ZOOM_SECRET = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
REGION_NAME = ''


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
    print(time)
    dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME,aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key= AWS_SECRET_ACCESS_KEY)
    table = dynamodb.Table('lunchtimeio_community_meetings')
    response = table.query(KeyConditionExpression=Key('timeslots').eq(str(time)))

    data = {'response': response['Items'][0]['zoomlink']}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
