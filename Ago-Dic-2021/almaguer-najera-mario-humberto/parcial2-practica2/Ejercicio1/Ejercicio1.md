#¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.4 y que cumpla con los siguientes puntos?

**Primer comando para crear un contenedor mongodb con las especificaciones.**

1. docker run -d -p 2027 --name mongodb mongo:4.4

**Despues ejecutamos el siguiente comando para acceder al contenedor.**

2. docker exec -it mongodb bash

**Accedemos a mongodb escribiendo mongo en la terminal, para asi crear nuestra base de datos 'baz'**

3. use baz

**Creamos un usuario 'foo' y su contraseña 'bar123'**

4. db.createUser({user: "foo", pwd: "bar123", roles: [] })

**Creamos una colección llamada 'qux' en nuestra base de datos 'baz', e insertamos datos**.

5. db.qux.save({nombre: "Nic", apellido: "Raboy" })

#Finalmente, contesta a las siguientes preguntas:

**¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?**
>connect('baz', 'foo', 'bar123')

**¿Cómo puedo insertar este registro en la colección de qux creada previamente?**
>db.nombreColeccion.save({name: 'al', age: 18, status: 'D', groups: ['politics', 'news']})