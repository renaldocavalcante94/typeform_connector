FROM ubuntu:latest as development
CMD bash
RUN apt-get update && apt-get -y install python3 python3-pip 
RUN pip3 install fastapi requests
WORKDIR /home/app

FROM ubuntu:latest as production
COPY . /home/app
RUN apt-get update && apt-get -y install python3 python3-pip
RUN pip3 install fastapi requests
WORKDIR /home/app

