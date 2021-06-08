Ejercicio 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.2 y que cumpla con los siguientes puntos?

1.- Que el contenedor se llame mongo_db
     docker run -d --name=mongo_db 

2.- Que el contenedor se mantenga en ejecución
    -d permite que la base de datos se siga ejecutando 

3.- Que el puerto asignado a la máquina host sea el 27027
    -p 27027:27017

4.- Que el usuario sea foo
    -e MONGO_INITDB_ROOT_USERNAME=foo

5.- Que el password sea bar123
    -e MONGO_INITDB_ROOT_PASSWORD=bar123

6.- Que se cree una base de datos llamada baz
    MONGO_INITDB_DATABASE=baz -v C:\Users\brand\OneDrive\Escritorio\BRENDESCUELA2\7semestre\DISEÑOYARQUITECTURA\PARCIAL2\Segundo_Parcial\Parte1:/docker-entrypoint-initdb.d mongo:4.2
        

7.- Que se cree una colección en la base de datos de baz llamada qux

9.- ¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?
    docker exec -it mongo_db bash
    mongo

RESPUESTAS
    AL MOMENTO DE INICIAR EL CONTENEDOR, MONGO NO PUEDE EJECUTAR, MAS BIEN, NO PUEDE CREAR UNA BASE DE DATOS CON UNA COLECCIÓN

COMANDO PARA CREAR CONTENEDOR 

    docker run -d --name=mongo_db -p 27027:27017 -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz -v C:\Users\brand\OneDrive\Escritorio\BRENDESCUELA2\7semestre\DISEÑOYARQUITECTURA\PARCIAL2\Segundo_Parcial\Parte1:/docker-entrypoint-initdb.d mongo:4.2
        