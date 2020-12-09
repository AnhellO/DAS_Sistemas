FROM python:3

WORKDIR /home/anonymous/app

COPY server.py .

RUN pip install Flask
RUN pip install Faker

EXPOSE 8000

# command to run on container start
CMD [ "python", "./server.py" ]