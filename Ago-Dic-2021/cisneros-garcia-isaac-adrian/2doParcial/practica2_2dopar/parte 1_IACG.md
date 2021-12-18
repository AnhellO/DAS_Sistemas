# Parte 1 comando completo

docker run -d -p 27027:27027 --name mongo_db -e MONGODB_INITDB_ROOT_USERNAME=foo -e MONGODB_INITDB_ROOT_PASSWORD=bar123 mongo:4.4
db.qux.save({nombre: "Juanito", apellido: "Pony" })
**_¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?_**
docker exec -it mongo_db mongo

**_¿Cómo puedo insertar este registro en la colección de qux creada previamente?_**
use baz   
db.qux.save({name: "al", age: 18, status:"D", groups:["politics","news"]})
db.qux.find()