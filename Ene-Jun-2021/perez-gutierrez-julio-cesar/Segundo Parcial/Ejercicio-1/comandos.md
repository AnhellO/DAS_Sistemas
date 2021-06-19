docker run -d -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE:faz -p 27017:27017 --name mongo_db mongo:4.2

docker ps -a

¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?
docker exec -it mongo_db /bin/bash

¿Cómo puedo insertar este registro en la colección de qux creada previamente?
use faz
db.qux.save({name:"al",age:18,status:"D",groups:["politics", "news"]})
db.qux.find();