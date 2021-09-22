
import os
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def compressImage(uploaded_image):
    # print("uploaded_imag", uploaded_image)
    # print("uploaded_image.content_type", uploaded_image.file.content_type)
    # print("FTYPE", FTYPE)
    image_temp = Image.open(uploaded_image)
    image_content_type = image_temp.get_format_mimetype()
    # print("image_content_type", image_content_type)
    FTYPE = image_content_type.split('/')[-1]
    image_name, image_extension = os.path.splitext(uploaded_image.path)
    image_extension = image_extension.lower()

    outputIoStream = BytesIO()
    image_temp.thumbnail((1600, 1600))
    image_temp.save(outputIoStream, format=FTYPE, quality=100)
    # print("image_temp", image_temp.size)
    outputIoStream.seek(0)
    uploaded_image = InMemoryUploadedFile(
        outputIoStream, 'ImageField', f"{image_name}.{image_extension}", image_content_type, sys.getsizeof(outputIoStream), None)
    return uploaded_image
