import cv2
from pyzbar.pyzbar import decode
import numpy as np
from whatsapp_request import downloadMedia


def process_image(message_body):
    message  = message_body['message']

    raw = downloadMedia(message['image']['id']).content
    image = np.asarray(bytearray(raw), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    barcodes = decode(image)
  
    for barcode in barcodes:
        print(f'barcode detected {barcode.data}')

