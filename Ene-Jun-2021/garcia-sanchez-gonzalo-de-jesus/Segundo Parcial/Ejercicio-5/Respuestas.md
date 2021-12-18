# Gonzalo Garcia

# para poder ejecutar el docker-compose.yml

    Tube que hacer el docker-compose.yml como en el ejercicio 2 
    pero en la parte de el redis-commander denttro del docker-compose.yml
    tube que ponerlo y luego eliminarlo de docker desktop para poder accedes 
    a la Docker network inspect ejercicio-5_p2e2 para asi sacar las "IPv4Address"
    de los 3 diferentes contenedores de docker para asi extraerlas "IPv4Address" y 
    ponerlas en el nuevo redis-commander para poder acceder al http://localhost:8081/
    y asi poder acceder a las 3 diferentes rutas de los contenedores de docker
    dejare el cmd.txt para pegar hay los comandos que use para este ejercicio y las fotos


    docker run --name redis_dbms -d -p 8081:8081 --network=ejercicio-5_p2e2 -e REDIS_HOSTS=redis_db_1:192.168.112.3:6379,redis_db_2:192.168.112.4:6379,redis_db_3:192.168.112.2:6379 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! rediscommander/redis-commander:latest