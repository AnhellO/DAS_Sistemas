Comandos que se usaron:


docker network create redisNetwork

                             
Contenedor 1: docker run -d -p 6379:6379 --network=redisNetwork --name redis_db_1 redis

Contenedor 2: docker run -d -p 6380:6379 --network=redisNetwork --name redis_db_2 redis

Contenedor 3: docker run -d -p 6381:6379 --network=redisNetwork --name redis_db_3 redis

 -e REDIS_HOSTS= {cualquiernombre:ipdelContainer:Puerto}
docker run -d -p 8081:8081 --network=redisNetwork --name redis_dbms -e REDIS_HOSTS=mylocal1:172.20.0.2:6379,mylocal2:172.20.0.3,mylocal3:172.20.0.4:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander 


