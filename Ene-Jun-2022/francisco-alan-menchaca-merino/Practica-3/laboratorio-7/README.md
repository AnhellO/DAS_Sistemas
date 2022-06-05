# Guía

Esta guía pretende mostrar un ejemplo sencillo de `docker networks` pero ahora conectando dos contenedores.

1. Crea una nueva network utilizando el comando `docker network create app`
   
   ![image](https://user-images.githubusercontent.com/71090472/172039674-e23f7bca-f18c-4674-80ca-39e9e2397282.png)
   
   1. Una vez creada puedes verificar esta network con `docker network inspect app`

      ![image](https://user-images.githubusercontent.com/71090472/172039681-4f3fd9b4-5e47-4577-9e8c-06c3ef354807.png)

2. Crea un contenedor que ejecute Redis utilizando el comando `docker run -d -p 6379:6379 --network=app --name redis redis --protected-mode no`
   
   ![image](https://user-images.githubusercontent.com/71090472/172039769-58ba0784-0e10-4270-81df-ed1ff3a2eb6a.png)
   
   1. Vuelve a utilizar el comando `docker network inspect app`, ¿puedes ver como nuestro contenedor de Redis está conectado a nuestra red de `app`?

      ![image](https://user-images.githubusercontent.com/71090472/172039807-fae951a2-6b7d-4b4d-9bd3-ecf3ca31f725.png)

3. Clona el repositorio de <https://github.com/AnhellO/redispy>

   ![image](https://user-images.githubusercontent.com/71090472/172039863-66d5ba04-dd43-47f1-980c-f398a2b984cf.png)

4. Construye la imágen de Python de la carpeta de `./app` con el comando `docker build -t miusario/redispy .`, donde `miusuario = tu usuario de docker-hub`

   ![image](https://user-images.githubusercontent.com/71090472/172039949-aa9708fc-eeb6-44f6-9bab-dbf261584606.png)

5. Ahora procederemos a instanciar un contenedor nuevo con la imágen que creamos anteriormente utilizando el comando `docker run -d --network app --name redispy miusuario/redispy`

   ![image](https://user-images.githubusercontent.com/71090472/172040012-1d0345df-b9f1-4416-8d62-a1ad465fd54a.png)

6. El nuevo container de Python debe de haber ejecutado el script correctamente. Para verificar esto puedes revisar los logs del contenedor con `docker logs redispy`. Deberías de ser capaz de ver los `print()` statements del script de `./app/app.py`, y entre en ellos algunos "fake emails" que se crearon gracias al paquete `faker` instalado dentro del contenedor de Python

   ![image](https://user-images.githubusercontent.com/71090472/172040498-accd7a05-74b3-46fd-92a4-862a08ed856e.png)

7. Si quieres dar un paso más allá y verificar que los cambios se guardaron en tu contenedor de Redis, entonces puedes llevar a cabo alguno de los siguientes pasos:
   1. Instalar el [cliente CLI de redis](https://redis.io/topics/rediscli) en tu máquina local, y conectarte a tu instancia de Redis por medio de `redis-cli -h 0.0.0.0 -p 6379`. Ya dentro prueba a jugar con algunos comandos como `KEYS *` y luego `GET algun-hash-key` utilizando alguno de los hash values que salieron en el primer comando como parámetro, en vez de `algun-hash-key`
   2. O bien, puedes conectarte al contenedor de `Redis` en ejecución con el comando `docker exec -it redis /bin/bash`, y ya dentro del mismo utilizar el comando `redis-cli` para conectarte a la instancia de Redis en ejecución. Intenta los mismos comandos propuestos en la 1er alternativa para verificarlo

   ![image](https://user-images.githubusercontent.com/71090472/172041206-74aea25f-6d0b-4318-91f2-6d36c3d40140.png)

   ![image](https://user-images.githubusercontent.com/71090472/172041292-5b523144-61c2-4eaf-872b-586653e9cfd0.png)

## Recursos

- <https://redis.io/>
- <https://hub.docker.com/_/redis>
- <https://hub.docker.com/_/python>
- <https://faker.readthedocs.io/en/master/>
- <https://pypi.org/project/redis/>
