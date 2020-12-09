#### Creamos el contenedor en dockerhub
* sudo docker build -t jorgelof/hello_flask .

* sudo docker login

* sudo docker tag jorgelof/hello_flask  jorgelof/hello_flask:extraordinario

* sudo docker push jorgelof/hello_flask:extraordinario

* sudo docker pull jorgelof/hello_flask:extraordinario 

* sudo docker run --name hflask -p 9999:8000 -d jorgelof/hello_flask:extraordinario

* sudo docker ps


### Enlace de Duckerhub

[https://hub.docker.com/repository/docker/jorgelof/hello_flask](https://hub.docker.com/repository/docker/jorgelof/hello_flask)
