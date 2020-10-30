FROM mongo

RUN apt-get update && apt-get update

RUN apt-get install python3.7

RUN apt install python3-pip

RUN pip3 install pymongo

WORKDIR /root

RUN mkdir mongo_app

ADD find.py /root/mongo_app

ADD populate.py /root/mongo_app

RUN cd mongo_app/

RUN python3 populate.py

RUN python3 find.py

EXPOSE 27017