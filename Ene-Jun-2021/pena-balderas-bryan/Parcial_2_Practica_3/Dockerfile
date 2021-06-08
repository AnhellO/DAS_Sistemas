
FROM ubuntu

WORKDIR /usr/src
RUN apt-get update        
RUN apt-get install -y git    
RUN cd /usr/src        
RUN git clone https://github.com/joaoventura/flask-static-site

FROM python:3.8
COPY requirements.txt /usr/src
WORKDIR /usr/src
RUN pip install --no-cache-dir -r requirements.txt

# run the command
CMD ["python", "/usr/src/flask-static-site/site.py"]