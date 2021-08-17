from io import BytesIO
from PIL import Image, ImageOps 
from jishaku.functools import executor_function

@executor_function 
def invert(image_bytes):
    with Image.open(BytesIO(image_bytes)) as image:
        buffer = BytesIO()
        inverted_image = ImageOps.invert(image.convert('RGB'))
        inverted_image.save(buffer, 'png')
        buffer.seek(0)
        return buffer