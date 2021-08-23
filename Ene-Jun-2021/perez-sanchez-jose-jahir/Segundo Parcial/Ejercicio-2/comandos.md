* Crear contenedores de Redis:
- docker run --name redis_db_1 -p 6379:6379 -d redis
- docker run --name redis_db_2 -p 6380:6379 -d redis
- docker run --name redis_db_3 -p 6381:6379 -d redis

* Crear Redis DBMS:
- docker run --name redis_dbms -e REDIS_HOSTS=local:redis_db_1:6379,local:redis_db_2:6379,local:redis_db_3:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do_Parcial! -p 8081:8081 -d  rediscommander/redis-commander:latest