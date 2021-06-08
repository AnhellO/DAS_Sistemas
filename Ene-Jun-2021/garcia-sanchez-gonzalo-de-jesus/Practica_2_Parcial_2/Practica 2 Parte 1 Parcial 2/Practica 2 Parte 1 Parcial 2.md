# **Parte 1**


####**¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MySQL versión 8 y que cumpla con los siguientes puntos?**
-   docker run --name=mysql_db -p 4000:3306 -e MYSQL_ROOT_PASSWORD=bar123 -d mysql:8
    docker exec -it mysql_db mysql -uroot -p

####**Que el contenedor se llame mysql_db**
-   docker run **--name=mysql_db** -p 4000:3306 -e MYSQL_ROOT_PASSWORD=bar123 -d mysql:8

####**Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)**
-   docker run --name=mysql_db -p 4000:3306 -e MYSQL_ROOT_PASSWORD=bar123 **-d** mysql:8
-   -d indica que el contenedor permanecerá corriendo en segundo plano.

####**Que el puerto asignado a la máquina host sea el 4000**
-   docker run --name=mysql_db -p **4000:3306** -e MYSQL_ROOT_PASSWORD=bar123 -d mysql:8
-   -p 4000:3306 conecta el puerto 33061 de nuestro sistema operativo con el puerto 3306 del contenedor.

####**Que el usuario sea foo**
-   -u FOO
####**Que el password sea bar123**
-   docker run --name=mysql_db -p 4000:3306 -e **MYSQL_ROOT_PASSWORD=bar123** -d mysql:8
-   -e MYSQL_ROOT_PASSWORD=bar123asigna la contraseña "secret" al usuario "foo" de MySQL, -e sirve para configurar variables de entorno.

####**Que se cree una base de datos llamada baz**
####**¿con qué comando(s) puedo conectarme a mi base de datos de MySQL corriendo dentro de mi contenedor de mysql_db?**
  
**Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.**