
# Práctica 2 - Parte 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MySQL versión 8 y que cumpla con los siguientes puntos?

- docker run --name mysql_db -p 4000:3306 -e MYSQL_ROOT_USER=foo -e MYSQL_ROOT_PASSWORD=bar123 -d mysql:8 (crear contenedor con el nombre de mysql_db, en el puerto 4000 de la máquina local, se instanciaron variables de ambiente para  (usuario y contraseña), corre en el background y mysql tiene la versión 8)

¿con qué comando(s) puedo conectarme a mi base de datos de MySQL corriendo dentro de mi contenedor de mysql_db?
-  docker exec -it mysql_db  bash ( conectarme al contenedor)
- which mysql
- mysql -u root -p (conecta con mysql)
- ingresa contraseña (bar123)
  

Se usaron los sig comandos:
- sudo docker logs mysql_db (revisar los logs del contenedor  de mysql)
- exit (salir de la terminal iterativa)
- show databases (muestra base de datos existentes)
- use  practica_2 ( utilizará la base de datospractica 2)
- create table persona (int id, nombre varchar(10)) (crea tabla con dos campos)
- insert into persona values (1,'juania')(insertar datos a la tabla)
- select * from persona (mostrará ñps datos de la tabla persona)
- truncate table persona (vaciar  la tabla de persona )
- show tables from database (ver tablas de la base de datos)
- sudo docker stop $(sudo docker stop ps -q -a)( detener contenedores)
- sudo docker rm $(sudo docker ps -q -a ) (eliminar los contenedires existentes)