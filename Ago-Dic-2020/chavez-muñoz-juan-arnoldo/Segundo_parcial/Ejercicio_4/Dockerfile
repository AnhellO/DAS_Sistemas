FROM python:3.7-alpine

LABEL maintainer="juan.arnoldo.munoz@hotmail.com"

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN git clone https://github.com/joaoventura/flask-static-site usr/src

COPY . /usr/src

WORKDIR /usr/src

RUN pip install -r requirements.txt

EXPOSE 5000

RUN cd /usr/src

CMD ["site.py"]

ENTRYPOINT ["python3"]