¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MySQL versión 8 y que cumpla con los siguientes puntos?

    Que el contenedor se llame mysql_db
    Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)
    Que el puerto asignado a la máquina host sea el 4000
    Que el usuario sea foo
    Que el password sea bar123
    Que se cree una base de datos llamada baz

- docker run --name=mysql_db -d -p 4000:3306 -e MYSQL_ROOT_PASSWORD=bar123 -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz mysql:8

Finalmente, ¿con qué comando(s) puedo conectarme a mi base de datos de MySQL corriendo dentro de mi contenedor de mysql_db?
- sudo docker exec -ti mysql_db mysql -u foo -p

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

Comandos:
- sudo docker run --name=mysql_db -d -p 4000:3306 -e MYSQL_ROOT_PASSWORD=bar123 -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz mysql:8

- sudo docker ps

- sudo docker exec -ti mysql_db mysql -u foo -p

- SHOW DATABASES; (dentro del contenedor)
