FROM python:3

WORKDIR /usr/src 

RUN git clone https://github.com/joaoventura/flask-static-site.git

COPY . /usr/src 

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# run the command
CMD ["python", "flask-static-site/site.py"]
