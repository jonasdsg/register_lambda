import cv2
from pyzbar.pyzbar import decode
import numpy as np
from whatsapp_request import downloadMedia
from item_register import register


def process_image(message_body):
    customer_id = message_body['customer']['customer_id']
    message  = message_body['message']

    raw = downloadMedia(message['image']['id']).content
    image = np.asarray(bytearray(raw), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    barcodes = decode(image)
  
    for barcode in barcodes:
        print(f'registrando item {barcode.data} cid {customer_id}')
        register(barcode.data,customer_id)


