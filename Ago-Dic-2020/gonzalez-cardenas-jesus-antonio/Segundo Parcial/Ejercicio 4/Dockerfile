FROM python:3.7.0

WORKDIR /usr/src

RUN apt install git -y

RUN git clone https://github.com/joaoventura/flask-static-site

RUN pip3 install -r flask-static-site/requirements.txt

CMD [ "python3","flask-static-site/site.py"]