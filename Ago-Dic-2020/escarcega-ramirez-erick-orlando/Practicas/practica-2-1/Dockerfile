FROM mongo:latest AS base
MAINTAINER ERORESRA
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pymongo
WORKDIR /root/practica
ADD populate.py .
ADD find.py .
EXPOSE 27017

FROM thinkcube/phpmoadmin:latest
MAINTAINER ERORESRA
WORKDIR /practica
EXPOSE 8080
