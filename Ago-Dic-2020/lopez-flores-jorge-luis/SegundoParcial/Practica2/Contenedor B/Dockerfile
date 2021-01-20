FROM python:3

LABEL maintainer="DanielSalazar"

RUN pip3 install pymongo
RUN pip3 install requests

COPY fetch.py .

ENTRYPOINT ["python3","fetch.py"]