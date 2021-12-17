# Ejercicio 1
* ¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.4 y que cumpla con los siguientes puntos?

docker run --name=mongo_db -d -p 27027:27027 -e USERNAME_MONGODB=foo -e MONGODB_PASSWORD=bar123 mongo:4.4

![Alt text](Ago-Dic-2021\aleman-ortiz-javier-eduardo\Screenshots\SS_1_E1.png)

![Alt text](Ago-Dic-2021\aleman-ortiz-javier-eduardo\Screenshots\SS_3_E1.png)

* ¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?

docker exec -it mongo_db mongo

* ¿Cómo puedo insertar este registro en la colección de qux creada previamente?

use baz
db.qux.save({name:"al", age:18, status:"D", groups:["politics","news"]})
db.qux.find()

![Alt text](Ago-Dic-2021\aleman-ortiz-javier-eduardo\Screenshots\SS_2_E1.png)

