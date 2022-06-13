## LABORATORIO 1

Listamos los contenedores que tenemos con el comando: `sudo docker ps -a`, vemos los contenedores que se encuentra en nuestro equipo.

![](/imagenes/1.png)

1. Inicia container de MySQL: `docker run --name=db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret-pw -d mysql:8`, como se indica en el laboratorio.

![](/imagenes/2.png)

   1. Puedes conectarte al contenedor con `docker exec -it db bash` y luego conectarte a MySQL por medio del 	comando `mysql -u root -p`.

   2. Para salir de la terminal interactiva del contenedor, primero hay que salir de `MySQL` por medio de `exit`, y una vez fuera podemos tecler la combinación `Ctrl+P` y `Ctrl+Q` para salir. Esto no detendrá nuestro contenedor.
	
![](/imagenes/3.png)


2. Inicia container de `PHPMyAdmin`: `docker run --name=my-admin -p 82:80 --link db:db -d phpmyadmin`.

![](/imagenes/4.png)

   1. Podrás ver tu contenedor de `PHPMyAdmin` corriendo desde <http://localhost:82/>.
   2. Una vez ahí introduce las credenciales correctas para acceder y comenzar a jugar con tus contenedores.

![](/imagenes/5.png)

3. Una vez que hayas jugado un poco con los contenedores, asegúrate de detenerlos y borrarlos utilizando `docker stop` para detenerlos, y `docker rm` para removerlos.

![](/imagenes/6.png)

Es divertido crear los contenedores entendible y solo seria aprender más y más para facilitar la creación de contenedores una facil implementación.
