¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.2 y que cumpla con los siguientes puntos?
    -docker run --name mongo_db -v mongodata:/data/db -d -p 27027:27027 mongo

¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?
    -winpty docker exec -it mongo_db bash
    -use baz

¿Cómo puedo insertar este registro en la colección de qux creada previamente?
    -db.qux.insert({name: "al", age: 18, status: "D", groups: ["politics", "news"] })