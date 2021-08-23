Ejercicio 2
Crea 4 contenedores por medio del cliente CLI de docker:

El 1er contenedor ejecutará un primer servidor de Redis y su nombre deberá de ser redis_db_1
El 2do contenedor ejecutará un segundo servidor de Redis y su nombre deberá de ser redis_db_2
El 3er contenedor ejecutará un tercer servidor de Redis y su nombre deberá de ser redis_db_3
El 4to contenedor deberá de ejecutar un servidor de Redis Commander el cual estará protegido con el usuario DASistemas y la contraseña 2do-parcial! para poder acceder a él. El contenedor debe de llamarse redis_dbms y tendrá que conectarse con todos los contenedores de Redis que se crearon en los pasos previos

Primero necesitaremos crear una network para conectar los contenedores:

docker network create part2

creamos los primeros 3 contenedores:

 docker run -d -p 6379:6379 --name redis_db_1 redis
 docker run -d -p 6380:6380 --name redis_db_2 redis
 docker run -d -p 6381:6381 --name redis_db_3 redis

El 4to contenedor deberá de ejecutar un servidor de Redis Commander el cual estará protegido con el usuario DASistemas y la contraseña 2do-parcial! para poder acceder a él. El contenedor debe de llamarse redis_dbms y tendrá que conectarse con todos los contenedores de Redis que se crearon en los pasos previos

docker run --name redis_dbms -d -p 8081:8081 --network=part2 -e REDIS_HOSTS=local:172.0.0.2:6379,local:172.0.0.3:6380,local:172.0.0.4:6381 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander

Para ver que todo este conectado correctamente y funcionando podemos utilizar:

docker logs redis_dbms

