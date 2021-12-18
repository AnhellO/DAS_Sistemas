FROM python:3.9
WORKDIR /app

COPY requirements.txt /app/
COPY info.py /app/
COPY mock_data.json /app/

RUN pip install -r requirements.txt

RUN python /app.py
CMD ["python", "./app.py"]