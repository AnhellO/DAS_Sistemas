# Ejercicio 2
 Crea 4 contenedores por medio del cliente CLI de docker:
- docker network create redis_network (crear la red)
- docker inspect redis_network (muestra la información relevante de la network)

El 1er contenedor ejecutará un primer servidor de Redis y su nombre deberá de ser redis_db_1
- sudo docker run -d -p 6379:6379 --network=redis_network --name redis_db_1 redis --protected-mode no  (crea contenedor con el nombre redis_db_1, le asigne el puerto 6379 de mi maquina, se conecta con la red de redis_network)

El 2do contenedor ejecutará un segundo servidor de Redis y su nombre deberá de ser redis_db_2
- sudo  docker run -d -p 6378:6379 --network=redis_network --name redis_db_2 redis --protected-mode no  (crea contenedor con el nombre redis_db_2, le asigne el puerto 6378 de mi maquina, se conecta con la red de redis_network)
- 
El 3er contenedor ejecutará un tercer servidor de Redis y su nombre deberá de ser redis_db_3
- sudo docker run -d -p 6377:6379 --network=redis_network --name redis_db_3 redis --protected-mode no  (crea contenedor con el nombre redis_db_3, le asigne el puerto 6377 de mi maquina, se conecta con la red de redis_network)

El 4to contenedor deberá de ejecutar un servidor de Redis Commander el cual estará protegido con el usuario DASistemas y la contraseña 2do-parcial! para poder acceder a él. El contenedor debe de llamarse redis_dbms y tendrá que conectarse con todos los contenedores de Redis que se crearon en los pasos previos
Verifica que puedes acceder correctamente a la interfaz de Redis Commander y que los 3 contenedores de Redis son accesibles desde el DBMS.


-  sudo docker run --name redis_dbms -d -p 8081:8081  --network=redis_network  -e REDIS_HOSTS=local:172.21.0.2:6379,local2:172.21.0.3:6379,local3:172.21.0.4 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander (crea el contenedor redis_dbms, se la asigna un usuario y contraseña, y se le asignan los host  con el que se va a comunicar )
-  sudo docker logs redis_dbms (muestra la información acerca del contenedor)
-  sudo docker stop $(sudo docker ps -q -a) (Apaga todos los contenedores)