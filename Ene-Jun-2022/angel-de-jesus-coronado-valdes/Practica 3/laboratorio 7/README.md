## LABORATORIO 7

Listamos los contenedores que tenemos con el comando: `sudo docker ps -a`, vemos los contenedores que se encuentra en nuestro equipo.

![](/imagenes/1.png)


1. Crea una nueva network utilizando el comando `docker network create app`.
   1. Una vez creada puedes verificar esta network con `docker network inspect app`.

![](/imagenes/2.png)
   
   
2. Crea un contenedor que ejecute Redis utilizando el comando `docker run -d -p 6379:6379 --network=app --name redis redis --protected-mode no`.

![](/imagenes/3.png)

   1. Vuelve a utilizar el comando `docker network inspect app`, ¿puedes ver como nuestro contenedor de Redis está conectado a nuestra red de `app`?.

![](/imagenes/4.png)
   
   
3. Clona el repositorio de <https://github.com/AnhellO/redispy>.

4. Construye la imágen de Python de la carpeta de `./app` con el comando `docker build -t miusario/redispy .`, donde `miusuario = tu usuario de docker-hub`.


5. Ahora procederemos a instanciar un contenedor nuevo con la imágen que creamos anteriormente utilizando el comando `docker run -d --network app --name redispy miusuario/redispy`.

![](/imagenes/5.png)


6. El nuevo container de Python debe de haber ejecutado el script correctamente. Para verificar esto puedes revisar los logs del contenedor con `docker logs redispy`. Deberías de ser capaz de ver los `print()` statements del script de `./app/app.py`, y entre en ellos algunos "fake emails" que se crearon gracias al paquete `faker` instalado dentro del contenedor de Python.

![](/imagenes/6.png)


7. Si quieres dar un paso más allá y verificar que los cambios se guardaron en tu contenedor de Redis, entonces puedes llevar a cabo alguno de los siguientes pasos:
   1. Instalar el [cliente CLI de redis](https://redis.io/topics/rediscli) en tu máquina local, y conectarte a tu instancia de Redis por medio de `redis-cli -h 0.0.0.0 -p 6379`. Ya dentro prueba a jugar con algunos comandos como `KEYS *` y luego `GET algun-hash-key` utilizando alguno de los hash values que salieron en el primer comando como parámetro, en vez de `algun-hash-key`.
   
   2. O bien, puedes conectarte al contenedor de `Redis` en ejecución con el comando `docker exec -it redis /bin/bash`, y ya dentro del mismo utilizar el comando `redis-cli` para conectarte a la instancia de Redis en ejecución. Intenta los mismos comandos propuestos en la 1er alternativa para verificarlo.
   
![](/imagenes/7.png)
   
Aprendi a como conectar contenedores por red y de ver y conocer la base de datos redis y como ejecutar un programa en python para hacer registros a redis.
   

