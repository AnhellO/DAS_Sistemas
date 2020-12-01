### Comandos

docker build -t drdz/static_flask .
docker run --name flask -p 8000:8000 drdz/static_flask
<!-- docker login --username=[usuario] --email=[contrasenia] -->
docker push drdz/static_flask


#### Link
https://hub.docker.com/repository/docker/drdz/static_flask