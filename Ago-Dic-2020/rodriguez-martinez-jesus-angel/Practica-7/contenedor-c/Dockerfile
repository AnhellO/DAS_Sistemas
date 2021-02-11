FROM python:3
ADD . /flask
WORKDIR /flask
RUN pip install -r requirements.txt
CMD ["sleep", "30"]
CMD ["python3", "app.py"]