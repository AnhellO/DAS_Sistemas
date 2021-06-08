-Para crear el contenedor
docker run -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -p 27017:27017 -d --name mongo_db mongo:4.2

-Ejecutarlo
docker exec -it mongo_db /bin/bash

-Para insertar el registro 
use admin
db.auth(“foo”, “bar123”)

use faz
db.qux.save({name:"al",age:18,status:"D",groups:["politics", "news"]})
db.qux.find();
