FROM ubuntu:latest

WORKDIR /todoapp


RUN apt -y update
RUN apt -y install curl
RUN apt -y install mariadb-server python python3-pip

COPY . .

RUN python3 -m pip install -r requirements.txt
