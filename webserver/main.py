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
# Called to all images we receive so they match a specific format for our model
def prepare_image(image, target):
    """Resize image to desired target(height and width) and pre-process it.
       image here is a PIL Image Instance thus has all the methods of a PIL Image Instance 
    """
    # If the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # Resize the input image and preprocess it
    image = image.resize(target) # resize to some height and width
    image = img_to_array(image) # Converts a PIL Image instance to a Numpy array.
    image = np.expand_dims(image, axis=0) # Insert a new axis that will appear at the axis position in the expanded array shape.
    #Pre-processing an image means changing the pixel values from 0 to 255 to some range 
    #e.g -1 to 1
    # Here, we use the range that imagenet uses
    image = imagenet_utils.preprocess_input(image)

    # Return the processed image
    return image


# create our home route
@app.get('/')
def index():
    return "Hello world"

#------------------predict route--------------------
@app.post('/predict')
def predict(request: Request, img_file: bytes=File(...)):
    data = {"success":False} # create a new dict called data to be returned

    #we then ensure that an image was properly uploaded to the endpoint
    if request.method == "POST":
        # data can be kept as bytes in an in-memory buffer when we use the io module’s Byte IO operations.
        image = Image.open(io.BytesIO(img_file))
        # send the image to be prepared
        #notice that the width and height come from the system variables
        image_width = int(os.environ.get("IMAGE_WIDTH"))
        image_height = int(os.environ.get("IMAGE_HEIGHT"))
        image = prepare_image(image, (image_width, image_height))
        # image is now a numpy array
        # we need to ensure it is C-contigious otherwise we cannot serialize it.
        # contigious is explained in the readme
        image = image.copy(order="C")
