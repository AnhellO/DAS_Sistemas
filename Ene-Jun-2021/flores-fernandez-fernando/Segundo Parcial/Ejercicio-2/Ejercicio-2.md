Ejercicio 2
=============
crear una network
-----------------
- docker network create ejercicio-2

crear los contenedores
---------------------
- docker run --name redis_db_1 -d -p 6379:6379 --network ejercicio-2 redis
- docker run --name redis_db_2 -d -p 6380:6379 --network ejercicio-2 redis
- docker run --name redis_db_3 -d -p 6381:6379 --network ejercicio-2 redis

ver las IP de los contenedores
-----------------------------
- docker network inspect ejercicio-2 

crear el contenedor redis-commander
-----------------------------------
- docker run --name redis_dbms -d -p 8081:8081 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! -e REDIS_HOSTS=172.21.0.2:redis_db_1:6379,172.21.0.3:redis_db_2:6379,172.21.0.4:redis_db_3:6379 --network ejercicio-2 rediscommander/redis-commander