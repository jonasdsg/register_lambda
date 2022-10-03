import requests
import os

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
BASE_URL ='https://graph.facebook.com/v15.0'
headers = {"Content-Type": "application/json; charset=utf-8","Authorization":AUTH_TOKEN}

def sendMessage(from_number, to_number, message):
    url = f'{BASE_URL}/{from_number}/messages'
    
    send={
            'messaging_product': 'whatsapp',
            'recipient_type': 'individual',
            'to': to_number,
            'type': 'text',
            'text': {
                'preview_url': 'false',
                'body': message
            }
    }
    
    print(f'enviando mensagem de {from_number} para {to_number}')
    requests.post(url, headers=headers,json=send)
    

def downloadMedia(mediaId):
    url = f'{BASE_URL}/{mediaId}'
    media_info_response = requests.get(url, headers=headers)
    if media_info_response.status_code == 200:
        media_body = media_info_response.json()
        media_content = requests.get(media_body['url'],headers=headers)
        if media_content.status_code == 200:
            return media_content
        
    raise Exception(f'erro ao requisitar informacoes do arquivo, status {media_info_response.status_code} response {media_info_response.json()}')
        