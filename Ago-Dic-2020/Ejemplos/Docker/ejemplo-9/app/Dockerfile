FROM python:3

WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

ADD . /usr/src/app

EXPOSE 5000

RUN export FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]