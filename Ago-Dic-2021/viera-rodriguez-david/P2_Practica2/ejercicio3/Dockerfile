FROM python:3.8

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
COPY insertar.py /usr/src/app
COPY mock_data.json /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./insertar.py"]