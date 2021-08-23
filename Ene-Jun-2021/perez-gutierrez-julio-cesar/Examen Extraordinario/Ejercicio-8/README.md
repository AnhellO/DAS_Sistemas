¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MySQL versión 8 y que cumpla con los siguientes puntos?

- Que el contenedor se llame database_mysql
- Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)
- Que el puerto asignado a la máquina host sea el 4444
- Que el usuario sea extra
- Que el password sea ordinario123!
- Que se cree una base de datos llamada pruebas

docker network create red_mysql

docker run --name database_mysql -p 4444:3306 --network=red_mysql -e MYSQL_ROOT_PASSWORD=ordinario123! -e MYSQL_USER=extra -e MYSQL_PASSWORD=ordinario123! -e MYSQL_DATABASE=pruebas -d mysql:8

¿Con qué comando(s) puedo conectarme a mi base de datos de MySQL corriendo dentro de mi contenedor de database_mysql?

docker exec -it database_mysql bash 

mysql -u extra -h 127.0.0.1 -p

show databases;

Finalmente, ¿qué comando necesito utilizar para ejecutar un contenedor de adminer que funja como DBMS y que se conecté a la base de datos de MySQL creada previamente?

docker run --network=red_mysql -p 8080:8080 adminer

