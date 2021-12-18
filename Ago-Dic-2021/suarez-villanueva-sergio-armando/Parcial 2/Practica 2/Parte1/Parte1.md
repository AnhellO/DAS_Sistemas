¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.4 y que cumpla con los siguientes puntos?

Que el contenedor se llame mongo_db
Que el contenedor se mantenga en ejecución
Que el puerto asignado a la máquina host sea el 27027
Que el usuario sea foo
Que el password sea bar123
Que se cree una base de datos llamada baz
Que se cree una colección en la base de datos de baz llamada qux

CREAR
1. docker run -d -p 2027 --name mongodb mongo:4.4

ACCESAR
2. docker exec -it mongodb bash

CREAR BD
3. use baz

USER Y PASSWORD
4. db.createUser({user: "foo", pwd: "bar123", roles: [] })

CREAR COLECCION E INSERTAR DATOS
5. db.qux.save({nombre: "Cristiano", apellido: "Ronaldo" })

#Finalmente, contesta a las siguientes preguntas:

¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?**
- connect('baz', 'foo', 'bar123')

¿Cómo puedo insertar este registro en la colección de qux creada previamente?**
- db.nombreColeccion.save({name: 'al', age: 18, status: 'D', groups: ['politics', 'news']})