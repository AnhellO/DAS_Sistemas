FROM mongo

MAINTAINER JAGC

RUN apt-get update && apt-get update

RUN apt-get install python3.7 -y

RUN apt install python3-pip -y

RUN pip3 install pymongo

WORKDIR /root

RUN mkdir mongo_app

ADD find.py /root/mongo_app

ADD populate.py /root/mongo_app

RUN service mongodb start -y

RUN python3 /root/mongo_app/populate.py

RUN python3 /root/mongo_app/find.py

EXPOSE 27017