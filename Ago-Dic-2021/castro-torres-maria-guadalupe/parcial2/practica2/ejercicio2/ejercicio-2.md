1. Crear una network
docker network create ejercicio2

2. Crear los contenedores
docker run --name redis1 -d -p 6379:6379 --network ejercicio2 redis
docker run --name redis2 -d -p 6380:6379 --network ejercicio2 redis
docker run --name redis3 -d -p 6381:6379 --network ejercicio2 redis

3. Ver las IP de los contenedores
docker network inspect ejercicio2

4. crear el contenedor redis-commander
docker run --name redis_dbms -d -p 8081:8081 -e HTTP_USER=DASistemas -e docker run --name redis_dbms -d -p 8081:8081 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=Ya-Casi-Se-Acaba-El-Semestre! -e REDIS_HOSTS=172.19.0.2:redis1:6379,172.19.0.3:redis2:6379,172.19.0.4:redis3:6379 --network ejercicio2 rediscommander/redis-commander

