FROM python:3
WORKDIR /usr/src/
RUN git clone https://github.com/joaoventura/flask-static-site.git
WORKDIR flask-static-site
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "site.py" ]