
# Practica 3
# Que extienda de la imágen base de Python3
FROM python:3

# Copie el contenido del directorio actual en el contenedor en / app
COPY . /usr/src

# Que utilice el directorio /usr/src como el directorio de trabajo
WORKDIR /usr/src

# Que clone el siguiente repositorio: https://github.com/joaoventura/flask-static-site
RUN git clone https://github.com/joaoventura/flask-static-site 

# Que instale todas las dependencias necesarias especificadas en el archivo de requirements.txt por medio de pip
RUN pip install --no-cache-dir -r requirements.txt

# Poner el puerto 8000 a disposición del mundo fuera de este contenedor
EXPOSE 5000

# Y finalmente que ejecute el script site.py, justo como se especifíca en el README del repositorio
CMD ["python", "./site.py"]
