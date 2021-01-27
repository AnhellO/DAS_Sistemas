FROM python:3-onbuild

# RUN apt install python3-pip -y

RUN pip3 install pymongo

RUN pip3 install requests

RUN mkdir app

WORKDIR /root/app

COPY  fetch.py .

CMD ["python3", "fetch.py"]