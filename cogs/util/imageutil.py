from io import BytesIO
from PIL import Image, ImageOps, ImageFilter
from jishaku.functools import executor_function

@executor_function 
def invert(image_bytes):
    with Image.open(BytesIO(image_bytes)) as image:
        buffer = BytesIO()
        inverted_image = ImageOps.invert(image.convert('RGB'))
        inverted_image.save(buffer, 'png')
        buffer.seek(0)
        return buffer

@executor_function 
def rotate(image_bytes, degrees):
    with Image.open(BytesIO(image_bytes)) as image:
        buffer = BytesIO()
        rotated_image = image.rotate(degrees)
        rotated_image.save(buffer, 'png')
        buffer.seek(0)
        return buffer

@executor_function 
def filter(image_bytes):
    with Image.open(BytesIO(image_bytes)) as image:
        buffer = BytesIO()
        filtered_image = image.filter(ImageFilter.DETAIL)
        filtered_image.save(buffer, 'png')
        buffer.seek(0)
        return buffer