FROM python:3

WORKDIR /usr/src/app

COPY . /usr/src/app 

RUN pip install --no-cache-dir -r requirements.txt

VOLUME [ "redis_volume:/data" ]

CMD ["python", "./app.py"]