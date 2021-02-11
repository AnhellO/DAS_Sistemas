FROM  python:3

LABEL maintainer="juan.arnoldo.munoz@hotmail.com"

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "fetch.py"] 