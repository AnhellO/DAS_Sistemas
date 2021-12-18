FROM python:3.8

WORKDIR /usr/src/app

COPY . /usr/src/app

VOLUME ["/redis_volume"]

RUN pip install --no-cache-dir -r requirements.txt

# run the command
CMD ["python", "./insertions.py"]
