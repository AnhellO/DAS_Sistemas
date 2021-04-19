FROM python:3.8

ADD rand.py .

RUN pip install random2 pymongo redis

EXPOSE 2308

CMD [ "python", "./rand.py" ]

