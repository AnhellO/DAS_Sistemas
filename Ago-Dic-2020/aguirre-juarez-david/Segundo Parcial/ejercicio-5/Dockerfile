FROM python:3

RUN pip install psycopg2
RUN pip install peewee

COPY ./data/ .

CMD ["python", "transfer.py"]