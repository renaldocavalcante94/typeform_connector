FROM ubuntu:latest as development
COPY . /home/app
RUN apt-get update && apt-get -y install python3 python3-pip 
RUN pip3 install fastapi requests uvicorn
WORKDIR /home/app

FROM ubuntu:latest as production
COPY . /home/app
RUN apt-get update && apt-get -y install python3 python3-pip
RUN pip3 install fastapi requests uvicorn
WORKDIR /home/app

