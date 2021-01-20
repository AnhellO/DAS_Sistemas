# Síntesis 1 - Conferencia "How to Get Started with Docker"

Esta conferencia trata sobre como empezar a usar docker, entre los temas que cubre están:

- ¿Qué son los contenedores y por qué no se deberían de importar?
- Instalar Docker.
- Escribir Dockerfiles y construir imágenes.
- Correr y mantener imágenes.
- Subir tus imágenes a la nube.

## Docker

Antes de los contenedores, instalar y configurar aplicaciones era complicado, ya que se tenía que juntar el código, binarios, configuraciones y dependendencias de la aplicación y con esto correrla manualmente. Gracias a Docker, esto se puede lograr de manera sencilla.

Docker hace que las aplicaciones/server sean efímeras.

Docker se enfoca en 3 pasos:
- Construir imágenes
- Enviar imágenes
- Correr Imágenes

## Escribir Dockerfiles y construir imágenes

Los Dockerfiles son usados para construir imágenes, prácticamente es una lista de comandos para el engine de Docker, que ejecutará para construir las imágenes. Los comandos que usa el ejemplo de la conferencia son:

- `FROM`: Indicas la imagen base que se va a usar, normalmente es una que ya trae parte de lo que se necesita.
- `WORKDIR`: Se le indica a docker cual va a ser el directorio de trabajo. Todos los comandos se ejecutarán en este directorio.
- `ENV`: Variable de ambiente, estas son accesadas por procesos dentro de la imagen.
- `COPY`: Copia un archivo del directorio a el directorio dentro de la imagen indicada.
- `RUN`: Este comando se utiliza para correr un comando dentro de la imagen.
- `CMD`: Esto se usa para indicar un comando que se ejecutará cuando se empiece a correr la imagen como un contenedor.

Para construir una imagen se usa la terminal. En la terminal (En el directorio donde se encuentra el Dockerfile) se usa el comando:

``
docker build .
``

- Nota: El Dockerfile debe tener el nombre "Dockerfile" si no no lo detectará.
- Nota 2: Si el Dockerfile no está en el mismo directorio, entonces cambia el punto por el path del directorio.


Hay varias opciones que se le pueden dar al comando, para verlas ejecuta:

``
docker build --help
``

La opción tag es recomendada, ya que esta le da un nombre a la imagen.

``
docker build --tag hello-world .
``
El resultado de este comando es la imagen, y ésta se añadirá a nuestra imagenes locales, las cuales podemos ver con el comando:

``
docker images
``

## Correr y mantener imágenes
Para correr imágenes se utiliza el comando:
``
docker run <nombre-de-la-imagen>
``
Ahora la imagen correrá, como no se definieron puertos para que la imagen tuviera comunicación, entonces correrá aislada.

Para ver lo que está corriendo en el sistema usa el comando
``docker ps -a``

Para iniciar un contenedor que fue detenido se usa el comando 
``docker start <nombre-del-contenedor>``
 y para detener uno que está activo usa el comando: 
 ``docker stop <nombre-del-contenedor>``

Para remover un contenedor que fue detenido se usa el comando: ``
docker rm <nombre-del-contenedor>``

Al iniciar un contenedor se le pueden dar opciones, por ejemplo:

``docker run -p 8080:80 --name hello -d hello-world``

El nombre del contenedor es hello-world. Entre las opciones se ven -p, --name -d
    
- -p Esta opción mapear los puertos del host a los del contenedor, siendo <host>:<contenedor>
- --name Esta opción le da un nombre al contenedor, en este caso "hello"
- -d Esta opción le permite al contenedor correr en segundo plano.

Para ver logs de un contenedor se usa el comando:
``docker logs <nombre-del-contenedor>`` 
Esto ayuda a hacer troubleshooting o darle mantenimiento a un contenedor. El parámetro -f se usa para seguir los logs, y que salgan en el output de la terminal cuando sucede el evento.

## Subir tus imágenes a la nube.
[Dockerhub](https://hub.docker.com/) es un repositorio para imágenes de docker, tiene capacidades de auto-construcción, para equipos y organizaciones como control de acceso, etc.

Para poder usar Docker Hub es necesario tener una cuenta.

Dentro de docker hub se crea el repo, con las configuraciones deseadas, y docker hub dará un comando para subir imágenes al repo. El comando funciona cuando el repo y la imagen tienen el mismo nombre, el comando es el siguiente:
``docker push <nombre-de-la-imagen>``

El resultado de este comando es la subida a Docker Hub de nuestra imagen.

Para bajar una imagen de Docker Hub se utiliza el comando:
``docker pull <nombre-de-la-imagen>``
