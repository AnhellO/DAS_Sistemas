FROM python:3-onbuild

RUN pip3 install Psycopg2-binary

RUN pip3 install peewee

RUN mkdir app_files

WORKDIR /root/app_files

COPY data_extractor.py .

COPY db.py .

COPY env.list .

COPY models.py .

COPY settings.py .

COPY data.json .

# CMD ["python3", "data_extractor.py"]