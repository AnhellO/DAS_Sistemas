Ejercicio 2


Comandos ejecutados:

1.- docker network create p2e2
2.- docker run -d -p 6379:6379 --network p2e2 --name redis_db1 redis --protected-mode no
3.- docker run -d -p 6380:6379 --network p2e2 --name redis_db2 redis --protected-mode no
4.- docker run -d -p 6381:6379 --network p2e2 --name redis_db3 redis --protected-mode no
1.- docker run --name redis_dbms -d -p 8081:8081 --network p2e2 -e REDIS_HOSTS=local:172.18.0.2:6379,local:172.18.0.3:6379,local:172.18.0.4:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander