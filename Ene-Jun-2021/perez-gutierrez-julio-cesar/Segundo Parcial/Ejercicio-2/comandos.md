
docker network create redinet

docker run -d -p 6379:6379 --network=redinet --name redis_db_1 redis --protected-mode no
docker run -d -p 80:6379 --network=redinet --name redis_db_2 redis --protected-mode no
docker run -d -p 4000:6379 --network=redinet --name redis_db_3 redis --protected-mode no

docker inspect redinet

docker run --name redis_dbms -d -p 8081:8081 --network=redinet -e REDIS_HOSTS=redis_db_1:172.18.0.2:6379,redis_db_2:172.18.0.3,redis_db_3:172.18.0.4 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander