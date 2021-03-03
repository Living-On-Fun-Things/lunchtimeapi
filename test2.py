import boto3
from boto3.dynamodb.conditions import Key, Attr
from flask import request, jsonify

dynamodb = boto3.resource('dynamodb', region_name="eu-west-1",aws_access_key_id="AKIAVHIWAVD7RSBS7U5Q", aws_secret_access_key= "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")
table = dynamodb.Table('lunchtimeio_community_meetings')
response = table.query(KeyConditionExpression=Key('timeslots').eq("12"))


data = {'response': response['Items'][0]['zoomlink']}
print(data)