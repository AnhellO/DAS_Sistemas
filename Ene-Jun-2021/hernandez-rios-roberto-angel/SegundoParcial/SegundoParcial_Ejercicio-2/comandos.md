-Creando network
docker network create red1
-Creando contenedores
docker run  -p 6379:6379 --network=red1 -d --name redis_db_1 redis --protected-mode no
docker run  -p 4000:6379 --network=red1 -d --name redis_db_2 redis --protected-mode no
docker run  -p 5000:6379 --network=red1 -d --name redis_db_3 redis --protected-mode no
-revisar la network
docker inspect red1
Poner la IPv4Address: de nuestra network
docker run --name redis_dbms -d -p 8081:8081 --network=red1 -e REDIS_HOSTS=local:172.19.0.2:6379,redis_db_2:172.19.0.3,redis_db_3:172.19.0.4 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander