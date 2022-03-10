# Details

This repo covers deployment of an image classification model(ResNet50) using FastAPI, Redis and Docker.<br>


For in-depth Residual Networks: [Residual Networks](https://github.com/mosesmulwa-bebop/Residual-Network-for-Digit-Recognition) <br>

For a more detailed FastAPI project: [FastAPI social media backend](https://github.com/mosesmulwa-bebop/Python-Api-Development)<br>

This repo is based of this article: [Medium Article](https://medium.com/analytics-vidhya/deploy-machine-learning-models-with-keras-fastapi-redis-and-docker-4940df614ece)<br>

## Overview
1. Building a web server using FastAPI (with Uvicorn) to serve as a machine learning endpoint. <br>
2. Building a machine learning model server that serves a Keras image classification model (ResNet50 trained on ImageNet). <br>
3. Using Redis as a message queue to pass queries and responses between the web server and model server. <br>
4. Using Docker Compose to spin them all up! <br>

## Contents
1. [Why FastAPI](https://github.com/mosesmulwa-bebop/ML-model-deployment-using-Keras-FastAPI-Redis-and-Docker#why-fastapi) <br>


## 	How it works
The main function of the web server is to serve a /predict endpoint through which other applications will call our machine learning model. <br>
When the endpoint is called, the web server routes the request to the Redis, which acts as an in-memory message queue for many concurrent requests. <br>
The model server simply polls the Redis message queue for a batch of images, classifies the batch of images, then returns the results to Redis. The web server picks up the results and returns that.<br>

##  Why FastAPI
FastAPI uses an ASGI(Asynchronous Server Gateway Interface) which means that requests are handled asynchronously. This means that they don't have to wait for others before them to finish doing their tasks.<br>

