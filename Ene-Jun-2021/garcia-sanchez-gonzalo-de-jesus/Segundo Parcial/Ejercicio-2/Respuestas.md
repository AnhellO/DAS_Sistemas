# Gonzalo Garcia

# CREO UNA NETWORK

docker network create p2e2

# CREO LOS 3 CONTENEDORES DE REDIS

docker run -d -p 6379:6379 --network=p2e2 --name redis_db_1 redis   

docker run -d -p 6380:6379 --network=p2e2 --name redis_db_2 redis   

docker run -d -p 6381:6379 --network=p2e2 --name redis_db_3 redis    

# SACO LAS IPv4 DE CADA UNO DE LOS CONTENEDORES Y LOS AGREGO AL redis-commander 
Docker network inspect p2e2
## Estas son las IPv4 que sacamos de la network no siempre son las mismas, despues se las colocamos al comando de  redis-commander 

    (IPv4Address": "172.22.0.2:6379 )

    (IPv4Address": "172.22.0.3:6379 )

    (IPv4Address": "172.22.0.44:6379 )

# CREO EL redis-commander CON SUS RESPECTIVAS INDICACIONES Y LAS IPv4 DE LOS CONTENEDORES ANTERIORES
docker run --name redis_dbms -d -p 8081:8081 --network=p2e2 -e REDIS_HOSTS=redis_db_1:172.22.0.2:6379,redis_db_2:172.22.0.3:6379,redis_db_3:172.22.0.4:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander:latest

# VERIFICO SI SE ENCUENTRAN EN EL redis-commander

http://localhost:8081/

