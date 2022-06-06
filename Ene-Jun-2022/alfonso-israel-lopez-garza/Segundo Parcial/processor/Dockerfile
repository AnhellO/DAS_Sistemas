FROM python:3

# Copia el contenido del directorio actual en el contenedor en /app
COPY . /usr/src/app

# Set el working directory a /usr/src/app
WORKDIR /usr/src/app

# Install todas las librerias/paquetes dentro de  requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Corre el comando
CMD ["python", "./Issues.py"]