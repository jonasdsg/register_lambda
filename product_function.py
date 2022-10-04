import datetime      
import boto3
import uuid
from boto3.dynamodb.conditions import Key
import os

dynamodb = boto3.resource('dynamodb')

TABLE_ID   = os.getenv("TABLE_ID")
TABLE_NAME = os.getenv("TABLE_NAME")
TABLE_PART = os.getenv("TABLE_PART")
TABLE_INDX = os.getenv("TABLE_INDX")
TABLE_CIDD = os.getenv("TABLE_CIDD")

def find_item(code):
    try:
        
        table = dynamodb.Table(TABLE_NAME)
        data = table.query(
            IndexName= TABLE_INDX,
            KeyConditionExpression=Key(TABLE_PART).eq(code)
        )
        return data.get('Items')
    except Exception as e:
        print('error {}'.format(e))
        return None

def save_item(code,cid):
    try:
        table = dynamodb.Table(TABLE_NAME)
        ID = str(uuid.uuid4())
        item = {
            TABLE_ID  : ID,
            TABLE_PART: str(code),
            TABLE_CIDD:  str(cid),
            'enriched': False,
            'createdAt': str(datetime.datetime.now()),
        }
        
        table.put_item(Item=item)
        
        return [item]
        
    except Exception as e:
        print('error while saving item {}'.format(e))

def save(code,cid):
    data = find_item(code)
    if len(data):
        return data
    return save_item(code,cid)
        
        
        