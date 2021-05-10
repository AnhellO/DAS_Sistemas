FROM python:3

COPY . /usr/src

WORKDIR /usr/src

RUN git clone https://github.com/joaoventura/flask-static-site.git

RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 8000

CMD [ "python3", "./flask-static-site/site.py"]





