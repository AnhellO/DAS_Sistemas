FROM python:3-onbuild

# RUN apt install python3-pip -y

RUN pip3 install pymongo

RUN pip3 install flask

RUN mkdir app

WORKDIR /root/app

# RUN mkdir static

# RUN mkdir templates

COPY static/ ./static

COPY templates/ ./templates

COPY view.py .

CMD ["python3", "view.py"]