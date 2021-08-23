Ejercicio 3
=============
crear volumen
-----------------
- docker volume create redis_volume

crear network
--------------
- docker network create ejercicio-3 

crear contenedor redis
---------------------
- docker run --name redis -d -p 6379:6379 -v redis_volume --network=ejercicio-3 redis

ver las IP de los contenedores
-----------------------------
- docker network inspect ejercicio-3

crear la imagen
----------------
- docker build -t rephyroth/redis_json .

creamos el contenedor que utiliza la imagen
-----------------------------
- docker run -d --name redis_json_py --network ejercicio-3 rephyroth/redis_json:latest

subimos a dockerhub
------------------------------
- docker push rephyroth/redis_json
