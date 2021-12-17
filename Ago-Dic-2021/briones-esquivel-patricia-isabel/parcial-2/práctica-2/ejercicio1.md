# Ejercicio 1
¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.4 y que cumpla con los siguientes puntos?
<br> 
- Que el contenedor se llame mongo_db, que el contenedor se mantenga en ejecución, que el puerto asignado a la máquina host sea el 27027
<br> docker run -d -p 27027 --name mongodb mongo:4.4

- Que el usuario sea foo, que el password sea bar123
<br> db.createUser({user: "foo", pwd: "bar123", roles: [] })
- Que se cree una base de datos llamada baz
<br> docker exec -it mongodb bash
<br> mongo
<br> use baz
- Que se cree una colección en la base de datos de baz llamada qux
<br> db.qux.save({username: "ackerman507" })

Finalmente, contesta a las siguientes preguntas:

- ¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?
<br> connect('baz', 'foo', 'bar123')
- ¿Cómo puedo insertar este registro en la colección de qux creada previamente?
<br> b.nombreColeccion.save({name: 'al', age: 18, status: 'D', groups: ['politics', 'news']})