# used the python:3.7-slim-buster image. The slim variant reduces the overall image size by about 700mb. 
# The alpine variant does not work with tensorflow
# I also chose to downloaded the machine learning model in the Dockerfile 
# so it’ll be cached in the Docker image.
# Otherwise the model will be downloaded at the point of running the model server.
# This is not an issue aside from adding a few minutes delay to the replication process 
# (as each worker that starts up needs to first download the model).
# Once again, the Dockerfile installs the requirements and then runs the main.py file.
FROM python:3.7-slim-buster

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

# Download ResNet50 model and cache in image
RUN python -c "from keras.applications import ResNet50; ResNet50(weights='imagenet')"

COPY . /app

CMD ["python", "/app/main.py"]
