Crea 4 contenedores por medio del cliente CLI de docker:

El 1er contenedor ejecutará un primer servidor de Redis y su nombre deberá de ser redis_db_1
El 2do contenedor ejecutará un segundo servidor de Redis y su nombre deberá de ser redis_db_2
El 3er contenedor ejecutará un tercer servidor de Redis y su nombre deberá de ser redis_db_3
El 4to contenedor deberá de ejecutar un servidor de Redis Commander el cual estará protegido con el usuario DASistemas y la contraseña 2do-parcial! para poder acceder a él. El contenedor debe de llamarse redis_dbms y tendrá que conectarse con todos los contenedores de Redis que se crearon en los pasos previos

Verifica que puedes acceder correctamente a la interfaz de Redis Commander y que los 3 contenedores de Redis son accesibles desde el DBMS.

Comandos:

docker network create p2e2
docker run -d -p 6379:6379 --network p2e2 --name redis_db1 redis --protected-mode no
docker run -d -p 6380:6379 --network p2e2 --name redis_db2 redis --protected-mode no
docker run -d -p 6381:6379 --network p2e2 --name redis_db3 redis --protected-mode no
docker network inspect p2e2
docker run --name redis_dbms -d -p 8081:8081 --network p2e2 -e REDIS_HOSTS=local:172.18.0.2:6379,local:172.18.0.3:6379,local:172.18.0.4:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander
docker logs redis_dbms