## LABORATORIO 6

Listamos los contenedores que tenemos con el comando: `sudo docker ps -a`, vemos los contenedores que se encuentra en nuestro equipo.

![](/imagenes/1.png)


También cambiaremos de utilizar el cliente de [`PHPMoAdmin`](https://hub.docker.com/r/thinkcube/phpmoadmin) a utilizar el de [`Mongo-Express`](https://hub.docker.com/_/mongo-express).

Vamos a partir de la solución propuesta, pero aplicando algunos cambios menores.

- Comenzamos por crear una network custom con el comando `docker network create lab6`.

![](/imagenes/2.png)


- Vamos a ejecutar el contenedor de `MongoDB`, pero ahora montándolo sobre nuestra nueva red: `docker run -d -p 27017:27017 --name m1 --network lab6 mongo`.

![](/imagenes/3.png)


- Procedemos a ejecutar el contenedor de `Mongo Express` con el siguiente comando: `docker run -d --name moexpress --network lab6 -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=admin -e ME_CONFIG_BASICAUTH_PASSWORD=karlitabb -p 8081:8081 mongo-express`.

![](/imagenes/4.png)


  - Puedes visitar el cliente DBMS en la URL <http://0.0.0.0:8081/>.

![](/imagenes/5.png)

  
- Después de tener nuestros dos contenedores iniciales de `Mongo` y del cliente de `Mongo Express` en ejecución, vamos a construir una imagen taggeada específicamente para este laboratorio con la cual ejecutaremos la solución propuesta en `GO` para que se conecté con el contenedor de mongo, pero ahora por medio de la docker network custom que hemos creado.
  - Construimos la imagen con el comando `docker build -t lab6 .`.
  
  - Instanciamos un contenedor de la imagen construída previamente con el comando `docker run -d --network lab6 --name mongogo lab6`.
  
![](/imagenes/6.png)

  
  - Visita el cliente de `Mongo Express` para poder ver los cambios reflejados


Ví como se ejecutan comando de go en una red de docker creo que se facilita más al trabajar con docker.

