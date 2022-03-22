"""
Model server script that polls Redis for images to classify
"""
import base64
import json
import os
import sys
import time

from keras.applications import ResNet50
from keras.applications import imagenet_utils
import numpy as np
import redis

# Connect to the redis server
db = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))

#Load the pre-trained Keras model trained on Imagenet
model = ResNet50(weights="imagenet")