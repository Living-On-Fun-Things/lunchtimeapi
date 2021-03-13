from flask import Flask
from flask import request, jsonify
import json
from json import loads
from flask_cors import CORS
import boto3
from boto3.dynamodb.conditions import Key, Attr

app = Flask(__name__)
CORS(app)


ZOOM_KEY = ''
ZOOM_SECRET = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
REGION_NAME = ''

@app.route('/')
def status():
    return ''


@app.route('/health')
def get():
    data = {'status': 'ok'}
    return jsonify(data)

@app.route('/interest', methods=['GET'])
def getinterest():
    dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME,aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key= AWS_SECRET_ACCESS_KEY)
    table = dynamodb.Table('lunchtimeio_community_counter')

    response_array = []
    for i in range(0,24):
        response = table.query(KeyConditionExpression=Key('timeslot').eq(str(i)))
        data = response['Items'][0]['interest']
        response_array.append(int(data))


    return jsonify({'response': (response_array)})

@app.route('/counter', methods=['POST'])
def createinterest():
    data = (request.data.decode())
    time = (json.loads(data)['time'])
    print(time)
    dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME,aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key= AWS_SECRET_ACCESS_KEY)
    table = dynamodb.Table('lunchtimeio_community_counter')
    response = table.query(KeyConditionExpression=Key('timeslot').eq(str(time)))

    data = {'response': response['Items'][0]}
    count = (data['response']['interest'])
    table.update_item(Key={'timeslot': str(time)}, UpdateExpression="set interest=:r", ExpressionAttributeValues={':r': (int(count) + 1)}, ReturnValues="UPDATED_NEW")

    return jsonify({'response': '200'})


if __name__ == '__main__':
    app.run()
