¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MySQL versión 8 y que cumpla con los siguientes puntos?

    Que el contenedor se llame mysql_db
    Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)
    Que el puerto asignado a la máquina host sea el 4000
    Que el usuario sea foo
    Que el password sea bar123
    Que se cree una base de datos llamada baz

R:  El comando que se uso para la sentencia anterior fue: 

                docker run -p 4000:4000 --name=mysql_db -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz -e MYSQL_ROOT_PASSWORD=12345 -d mysql:8


Finalmente, ¿con qué comando(s) puedo conectarme a mi base de datos de MySQL corriendo dentro de mi contenedor de mysql_db?

R: El comando que se uso para conectarse a la base de datos fue:
            docker exec -it 3bb9acdaca3a bash (Se ejecuta el container creado poniendo el id que le pertenece)

    Despues, ya dentro de nuestra terminal, ingresamos a mysql con el comando: 
                    mysql -u foo -p (donde foo es nuestro usuario, y la contraseña con la que ingresamos es: bar123)

