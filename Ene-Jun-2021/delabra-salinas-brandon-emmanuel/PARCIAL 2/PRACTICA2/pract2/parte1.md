Parte 1
¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MySQL versión 8 y que cumpla con los siguientes puntos?
    docker run --name=mysql_db -p 4000:3306 -e MYSQL_ROOT_PASSWORD=pass -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz -d mysql:8

    Que el contenedor se llame mysql_db
        docker run --name=mysql_db -d
    Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)
        -d "Permite que siga corriendo" 
    Que el puerto asignado a la máquina host sea el 4000
        -p 4000:3306
    Que el usuario sea foo
        -e MYSQL_USER=foo
    Que el password sea bar123
        -e MYSQL_PASSWORD=bar123
    Que se cree una base de datos llamada baz
        -e MYSQL_DATABASE=baz -d mysql:8

    Finalmente, ¿con qué comando(s) puedo conectarme a mi base de datos de MySQL corriendo dentro de mi contenedor de mysql_db?
        docker exec -it mysql_db bash

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.