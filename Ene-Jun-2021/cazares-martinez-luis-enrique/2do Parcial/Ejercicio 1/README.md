Ejercicio 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de 
MongoDB versión 4.2 y que cumpla con los siguientes puntos?

Que el contenedor se llame mongo_db
Que el contenedor se mantenga en ejecución
Que el puerto asignado a la máquina host sea el 27027
Que el usuario sea foo
Que el password sea bar123
Que se cree una base de datos llamada baz
Que se cree una colección en la base de datos de baz llamada qux

► docker run -d -p 27027:27017 --name=mongo_db -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz mongo:4.2 *

¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?
¿Cómo puedo insertar este registro en la colección de qux creada previamente?

► docker exec -it mongo_db bash

► mongo 27027

► db.qux1.insert({
    name: "all",
    age: 18,
    status: "D",
    groups: ["politics", "news"]
    
  })




