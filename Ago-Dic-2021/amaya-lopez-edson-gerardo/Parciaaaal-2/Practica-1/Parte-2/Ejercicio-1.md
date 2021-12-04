

`HELP.md`

### ¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.4 y que cumpla con los siguientes puntos?

- Que el contenedor se llame mongo_db
- Que el contenedor se mantenga en ejecución
- Que el puerto asignado a la máquina host sea el 27027
- Que el usuario sea foo
- Que el password sea bar123
- Que se cree una base de datos llamada baz
- Que se cree una colección en la base de datos de baz llamada qux


```docker
docker run -d -p 27027:27027 --name mongo_db -e MONGODB_INITDB_ROOT_USERNAME=foo -e MONGODB_INITDB_ROOT_PASSWORD=bar123 mongo:4.4
```



### ¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?
```docker
docker exec -it mongo_db mongo
```

### ¿Cómo puedo insertar este registro en la colección de qux creada previamente?
> use baz

> db.qux.save({name: "al", age: 18, status:"D",
    groups:["politics","news"]})
> db.qux.find()


![contenedor mongo](img\mongo.jpeg)
![mongoDB](img\mongoClient.jpeg)
![Find](img\MongoFind.jpeg)




