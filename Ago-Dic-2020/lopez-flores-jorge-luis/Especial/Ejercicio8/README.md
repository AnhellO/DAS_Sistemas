### Primero se crea una red de docker:

* sudo docker network create ejercicio8

### Para crear el contenedor de mongo se ejecuta el siguiente comando:

* sudo docker run --name mongo -d -p 27017:27017 --network ejercicio8 mongo

### Para crear el contenedor de redis

* sudo docker run --name redis --network ejercicio8 -d -p 6379:6379 redis

### Finalmente corremos el compose

* sudo docker-compose up