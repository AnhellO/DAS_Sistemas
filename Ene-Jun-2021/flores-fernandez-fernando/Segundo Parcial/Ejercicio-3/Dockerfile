FROM python:3

COPY . usr/src/app

WORKDIR usr/src/app

ADD ejercicio-3.py .

VOLUME [redis_volume]

RUN pip install redis 

CMD [ "python", "./ejercicio-3.py" ]


