FROM  python:3 AS firststage
LABEL maintainer="juan.arnoldo.munoz@hotmail.com"
RUN apt-get update; apt-get install -y mongodb-org
RUN pip install pymongo
WORKDIR /practica_6_docker
ADD populate.py .
ADD find.py .

FROM thinkcube/phpmoadmin:latest AS secondstage
LABEL maintainer="juan.arnoldo.munoz@hotmail.com"
WORKDIR /practica_6_docker
EXPOSE 8080
