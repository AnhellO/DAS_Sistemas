FROM python:3

RUN pip install requests
RUN pip install pymongo

COPY ./fetch.py .

ENTRYPOINT ["python", "fetch.py"]