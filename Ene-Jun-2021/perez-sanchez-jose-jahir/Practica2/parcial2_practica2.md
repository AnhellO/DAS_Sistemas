Parte 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MySQL versión 8 y que cumpla con los siguientes puntos?
El comando que use es el siguiente:
docker run --name=mysql_db -p 4000:4000  -e MYSQL_ROOT_PASSWORD=secret-pw -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz -d mysql:8

Finalmente, ¿con qué comando(s) puedo conectarme a mi base de datos de MySQL corriendo dentro de mi contenedor de mysql_db?
Con el comando: docker exec -it mysql_db bash y luego use mysql -u root -p y despues hice un use baz para checar que la base existia,
no lo hice con mysql -u foo -p bar123 porque me arrojaba un error.

Parte 2

Los comandos usados fueron:
Para crear la red - docker network create Prac2
Para crear el contenedor de mongo conectado a la red - docker run -d -p 27017:27017 --name m1 --network Prac2 mongo
Para crear el contenedor de mongo express conectado a la red y al contenedor de mongo - docker run -d --name mexpress --network Prac2 -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=DAS -e ME_CONFIG_BASICAUTH_PASSWORD=abcde123?! -p 8081:8081 mongo-express

Parte 3

docker network create Prac2
docker run -d -p 27017:27017 --name mongo --network Prac2 mongo
docker run -d -p 6379:6379 --network=Prac2 --name redis redis --protected-mode no