FROM python:3

WORKDIR /home/salguer/redis

COPY . /home/salguer/redis

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./inserts.py"]