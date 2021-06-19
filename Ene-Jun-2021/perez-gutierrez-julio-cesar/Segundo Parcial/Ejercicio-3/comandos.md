docker network create red_redis

docker volume create redis_volume

docker run -d -p 6379:6379 -v redis_volume:/var/lib/redis --network=red_redis --name redis redis --protected-mode no

docker build -t 15604715/redis_json .

docker run -d --name pyredis --network=red_redis 15604715/redis_json

docker run --name redis_dbms -d -p 8081:8081 --network=red_redis -e REDIS_HOSTS=local:172.19.0.2:6379 -e HTTP_USER=foo -e HTTP_PASSWORD=bca rediscommander/redis-commander


docker login 
docker push 15604715/redis_json

Link DockerHub: https://hub.docker.com/repository/docker/15604715/redis_json 