FROM mongo:latest

LABEL maintainer="DanielSalazar"

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pymongo

WORKDIR /practicadockerfile

ADD populate.py /practicadockerfile
ADD find.py /practicadockerfile

EXPOSE 27017

CMD ["python3","populate.py"]