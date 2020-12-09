### Primero se crea una red de docker:

 * docker network create redis-net

### Para crear el contenedor de redis se ejecuta el siguiente comando:

* sudo docker run --name m1 -d -p 27017:27017 --network mongo_network mongo
 
### Para crear el contenedor de redis-commander

* sudo docker run --name mexpress -d -e HTTP_USER=DAS -e HTTP_PASSWORD=extra123 -e MONGO_PORT=27017 -e MONGO_HOST=mongo --network mongo_network -p 8081:8081  mongo-express

Entra a la dirección [http://localhost:8081/](http://localhost:8081/)