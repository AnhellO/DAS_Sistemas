FROM python:3

WORKDIR /usr/src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt 

RUN git clone https://github.com/joaoventura/flask-static-site.git

EXPOSE 8000

CMD [ "python", "./flask-static-site/site.py" ]