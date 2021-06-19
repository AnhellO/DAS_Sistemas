Ejercicio 1
¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.2 y que cumpla con los siguientes puntos?

Que el contenedor se llame mongo_db
Que el contenedor se mantenga en ejecución
Que el puerto asignado a la máquina host sea el 27027
Que el usuario sea foo
Que el password sea bar123
Que se cree una base de datos llamada baz
Que se cree una colección en la base de datos de baz llamada qux

Respuestas:
Ya que Mongo se maneja distinto que las bases de datos SQL, para lograr hacer que se cree una abse de datos con una coleccion determinada, se tienen que hacer pasos extras antes. En primer lugar, se tiene que crear una carpeta con el nombre de "docker-entrypoint-initdb.d", dentro de esta carpeta pondremos nuestros scripts que queramos que se ejecuten al inicializar el contenedor. En este caso se usara un script llamado "init-mongo.js" para crear una base de datos llamada "baz" con el usuario y contrasenia dada, "foo" y bar123, respectivamente. Despues esta el archivo "seed.js" el cual se encarga de realizar una insercion en la coleccion ya que a diferencia de las bases de datos SQL no hay un equivalente a "CREATE DATABASE" o "CREATE TABLE" por lo que si queremos ver esta base de datos "baz" con la coleccion "qux" tendremos que forzosamente realizar una insercion.
Por lo tanto, el comando resultante quedaria de la siguiente forma:

- sudo docker run -d --name=mongo_db -p 27027:27017 -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz -v /home/hiroshi/Documents/'Escuela 3.0'/ArquiYDiseñoSoft/'Segundo Parcial'/Ejercicio-1/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d mongo:4.2

- sudo docker run -d --name=mongo_db -p 27027:27017 -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz -v ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js mongo:4.2
