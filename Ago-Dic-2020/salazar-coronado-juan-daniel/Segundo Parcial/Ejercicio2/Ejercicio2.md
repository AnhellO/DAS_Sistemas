# Comandos para crear los contenedores:
- Contenedor 1: docker run --name redis -p 6379:6379 -d redis
- Contenedor 2: 
docker run --rm --name commander -d --link redis:conexionrc --env REDIS_HOSTS=local:redis:6379 --env HTTP_USER=daniel --env HTTP_PASSWORD=dm16 -p 8081:8081 rediscommander/redis-commander:latest

### Comando que use para llegar hasta la carpeta del ejercicio
cd desktop\universidad\diseño y arquitectura de software\das_sistemas\ago-dic-2020\salazar-coronado-juan-daniel\segundo parcial\ejercicio2