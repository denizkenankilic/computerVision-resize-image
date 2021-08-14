# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 21:49:21 2021

@author: deniz.kilic
"""

from PIL import Image
import os

images_path = r'images'
resized_images_path = r'resized_images'

if not os.path.exists(resized_images_path):
    os.makedirs(resized_images_path)

dirs = os.listdir(images_path)

def resize(images_path, resized_images_path, image_format):
    for item in dirs:
        if os.path.isfile(images_path+ '\\' + item):
            im = Image.open(images_path + '\\' + item)
            f, e = os.path.splitext(item)
            imResize = im.resize((512,512), Image.ANTIALIAS)
            if image_format == "jpeg":
                imResize.save(resized_images_path + '\\' + item + ' _resized.jpg', 'JPEG')
            elif image_format == "bmp":
                imResize.save(resized_images_path + '\\' + item + ' _resized.bmp')
            elif image_format == "tiff":
                imResize.save(resized_images_path + '\\' + item + ' _resized.tif')
            elif image_format == "png":
                imResize.save(resized_images_path + '\\' + item + ' _resized.png')
resize(images_path, resized_images_path, image_format)
