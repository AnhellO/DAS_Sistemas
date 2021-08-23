-creando network
docker network create redis_python
-creando volumen
docker volume create redis_volume
-creando el contenedor de redis
docker run -p 6379:6379 -v redis_volume:/var/lib/redis --network=redis_python -d --name redis redis --protected-mode no
-creando imagen con mi nombre usuario docker hub
docker build -t robertohr/redis_json .

docker run -d --name redis_json_py--network=redis_python robertohr/redis_json

docker run --name redis_dbms -d -p 8081:8081 --network=redis_python -e REDIS_HOSTS=local:redis:6379 -e HTTP_USER=admin -e HTTP_PASSWORD=123 rediscommander/redis-commander