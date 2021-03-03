from flask import Flask
from flask import request, jsonify
import json
from json import loads
from flask_cors import CORS
import boto3
from boto3.dynamodb.conditions import Key, Attr

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
    dynamodb = boto3.resource('dynamodb', region_name="eu-west-1",aws_access_key_id="AKIAVHIWAVD7RSBS7U5Q", aws_secret_access_key= "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")
    table = dynamodb.Table('lunchtimeio_community_meetings')
    response = table.query(KeyConditionExpression=Key('timeslots').eq(str(time)))

    data = {'response': response['Items'][0]['zoomlink']}
    print(jsonify(data))
    return jsonify(data)


if __name__ == '__main__':
    app.run()
