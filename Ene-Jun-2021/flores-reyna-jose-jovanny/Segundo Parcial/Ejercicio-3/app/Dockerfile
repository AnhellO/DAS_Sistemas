#Que extienda de la imágen base de Python3
FROM python:3

#Que utilice el directorio /app como el directorio de trabajo
COPY . /app

WORKDIR /app

#Que instale todas las dependencias necesarias por medio de pip
RUN pip install --no-cache-dir -r requeriments.txt

#Que monte el volumen redis_volume
$ docker run -d \
  --name devtest \
  --mount source=redis_volume,target=/app \
  nginx:latest


EXPOSE 3000


CMD [ "python3", "./app.py"]
