Ejercicio 3
1. crear volumen
docker volume create redis_volume

2. crear network
docker network create ejercicio3

3. crear contenedor redis
docker run --name redis -d -p 6379:6379 -v redis_volume --network=ejercicio3 redis

4. ver las IP de los contenedores
docker network inspect ejercicio3

5. crear la imagen
docker build -t mariacastro/redis_json .

6. creamos el contenedor que utiliza la imagen
docker run -d --name redis_json_py --network ejercicio3 mariacastro/redis_json:latest

7. subimos a dockerhub
docker push mariacastro/redis_json