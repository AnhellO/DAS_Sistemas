## LABORATORIO 12

Listamos los contenedores que tenemos con el comando: `sudo docker ps -a`, vemos los contenedores que se encuentra en nuestro equipo.

![](/imagenes/1.png)


1. Un contenedor que maneja el frontend de la app y que utiliza `Flask`. Este interactua con el contenedor de la base de datos para obtener los registros guardados en la DB por medio del contenedor 2.


2. Este contenedor corre un script de python que se conectará con la API de gatitos para obtener múltiples registros, almacenándolos en la base de datos.


3. Este contenedor corre la base de datos en `PostgreSQL` e inicializa la única tabla que se utiliza en la DB por medio del archivo [init.sql](db/init.sql).


4. Ejecuta un servidor de `PgAdmin` que se conecta con la base de datos y que funge como DBMS de la aplicación.



1. Ejecuta el comando `docker-compose up -d --build` y espera a que los contenedores estén listos.

![](/imagenes/2.png)

   1. Puedes verificar los contenedores en ejecución individualmente utilizando el comando `docker logs <nombre-del-container>`.

![](/imagenes/3.png)

   2. El contenedor 2 debería de estar arriba solamente por un tiempo en específico (el tiempo que tarde en "_crawlear_" la API pública) y después debería de detenerse.
   
   
2. Visita la app por medio de la URL <http://0.0.0.0:5000/>. Puedes interactuar con los siguientes endpoints de la aplicación tanto por `GET` requests como por `POST` requests: `/hello` y `/my-cats`. Échale un vistazo al archivo [`app.py`](app/app.py) para mayor detalle :wink:
   1. Deberías de poder ver **10** gatos existentes en la DB por medio de la URL <http://0.0.0.0:5000/my-cats>. Estos fueron los que se crearon gracias al contenedor 2.
   2. Recuerda que puedes utilizar clientes como `cURL`, `Postman` o `Insomnia` para llevar a cabo esta interacción :wink:
   3. Juega un poco con la aplicación y haz ajustes a diestra y siniestra. Si quisieras ver algún cambio en específico reflejado en la app en ejecución (por ejemplo en el frontend, o volver a correr el [`scraper`](app/scraper.py) pero con más registros) basta con aplicar los cambios a los archivos y reiniciar el contenedor que contiene esos archivos por medio del comando `docker restart <nombre-del-container>`. Podrás ver estos cambios reflejados sin tener que detener los demás contenedores y sobre todo sin tener que reconstruir todas las imágenes gracias a los [bind mounts de docker](https://docs.docker.com/storage/bind-mounts/).
   
   
3. Una vez que te sientas listo, recuerda utilizar `docker-compose down` para detener y borrar todos los contenedores en ejecución.


Aprendí a utilizar nuevas librerias y a orquestar 4 contenedores de los cuales ya se va viendo una conexión de una app del como es que se ve mediante el proceso de peticiones tipo POST GET HTTP de una API.

