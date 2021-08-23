Ejercicio 1

Comando para levantar contenedor Docker que corra un servidor MongoDB 4.2 con las caracteristicas indicadas:

docker run -d -p 27027:27027 -e MONGODB_USER=foo -e MONGODB_PASSWORD=bar123 -e MONGODDB_NAME=baz --name=mongo_db mongo:4.2 

¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?

docker exec -it mongo_db mongo

¿Cómo puedo insertar este registro en la colección de qux creada previamente?
Despues de conectarnos a la base de MongoDB. 
Usando el comando use seleccionamos la base de datos con la que vamos a trabajar:

use mongo_db

Creamos la coleccion qux con el siguiente comando:

db.createCollection('qux')

Insertamos el registro indicado con el siguiente comando:

db.qux.insert({"name":"al","age":18,"status":"D","groups":["politics","news"]})

Si queremos ver los datos ingresados podemos utilizar el comando:

db.qux.find();
