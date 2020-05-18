FROM python:3

COPY . /usr/src/Script

WORKDIR /usr/src/Script

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./fake.py"]