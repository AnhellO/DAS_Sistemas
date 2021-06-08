# Ejercicio 1
¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.2 y que cumpla con los siguientes puntos?

Que el contenedor se llame mongo_db
Que el contenedor se mantenga en ejecución
Que el puerto asignado a la máquina host sea el 27027
Que el usuario sea foo
Que el password sea bar123

Se usaron los sig comandos:
- sudo docker run --name mongo_db -p 27027:27017  -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123  -d mongo:4.2

¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?
- docker exec -it mongo_db /bin/bash
- mongo
- use admin 
- db.auth("foo","bar123"); (Permite a un usuario autenticarse en la base de datos)
- show dbs (muestra base de datos)

Que se cree una base de datos llamada baz:
- use baz (crea base de datos)

Que se cree una colección en la base de datos de baz llamada qux
- Crea la coleccion qux: e inserta datos
- ¿Cómo puedo insertar este registro en la colección de qux creada previamente?
    db.qux.save({name:'al', age: 18, status: "D",groups: ["politics","news"]})
    db.qux.save({name:'an', age: 20, status: "C",groups: ["asna","nana"]})
- db.qux.find() (método se obtiene una lista de colecciones.)
-show dbs (muestra base de datos)
-show collections (muestra las colecciones creadas)
