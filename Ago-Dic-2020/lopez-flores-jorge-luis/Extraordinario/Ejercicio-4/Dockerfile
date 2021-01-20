FROM python:3

WORKDIR /home/anonymous/app

COPY server.py .

RUN pip install flask
RUN pip install faker

CMD [ "python", "server.py" ]