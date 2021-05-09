# Práctica 2 - Parte 2

Crea 2 contenedores por medio del cliente CLI de docker:

El 1er contenedor ejecutará un servidor de MongoDB y su nombre deberá de ser m1
- docker network create mongo_network (crea red con el nombre de mongo_network)
- sudo docker run -d -p 27018:27017 --name m1 --network mongo_netwrok mongo (crea contenedor con el nombre m1, le asigne el puerto 27018 de mi maquina, se conecta con la red de mongo_network)

El 2do contenedor ejecutará un cliente de Mongo Express el cual se llame mexpress y que se conectará al contenedor m1 creado en el punto anterior. Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:
Usuario: DAS
Password: abcde123?!

- docker run -d --name mexpress --network mongo_network -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=DAS -e ME_CONFIG_BASICAUTH_PASSWORD=abcde123?! -p 8081:8081 mongo-express (crea contenedir que se llama mexpress, se le asignan variables de autentificacion (usario y contraseña), se conecta con el contendor de m1)

Se usaron los sig comandos:
- sudo docker ps -a (muestra contenedores con sus caracteristicas)
-  sudo docker stop $(sudo docker ps -q -a) Detiene todos los contenedores