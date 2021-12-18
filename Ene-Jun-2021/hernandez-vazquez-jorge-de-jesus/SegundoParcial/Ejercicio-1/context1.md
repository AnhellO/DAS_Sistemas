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
        R:       docker exec -it mongo_db /bin/bash
                    mongo -u foo -p (password)
    
    ¿Cómo puedo insertar este registro en la colección de qux creada previamente?
        R:      Mediante el CLI de MongoDB o con el DBMS de Mongoexpress


Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.


            docker run -p 27027:27027 --name=mongo_db -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz -d mongo:4.2



