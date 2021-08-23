Ejercicio 1
=============

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.2 y que cumpla con los siguientes puntos?
------------
docker run --name=mongo_db -d -p 27027:27027 -e ME_CONFIG_MONGODB_ADMINUSERNAME=foo -e  ME_CONFIG_MONGODB_ADMINPASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz -e MONGO_INITDB_COLLECTION=qux mongo:4.2

¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?
-----------
docker exec -it mongo_db bash

mongo


¿Cómo puedo insertar este registro en la colección de qux creada previamente?
----------

 use baz

 db.qux.insertOne({name:"al",age:18,status:"D",groups:["politics","news"]})



