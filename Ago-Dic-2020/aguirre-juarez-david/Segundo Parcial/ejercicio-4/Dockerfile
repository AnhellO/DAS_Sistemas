FROM python:3

WORKDIR /usr/src

RUN git clone https://github.com/joaoventura/flask-static-site .
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "site.py"]