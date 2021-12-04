<h1>Ejercicio 1</h1>
<h2>¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.4 y que cumpla con los siguientes puntos?</h2>
<br>
<h3>Que el contenedor se llame mongo_db</h3>
<p>R = --name mongo_db</p>
<br>
<h3>Que el contenedor se mantenga en ejecución</h3>
<p>R = docker run</p>
<br>
<h3>Que el puerto asignado a la máquina host sea el 27027</h3>
<p>R = -p 27027:27027</p>
<br>
<h3>Que el usuario sea foo</h3>
<p>R = MONGODB_INITDB_ROOT_USERNAME=foo</p>
<br>
<h3>Que el password sea bar123</h3>
<p>R =  MONGODB_INITDB_ROOT_PASSWORD=bar123</p>
<br>
<h3>Que se cree una base de datos llamada baz</h3>
<p>R = use baz</p>
<br>
<h3>Que se cree una colección en la base de datos de baz llamada qux</h3>
<p>R = db.qux</p>
<br>
<h3>¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?</h3>
<p>R = docker exect -it mongo_db bash (Para ejecutar mongo) mongo (para inicializar mongo) </p>
<br>
<h3>¿Cómo puedo insertar este registro en la colección de qux creada previamente?</h3>
<p>R = db.qux.insertOne({
name: "al",
age: 18,
status: "D",
groups: ["politics", "news"]
}
)</p>
<br>
