"""
Web server script that exposes endpoints and pushes images to Redis for classification by model server. Polls
Redis for response from model server.
Adapted from https://www.pyimagesearch.com/2018/02/05/deep-learning-production-keras-redis-flask-apache/


Good to know:
Serialization is the process of converting an object into a stream of bytes to store the object 
or transmit it to memory, a database, or a file. 
Its main purpose is to save the state of an object in order to be able to recreate it when needed.
The reverse process is called deserialization.
"""
import base64
import io
import json
import os
import time
import uuid

from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import numpy as np
from PIL import Image
import redis

from fastapi import FastAPI, File, HTTPException
from starlette.requests import Request


app = FastAPI()
db = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))

CLIENT_MAX_TRIES = int(os.environ.get("CLIENT_MAX_TRIES"))



# ---------------------------PREPARE IMAGE-------------------------------
def prepare_image(image, target):
    """Resize image to desired target(height and width) and pre-process it"""
    # If the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # Resize the input image and preprocess it
    image = image.resize(target) # resize to some height and width
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    #Pre-processing an image means changing the pixel values from 0 to 255 to some range 
    #e.g -1 to 1
    # Here, we use the range that imagenet uses
    image = imagenet_utils.preprocess_input(image)

    # Return the processed image
    return image
