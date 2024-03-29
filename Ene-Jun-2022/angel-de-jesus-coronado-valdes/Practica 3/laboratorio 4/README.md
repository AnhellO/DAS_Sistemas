## LABORATORIO 4

Listamos los contenedores que tenemos con el comando: `sudo docker ps -a`, vemos los contenedores que se encuentra en nuestro equipo.

![](/imagenes/1.png)


1. Crea un par de volumenes para `MySQL` y para `PHPMyAdmin` respectivamente por medio de los siguientes comandos `docker volume create mysql-volume` y `docker volume create phpmyadmin-volume`.

![](/imagenes/2.png)


2. Vuelve a crear los contenedores de `MySQL` y de `PHPMyAdmin` con los mismos comandos utilizados anteriormente, pero ahora añadiendo la opción `-v` a cada comando de `docker run`, asociándolo a su respectivo volumen. Los comandos quedarían de la siguiente manera:
   1. `docker run --name=db -p 3306:3306 -v mysql-volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8`.
   2. `docker run --name=my-admin -p 82:80 -v phpmyadmin-volume:/etc/phpmyadmin/config.user.inc.php --link db:db -d phpmyadmin`.

![](/imagenes/3.png)
   
   
3. Crea una nueva base de datos con algunas tablas y registros por medio del contenedor de `MySQL` y el cliente CLI de `MySQL` dentro del mismo, o bien, por medio de la interfaz de `PHPMyAdmin` a través de <http://localhost:82/>.

![](/imagenes/4.png)


4. Una vez que confirmes que los registros que agregaste existen en la DB, procede a detener y a borrar los contenedores en ejecución utilizando los siguientes comandos.
   1. `docker stop db my-admin`.
   2. `docker rm db my-admin`.

   
5. Utiliza `docker volume ls` para poder revisar los volumenes existentes, ¿ves cómo estos siguen ahí a pesar de que tus contenedores ya no lo están?.


6. Vuelve a crear los contenedores de `MySQL` y de `PHPMyAdmin` con los mismos comandos utilizados anteriormente en el paso 1 de esta guía, asegurándote de montar los volúmenes a los mismos.

7. Revisa tu base de datos de `MySQL`, ¿puedes ver cómo tus datos siguen en existencia después de haber sido persistidos en su respectivo volumen?

![](/imagenes/5.png)


Lo que aprendí hoy fue que gracias a los volumenes en docker podemos recuperar datos almacenados en una base de datos y esto con la finalidad de que por alguna razón borramos por accidente un contenedor, no nos preocupemos ya que con los volumenes podemos obtener nuestros datos.
