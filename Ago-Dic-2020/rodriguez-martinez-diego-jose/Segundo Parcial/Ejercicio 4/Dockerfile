FROM python:latest
LABEL "Correo:"=d.rdz.mtz314@gmail.com

WORKDIR /usr/src

RUN git clone https://github.com/joaoventura/flask-static-site.git
RUN pip3 install -r ./flask-static-site/requirements.txt

EXPOSE 8000

CMD ["python3", "./flask-static-site/site.py"]