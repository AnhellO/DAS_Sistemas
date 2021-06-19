Ejercicio 2

Network
► docker network create p2e2

Contenedores
Contendor 1:
► docker run -d -p 6379:6379 --network=p2e2 --name redis_db_1 redis
Contendor 2:   
► docker run -d -p 6380:6379 --network=p2e2 --name redis_db_2 redis
Contendor 3:   
► docker run -d -p 6381:6379 --network=p2e2 --name redis_db_3 redis    

Mostrar las IPv4
► Docker network inspect p2e2


IPv4
	redis-commander 

    (IPv4Address": "172.22.0.2:6379 )

    (IPv4Address": "172.22.0.3:6380 )

    (IPv4Address": "172.22.0.44:6381 )


Crear el redis-commander
► docker run --name redis_dbms -d -p 8081:8081 --network=p2e2 -e REDIS_HOSTS=redis_db_1:172.22.0.2:6379,redis_db_2:172.22.0.3:6380,redis_db_3:172.22.0.4:6381 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander:latest


Verificar que todo este correcto
►http://localhost:8081/

