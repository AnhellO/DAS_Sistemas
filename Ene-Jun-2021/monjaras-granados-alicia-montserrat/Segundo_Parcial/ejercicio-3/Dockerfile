# Imagen
FROM python:3

#  directorio de trabajo es desde donde se ejecuta el contenedor al iniciarse
WORKDIR /app

# Agrega los scripts de python, para que la aplicación se ejecute 
COPY . /app

# Instalar Dependencias
RUN pip install --no-cache-dir -r requirements.txt 

# especificación de volúmen
VOLUME ["./data"]


# Corre el comando
CMD ["python3", "./app.py"]