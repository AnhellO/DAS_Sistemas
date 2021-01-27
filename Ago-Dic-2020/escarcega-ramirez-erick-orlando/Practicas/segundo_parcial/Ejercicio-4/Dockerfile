FROM python:3
MAINTAINER ERORESRA
WORKDIR /usr/src
RUN git clone https://github.com/joaoventura/flask-static-site.git
RUN pip3 install -r ./flask-static-site/requirements.txt
CMD [“python3 " "./flask-static-site/site.py”]
EXPOSE 8000