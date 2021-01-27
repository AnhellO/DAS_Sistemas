### Comandos

docker run --name redis -p 6379:6379 -d redis
docker run --name commander -d -p 8081:8081 -e REDIS_HOSTS=local:redis:6379 -e HTTP_USER=user -e HTTP_PASSWROD=password rediscommander/redis-commander:latest