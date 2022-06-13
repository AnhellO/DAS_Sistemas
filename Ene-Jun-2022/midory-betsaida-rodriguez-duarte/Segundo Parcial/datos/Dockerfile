FROM python:3

#Copiando el contenido del directorio actual en el contenedor en /app
COPY . /usr/src/app

WORKDIR /usr/src/app

#Instalando librerias requeridas dentro del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Corrieda del comando
CMD [ "python", "datos.py" ]
