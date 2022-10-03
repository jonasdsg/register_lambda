import json
from image_processor import process_image


def handler(event,context):
    for record in event['Records']:
        message_body = json.loads(record['body'])
        process_image(message_body)
