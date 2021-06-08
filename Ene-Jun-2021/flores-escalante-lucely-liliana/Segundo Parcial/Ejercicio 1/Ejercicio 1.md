¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.2 y que cumpla con los siguientes puntos?

Que el contenedor se llame mongo_db
Que el contenedor se mantenga en ejecución
Que el puerto asignado a la máquina host sea el 27027
Que el usuario sea foo
Que el password sea bar123
Que se cree una base de datos llamada baz
Que se cree una colección en la base de datos de baz llamada qux

Finalmente, contesta a las siguientes preguntas:

¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db? ¿Cómo puedo insertar este registro en la colección de qux creada previamente?

Respuesta:
No se puede crear una base de datos a través de Mongo con una coleccion al iniciar el contenedor.

Comando: docker run -d --name=mongo_db -p 27027:27017 -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz -v "C:\Users\lulif\Documents\DAS_Sistemas\Ene-Jun-2021\flores-escalante-lucely-liliana\Segundo Parcial\Ejercicio 1\docker-entrypoint-initdb.d":/docker-entrypoint-initdb.d mongo:4.2
docker exec -it mongo_db bash
mongo -u "foo" -p "bar123"
 show dbs
  use baz
  show collections