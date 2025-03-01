# server/image_utils.py
from PIL import Image
import base64
from io import BytesIO

def decode_base64_image(base64_string: str) -> Image.Image:
    """
    Decodes a base64-encoded image string into a PIL Image.
    """
    image_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(image_data))
    return image

def encode_image(image_path: str) -> str:
    """
    Encodes an image to a base64 string.
    """
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        encoded_string = base64.b64encode(image_data).decode("utf-8")
    return encoded_string
