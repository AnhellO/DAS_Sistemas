FROM python:3

RUN pip install pymongo
RUN pip install Flask

COPY . .

ENTRYPOINT flask run --host 0.0.0.0