docker compose build

docker network create practica5

docker run --name redis_dbms -d -p 8081:8081 --network=practica5 -e REDIS_HOSTS=redis_db_1:172.19.0.2:6379,redis_db_2:172.19.0.3:6379,redis_db_3:172.19.0.4:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander:latest