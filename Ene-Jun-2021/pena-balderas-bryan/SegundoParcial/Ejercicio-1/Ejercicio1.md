Ejercicio 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.2 y que cumpla con los siguientes puntos?

    Que el contenedor se llame mongo_db
    Que el contenedor se mantenga en ejecución
    Que el puerto asignado a la máquina host sea el 27027
    Que el usuario sea foo
    Que el password sea bar123
    Que se cree una base de datos llamada baz
    Que se cree una colección en la base de datos de baz llamada qux

Finalmente, contesta a las siguientes preguntas:

    ¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?

    // sudo docker exec -it mongo_db bash

    ¿Cómo puedo insertar este registro en la colección de qux creada previamente?

    // db.insertOne({
        name:"al",
        age:18,
        status:"D",
        groups:["politics","news"]
    })

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

///Bryan Peña Balderas
