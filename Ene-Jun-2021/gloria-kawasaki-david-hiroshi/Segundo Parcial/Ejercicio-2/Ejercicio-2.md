Ejercicio 2
Crea 4 contenedores por medio del cliente CLI de docker:

El 1er contenedor ejecutará un primer servidor de Redis y su nombre deberá de ser redis_db_1
El 2do contenedor ejecutará un segundo servidor de Redis y su nombre deberá de ser redis_db_2
El 3er contenedor ejecutará un tercer servidor de Redis y su nombre deberá de ser redis_db_3
El 4to contenedor deberá de ejecutar un servidor de Redis Commander el cual estará protegido con el usuario DASistemas y la contraseña 2do-parcial! para poder acceder a él. El contenedor debe de llamarse redis_dbms y tendrá que conectarse con todos los contenedores de Redis que se crearon en los pasos previos

Verifica que puedes acceder correctamente a la interfaz de Redis Commander y que los 3 contenedores de Redis son accesibles desde el DBMS.

Respuesta: para que cualquier cantidad de contenedores puedan conectarse entre si le tendra que realizar primero una network, en este caso sera llamada "ejercicio2". Se crea con el siguiente comando:

- sudo docker network create ejercicio2

Despues se procede a crear los contenedores, indicandole que debe estar en la red previamente creada con --network, generando los siguientes comandos:
base:

- sudo docker run -d -p 6379:6379 --network ejercicio2 --name redis_db1 redis --protected-mode no
- sudo docker run -d -p 6380:6379 --network ejercicio2 --name redis_db2 redis --protected-mode no
- sudo docker run -d -p 6381:6379 --network ejercicio2 --name redis_db3 redis --protected-mode no

Por ultimo, se crea el cuarto contenedor, quedando de la siguiente manera:
- d run -d -p 8081:8081 -e REDIS_HOSTS=local:redis:6379 -e HTTP_USER=root -e HTTP_PASSWORD=qwerty rediscommander/redis-commander:latest

sudo docker run --name redis_dbms -d -p 8081:8081 --network ejercicio2 -e REDIS_HOSTS=local:172.19.0.2:6379,local:172.19.0.3:6379,local:172.19.0.4:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander

(NOTA: en las capturas se observa que se usa un comando diferente el cual es "d", esto es un alias de los comandos "sudo docker")