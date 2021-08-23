Ejercicio 5

docker-compose.yml - Ejercicio 2

Comandos utilizados
Docker Compose
► docker-compose up -d

Networks ID
► docker network ls

Crear el redis-commander
► docker run --name redis_dbms -d -p 8081:8081 --network=desktop_p2e2 -e REDIS_HOSTS=redis_db_1:192.168.112.3:6379,redis_db_2:192.168.112.4:6379,redis_db_3:192.168.112.2:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander:latest

Verificar
► docker ps


