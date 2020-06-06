# How to Get Started with Docker

En esta charla pudimos ver lo esenciales que son en el mundo del desarrollo los contenedores.
Aprendimos como instalar docker, construir nuestras primeras imagenes, ejecutar las imagenes
que creamos localmente, y vimos un poco sobre como conectar contenedores utilizando la red Docker.

Cada contenedor Docker es una "Instancia" de una imagen docker. Podemos tener acceso a una gran 
biblioteca de imagenes docker preconstruidas en dockerhub. Sin embargo, para comprender un poco 
mejor docker creamos una imagen como ejercicio. Necesitamos de un dockerfile el cual es un archivo 
de texto que contiene una serie de instrucciones necesarias para la creacion de la imagen. 
#### Descarga la imagen de Ubuntu 16.04
FROM ubuntu:16.04

#### Actualiza la imagen base de Ubuntu 16.04
RUN apt-get update

#### Ejecuta el commando apt-get install y elimina determinados archivos y temporales
RUN apt-get install -y nginx \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#### Indica los puertos TCP/IP los cuales se pueden accede a los servicios del contenedor
EXPOSE 80

##### Establece el commando del proceso de inicio del contenedor
CMD [“nginx”]



### Acquired knowledge
- How to install docker
- Create my own Image 
- Run my own image locally
- Docker Compose
- How to run docker compose file 
