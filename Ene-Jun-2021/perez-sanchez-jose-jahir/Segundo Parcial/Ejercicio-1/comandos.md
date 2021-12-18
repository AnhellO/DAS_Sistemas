* MongoDB: docker run --name mongo_db -p 27027:27017 -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=daz -d mongo:4.2
La collection con el archivo mongo-init.js
* Conectarse a la DB:
- docker exec -it mongo_db /bin/bash y despues entrando con el comando mongo -u foo -p bar123
* Crear el documento de la collection:
- db.collection.insertOne({name: "all", age: 18, status: "D", groups: ["politics","news"]})