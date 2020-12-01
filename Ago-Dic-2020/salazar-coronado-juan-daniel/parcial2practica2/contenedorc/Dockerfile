FROM python:3

LABEL maintainer="DanielSalazar"

RUN pip3 install pymongo
RUN pip3 install flask

COPY . .

ENTRYPOINT flask run --host 0.0.0.0