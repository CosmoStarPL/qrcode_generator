from pyzbar.pyzbar import decode
from PIL import Image


def qr_code_read(image_path):
    image = Image.open(image_path)
    decoded_objects = decode(image)
    return [obj.data.decode('utf-8') for obj in decoded_objects]
