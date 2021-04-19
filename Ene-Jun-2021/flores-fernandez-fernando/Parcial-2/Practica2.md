Parte 1
===============
levantar un contenedor Docker MySQL
------------------------------------
docker run --name=mysql_db -p 4000:3306 -e MYSQL_ROOT_PASSWORD=pass -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz -d mysql:8
- --name : nombre del container
- -p : puerto host/bind container 
- -e : enviroment root password o usuario y password
- -d : corra en background
- mysql:8 : version 8 

docker exec -it mysql_db bash
- it : terminal interactiva

 mysql -u foo -pbar123
 - -u :usuario
 - -p :password

 Parte 2
===============
docker network create --driver bridge practica2_network
- --driver : driver que usa para comunicacrse con el network

docker run -d -p 27017:27017 --network practica2_network --name m1 mongo
- --network :red que se va a conectar el contenedor

docker run --name=mexpress --network practica2_network -e ME_CONFIG_MONGODB_SERVER=m1 -e MONGO_INITDB_ROOT_USERNAME=DAS -e MONGO_INITDB_ROOT_PASSWORD=abcde123?!  -p 8081:8081 mongo-express

Parte 3
============
docker run -d -p 6379:6379 --name redis --network practica2_network redis

docker run -d -p 27017:27017 --network practica2_network --name mongo mongo

docker build -t python-rand .

docker run -it -p 2308:2308 --name pythonRand --network practica2_network python-rand
