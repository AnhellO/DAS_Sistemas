//Crear cualquier contenedor de redis

//Sudo docker run -d -p 5000:6379 --network=Ejercicio2 --name redis_db_2 redis --protected-mode no




//Crear Contenedor Redis-Commander

//Sudo docker run -d --network=Ejercicio2 -e HTTP_USER=DASistemas -e HTTP_PASSWORD=2do-parcial! -e REDIS_HOSTS=redis_db_1,redis_db_2,redis_db_3 -p 8081:8081 --name redis_dbms rediscommander/redis-commander:latest