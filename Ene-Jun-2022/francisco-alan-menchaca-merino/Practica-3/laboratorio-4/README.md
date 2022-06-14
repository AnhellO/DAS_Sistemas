# Guía

Esta guía parte del [`laboratorio-1`](../laboratorio-1/) de Docker, pero ahora añadiendo la lógica para volúmenes.

1. Crea un par de volumenes para `MySQL` y para `PHPMyAdmin` respectivamente por medio de los siguientes comandos `docker volume create mysql-volume` y `docker volume create phpmyadmin-volume`

   ![image](https://user-images.githubusercontent.com/71090472/172034766-01e9c685-a886-4dfd-9c34-89877af7b412.png)
   

2. Vuelve a crear los contenedores de `MySQL` y de `PHPMyAdmin` con los mismos comandos utilizados anteriormente, pero ahora añadiendo la opción `-v` a cada comando de `docker run`, asociándolo a su respectivo volumen. Los comandos quedarían de la siguiente manera:
   1. `docker run --name=db -p 3306:3306 -v mysql-volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8`
   2. `docker run --name=my-admin -p 82:80 -v phpmyadmin-volume:/etc/phpmyadmin/config.user.inc.php --link db:db -d phpmyadmin`

   ![image](https://user-images.githubusercontent.com/71090472/172034740-8ea0a911-d37c-4fb7-b058-c4d866d932f3.png)
   
3. Crea una nueva base de datos con algunas tablas y registros por medio del contenedor de `MySQL` y el cliente CLI de `MySQL` dentro del mismo, o bien, por medio de la interfaz de `PHPMyAdmin` a través de <http://localhost:82/>

   ![image](https://user-images.githubusercontent.com/71090472/172034928-f7b9d266-11b5-40a8-803c-5257d19b4ceb.png)

4. Una vez que confirmes que los registros que agregaste existen en la DB, procede a detener y a borrar los contenedores en ejecución utilizando los siguientes comandos
   1. `docker stop db my-admin`
   2. `docker rm db my-admin`

   ![image](https://user-images.githubusercontent.com/71090472/172034968-f40bd2ce-f6ff-4694-bc92-c3cbfd63c4d9.png)

5. Utiliza `docker volume ls` para poder revisar los volumenes existentes, ¿ves cómo estos siguen ahí a pesar de que tus contenedores ya no lo están?

   ![image](https://user-images.githubusercontent.com/71090472/172034990-5917bc62-b33e-4b97-9c11-942ca84d4212.png)

6. Vuelve a crear los contenedores de `MySQL` y de `PHPMyAdmin` con los mismos comandos utilizados anteriormente en el paso 1 de esta guía, asegurándote de montar los volúmenes a los mismos

   ![image](https://user-images.githubusercontent.com/71090472/172035000-df9c8ff0-b3e9-4894-a295-a576fc14fb72.png)

7. Revisa tu base de datos de `MySQL`, ¿puedes ver cómo tus datos siguen en existencia después de haber sido persistidos en su respectivo volumen?

   ![image](https://user-images.githubusercontent.com/71090472/172035022-098e960d-41e9-45aa-ac63-b4daf134092d.png)

## Recursos

- <https://docs.docker.com/storage/volumes/>
- <https://docs.docker.com/storage/bind-mounts/>
- <https://docs.docker.com/storage/tmpfs/>
