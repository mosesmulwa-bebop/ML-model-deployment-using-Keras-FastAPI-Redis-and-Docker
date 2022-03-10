#The tiangolo/uvicorn-gunicorn-fastapi image is used for the web server.
#This Docker image provides a neat ASGI stack (Uvicorn managed by Gunicorn with FastAPI framework) 

#This docker file copies the abpve image, installs the necessary Python requirements 
#and copies the code into the container.
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app