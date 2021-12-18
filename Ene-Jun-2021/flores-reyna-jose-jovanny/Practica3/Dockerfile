#Que extienda de la imágen base de Python3
FROM python:3

#Que utilice el directorio /usr/src como el directorio de trabajo
COPY . /usr/src

WORKDIR /usr/src

#Que clone el siguiente repositorio: https://github.com/joaoventura/flask-static-site
RUN git clone https://github.com/joaoventura/flask-static-site.git

#Que instale todas las dependencias necesarias especificadas en el archivo de requirements.txt por medio de pip
RUN pip install --no-cache-dir -r requeriments.txt

#Ten en cuenta que los contenedores creados en base a esta imágen deben de ser accesibles desde el exterior 
EXPOSE 3000

# finalmente que ejecute el script site.py, justo como se especifíca en el README del repositorio
CMD [ "python3", "./site.py"]





