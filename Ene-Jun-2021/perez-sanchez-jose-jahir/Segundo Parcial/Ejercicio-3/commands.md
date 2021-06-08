* Crear Volumen:
- docker volume create redis_volume

* Crear container de redis en el volumen creado:
- docker run --name redis -p 6379:6379 -v redis_volume:/data -d redis

* Crear imagen por me dio del Dockerfile:
- docker build -t jahar/redis_json .

* Hacer login:
-  Docker login

* Enviarla a DockerHub:
- docker push jahar/redis_json
Nota: No se porque sale mounted from jahar/static_flask si ya borre esa imagen

* Link de DockerHub:
- https://hub.docker.com/r/jahar/redis_json

* Contenedor con la imagen:
- docker run --name redis_json_py -d -p 5000:8000 jahar/redis_json