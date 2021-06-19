//Crear volumen

// sudo docker volume create redis_volume

//crear contenedor redis

//sudo docker run -d -p 5000:6379 --network=Ejercicio2 --name redis_db redis --mount source=redis_volume destination=/usr/src/app --protected-mode no

//Link repo

// https://hub.docker.com/r/bryanbalderas/redis_json