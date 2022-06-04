## LABORATORIO 2

Listamos los contenedores que tenemos con el comando: `sudo docker ps -a`, vemos los contenedores que se encuentra en nuestro equipo.

![](/imagenes/1.png)

1. Iniciar el container de `MongoDB` utilizando el comando `docker run -d -p 27017:27017 --name m1 mongo`.

![](/imagenes/2.png)


   1. Puedes conectarte al contenedor de Mongo con `docker exec -it m1 /bin/bash` y luego conectarte a `MongoDB` por medio del comando `mongo`.
   2. Para salir de la terminal interactiva del contenedor, primero hay que salir de `MongoDB` tecleando el comando `exit`, y una vez fuera podemos tecler la combinación `Ctrl+P` y `Ctrl+Q` para salir.

![](/imagenes/3.png)


2. Utilizaremos los scripts de `Python` existentes en la carpeta para popular la colección de mongo, utilizando la librería <https://api.mongodb.com/python/current/tutorial.html>.
   1. Instalar la librería de mongo por medio del comando `pip install pymongo`.
   2. Ejecuta los scripts con `python populate.py` y `python find.py`.
   3. Revisa los registros por medio del CLI de `mongo` o de tu DBMS favorito.

![](/imagenes/4.png)
   
3. Una vez que hayas terminado de jugar con `MongoDB` y los scripts de `Python`, asegúrate de detener y remover el contenedor de `MongoDB` en ejecución utilizando `docker stop m1; docker rm m1`.

![](/imagenes/5.png)

Viedno que se puede usar scripst de python para usar con el contenedor de docker que tiene una imagen de mongo db esto se pone más interesante y divertido, eh aprendido a usar los contenedores con python. 

