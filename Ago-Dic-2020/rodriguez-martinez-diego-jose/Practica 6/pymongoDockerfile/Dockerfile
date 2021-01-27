###DOCKER FILE PARA CREAR IMAGEN DE MONGODB, CON PYTHON3, PIP3, Y PYMONGO DOCKERIZADOS


#Voy a crear la imagen del dockerfile con la imagen base de mongo:latest
FROM mongo:latest
LABEL "Correo:"=d.rdz.mtz314@gmail.com


### An~ado esta linea, me dice que no lo tiene
# RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

## Uso el comando de Run para correr estos comandos mientras se construye la imagen
# Instalo python3 y pip3, ademas de instalar pymongo con pip3  
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get -y install python3.7-dev
RUN pip3 install pymongo

#Creo el workdir del contenedor
WORKDIR /home/DAS_Sistemas/Ago-Dic-2020/rodriguez-martinez-diego-jose/Practica6/

#An~ado los scripts de python, estos los voy a correr despues dentro del contenedor con el script bash adjuntado
COPY find.py .
COPY populate.py .

#Abro el puerto 27017 en el contenedor
EXPOSE 27017