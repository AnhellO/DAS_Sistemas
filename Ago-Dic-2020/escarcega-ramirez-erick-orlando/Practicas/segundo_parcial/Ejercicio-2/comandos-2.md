# docker run --name redis -p 6969:6379 -d redis

# docker run --name commander --link redis:serverredis -e REDIS_HOSTS=local:redis:6379 -e HTTP_USER=foo -e HTTP_PASSWORD=bar123 -p 8081:8081 rediscommander/redis-commander:latest