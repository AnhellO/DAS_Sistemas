# Soluciones

## Ejercicio 1

- MySQL: `docker run --name mysql_db -p 4000:3306 -e MYSQL_ROOT_PASSWORD=secret123 -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz -d mysql:8`
- Conectarse a la DB con alguno de los 2 comandos siguientes:
  - `docker exec -it mysql_db mysql -u foo -pbar123`
  - `docker exec -it mysql_db /bin/bash` y luego dentro de la sesión de bash del contenedor `mysql -u foo -pbar123`

## Ejercicio 2

- Redis: `docker run -d -p 6379:6379 --name redis redis`
- Redis Commander: `docker run --name commander -d -p 8081:8081 -e REDIS_HOSTS=local:{redis-container-IP}:6379 -e HTTP_USER={usuario} -e HTTP_PASSWORD={password} rediscommander/redis-commander` donde ->
  - `{redis-container-IP}`: la IP de tu contenedor de `redis`
  - `{usuario}`: un nombre de usuario que tu elijas
  - `{password}`: un password que tu elijas
- Visita <http://0.0.0.0:8081/>

## Ejercicio 3

- Volumen: `docker volume create mongo_volume`
- 1er contenedor de Mongo: `docker run -d -p 27017:27017 --name mongo -v mongo_volume:/data/db mongo`
- Ejecuta los scripts con `python ejercicio3/populate.py` y `python ejercicio3/find.py`
- Detén y borra el contenedor actual de Mongo: `docker stop mongo; docker rm mongo`
- 2do contenedor de Mongo: `docker run -d -p 27017:27017 --name mongo2 -v mongo_volume:/data/db mongo`
- Ejecuta el script `python ejercicio3/find.py` de nuevo

## Ejercicio 4

- Dockerfile final: [`Dockerfile`](ejercicio-4/Dockerfile)
- Construye la imágen con `docker build -t {mi-user}/static_flask .`
- Envíala a tu cuenta de `DockerHub` con `docker push {mi-user}/static_flask`
- Instancia un contenedor con `docker run --name flask -d -p 5000:8000 {mi-user}/static_flask`

## Ejercicio 5

- Docker Compose final: [`docker-compose.yml`](ejercicio-5/docker-compose.yml)
- Utiliza `docker-compose up -d --build` para ejecutar el stack de la aplicación
