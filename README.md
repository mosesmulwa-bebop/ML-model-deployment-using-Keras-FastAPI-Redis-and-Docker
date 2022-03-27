# Details

This repo covers deployment of an image classification model(ResNet50) using FastAPI, Redis and Docker.<br>


For an in-depth project on Residual Networks: [Residual Networks](https://github.com/mosesmulwa-bebop/Residual-Network-for-Digit-Recognition) <br>

For a more detailed FastAPI project: [Using FastAPI to build a full-fledged social media backend](https://github.com/mosesmulwa-bebop/Python-Api-Development)<br>

This repo is based on this medium article: [Medium Article](https://medium.com/analytics-vidhya/deploy-machine-learning-models-with-keras-fastapi-redis-and-docker-4940df614ece)<br>

## Deployment
1. First docker-compose
```shell script
   docker-compose up
   ```
2. Test with sample image provided
```shell script
   curl -X POST img_file=@doge.jpg http://localhost/predict
   ```
The sample Image
![Doge](doge.jpg)

3. Response if everything run correctly.
##### Response (Code 200)

```json
{"success":true,
"predictions":[
    {"label":"dingo","probability":0.5237663984298706},
    {"label":"Pembroke","probability":0.178588405251503},
    {"label":"basenji","probability":0.1512373834848404},
    {"label":"Eskimo_dog","probability":0.03126605227589607},
    {"label":"bath_towel","probability":0.011432502418756485}]}
```


## Overview
1. Building a web server using FastAPI (with Uvicorn) to serve as a machine learning endpoint. <br>
2. Building a machine learning model server that serves a Keras image classification model (ResNet50 trained on ImageNet). <br>
3. Using Redis as a message queue to pass queries and responses between the web server and model server. <br>
4. Using Docker Compose to spin them all up! <br>

## 	How it works
The main function of the web server is to serve a /predict endpoint through which other applications will call our machine learning model. <br>
When the endpoint is called, the web server routes the request to the Redis, which acts as an in-memory message queue for many concurrent requests. <br>
The model server simply polls the Redis message queue for a batch of images, classifies the batch of images, then returns the results to Redis. The web server picks up the results and returns that.<br>

## Contents
1. [Included Files](https://github.com/mosesmulwa-bebop/ML-model-deployment-using-Keras-FastAPI-Redis-and-Docker#included-files) <br>
2. [Why FastAPI](https://github.com/mosesmulwa-bebop/ML-model-deployment-using-Keras-FastAPI-Redis-and-Docker#why-fastapi) <br>



## Included Files

### 1. Webserver
Contains code for the webserver built using FastAPI
<b>Dockerfile</b> - Docker file for copies the fastapi image and installing requirements.
<b>main.py</b> - runs the FastAPI server, exposing the/predict endpoint which takes the uploaded image, serializes it, pushes it to Redis and polls for the resulting predictions.
<b>requirements.txt</b>- contains all the requirements for the webserver.





##  Why FastAPI
FastAPI uses an ASGI(Asynchronous Server Gateway Interface) which means that requests are handled asynchronously. This means that they don't have to wait for others before them to finish doing their tasks.<br>
FastAPI is also a micro web framework with many advantages, including out-of-the-box support for asynchronous code using the Python async and await keywords, and much more.<br>

