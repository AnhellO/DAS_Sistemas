FROM python:3

LABEL maintainer="DanielSalazar"

WORKDIR /usr/src

RUN git clone https://github.com/joaoventura/flask-static-site.git .
RUN pip3 install -r requirements.txt

CMD ["python3","site.py"]