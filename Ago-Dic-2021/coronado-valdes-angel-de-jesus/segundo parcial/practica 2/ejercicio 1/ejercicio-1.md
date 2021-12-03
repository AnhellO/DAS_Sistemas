# Ejercicio 1
¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.4 y que cumpla con los siguientes puntos?
- **Que el contenedor se llame mongo_db**
- **Que el contenedor se mantenga en ejecución**
- **Que el puerto asignado a la máquina host sea el 27027**
- **Que el usuario sea foo**
- **Que el password sea bar123**
- **Que se cree una base de datos llamada baz**
- **Que se cree una colección en la base de datos de baz llamada qux**
- **¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo      dentro de mi contenedor de mongo_db?**
- **¿Cómo puedo insertar [este registro](https://github.com/AnhellO/DAS_Sistemas/blob/development/Ago-Dic-2021/Pr%C3%A1cticas/2do%20Parcial/Pr%C3%A1ctica%202/mongodb-registro.png) en la colección de qux creada previamente?**
___
## Solución ##
>*Por medio de este comando listamos los contenedores que se encuentra en ejecución ver contenedores en ejecucion.*
- **$ sudo docker ps -a**

>*Con este comando creamos el contenedor de mongodb con su user y pass, con la version especificada con la comunicación con sus respectivos puestos.*
- **$ sudo docker run -d -p 27027:27027 --name mongo_db -e MONGODB_USER="foo" -e MONGODB_PASS="bar123" mongo:4.4**

>*Volvemos a listar los contenedores.*
- **$ sudo docker ps -a**

>*Usando la siguiente line de comando ejecutamos el contenedor donde mensionamos el nombre del contenedor y le decimos que nos abra una sesión una terminal.*
- **$ sudo docker exec -it mongo_db /bin/bash**

>*Dentro de la session o terminal del contenedor entramos a mongodb por medio del comando "mongo".*
- **root@6f86d308d77a:/# mongo**

>*Dentro del CLI de mongo listamos las bases de datos po medio del siguiente comando "show dbs".*
- **> show dbs**

>*Usando el comando "use (nameDatabase)" se usa la base de datos con el nombre puesto en el comando, si no existe se creara.*
- **> use baz**

>*Con este comando insertamos datos en la colección "qux" y "insertOne" se inserta un solo registro.*
- **> db.qux.insertOne({name:"al",age:18,status:"D",goups:["politics","news"]})**

>*Mostramos la colección donde "db" indica la base de datos actual, "qux" la colección y "find({})" muestra todo el contenido de la colección.*
> db.qux.find({})

**¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?**
> *Dentro de la session o terminal del contenedor entramos a mongodb.*
- **root@6f86d308d77a:/# mongo**

**¿Cómo puedo insertar este registro en la colección de qux creada previamente?**
>*insertamos datos en la colección.*

- **> db.qux.insertOne({name:"al",age:18,status:"D",goups:["politics","news"]})**

>*Con el comando "db" hace referencia a la base de datos que estemos usando "qux" se crea si es que no exite "insertOne" me inserta un objeto a la base de datos.
___
## Imagenes del Ejercicio ##
![Creación del contenedor y la ejecución del contenedor](1.1.png)
![Iniciando los comandos de la base de datos](3.3.png)


