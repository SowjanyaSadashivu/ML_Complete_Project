#from python version on linux base image of linux env
FROM python:3.8-slim-buster 
#this is my current working directory
WORKDIR /app
#copy . everything from current working directory to /app folder 
COPY . /app 
#run the following command, update all packages before deploying
RUN apt update -y && apt install awscli -y
#install all the dependencies
RUN pip install -r requirements.txt
# list of command to be 
CMD ["python3", "app.py"]
