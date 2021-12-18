docker network create practica2

docker run -d -p 6379:6379 --network=practica2 --name redis_db_1 redis   

docker run -d -p 6380:6379 --network=practica2 --name redis_db_2 redis   

docker run -d -p 6381:6379 --network=practica2 --name redis_db_3 redis    

Docker network inspect practica2

docker run --name redis_dbms -d -p 8081:8081 --network=practica2 -e REDIS_HOSTS=redis_db_1:172.19.0.2:6379,redis_db_2:172.19.0.3:6379,redis_db_3:172.19.0.4:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander:latest

http://localhost:8081/

