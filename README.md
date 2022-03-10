# Details

This repo covers deployment of an image classification model(ResNet50) using FastAPI, Redis and Docker.<br>


For in-depth Residual Networks: https://github.com/mosesmulwa-bebop/Residual-Network-for-Digit-Recognition <br>

For a more detailed FastAPI project: https://github.com/mosesmulwa-bebop/Python-Api-Development <br>

## Overview
1. Building a web server using FastAPI (with Uvicorn) to serve as a machine learning endpoint. <br>
2. Building a machine learning model server that serves a Keras image classification model (ResNet50 trained on ImageNet). <br>
3. Using Redis as a message queue to pass queries and responses between the web server and model server. <br>
4. Using Docker Compose to spin them all up! <br>
