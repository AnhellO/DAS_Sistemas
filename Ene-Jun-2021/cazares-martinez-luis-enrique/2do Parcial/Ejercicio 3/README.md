Ejercicio 3

Network
► docker network create P2E3

Volumen
► docker volume create --name redis_volume --driver local

Contenedor de redis
► docker run -d -p 6379:6379 -v redis_volume --network P2E3 --name redis_db_1 redis 

Construir Imagen
► docker build -t luisenrique94/redis_json .

Running DOCKERFILE 
► docker run -d --name redis_json_py --network P2E3 luisenrique94/redis_json:latest

Hacer push a DOCKER HUB
► docker push luisenrique94/redis_json

LINK
► https://hub.docker.com/r/luisenrique94/redis_json



