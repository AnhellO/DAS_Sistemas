FROM python:3.8

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install redis
VOLUME /redis_volume

CMD ["python", "./cnxredis.py"]

