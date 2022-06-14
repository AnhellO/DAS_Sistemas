# Guía

Esta guía parte de la solución de la tarea propuesta en la 2da sesión, pero utiliza el concepto de `docker networks` para comunicar los contenedores entre si.

También cambiaremos de utilizar el cliente de [`PHPMoAdmin`](https://hub.docker.com/r/thinkcube/phpmoadmin) a utilizar el de [`Mongo-Express`](https://hub.docker.com/_/mongo-express).

Vamos a partir de la solución propuesta, pero aplicando algunos cambios menores.

- Comenzamos por crear una network custom con el comando `docker network create lab6`

  ![image](https://user-images.githubusercontent.com/71090472/172038409-4c317dc4-8001-495d-b579-f14c543a68ef.png)

- Vamos a ejecutar el contenedor de `MongoDB`, pero ahora montándolo sobre nuestra nueva red: `docker run -d -p 27017:27017 --name m1 --network lab6 mongo`

  ![image](https://user-images.githubusercontent.com/71090472/172038529-c7427b80-a38f-4e46-a91d-a6adcb8857e7.png)

- Procedemos a ejecutar el contenedor de `Mongo Express` con el siguiente comando: `docker run -d --name moexpress --network lab6 -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=admin -e ME_CONFIG_BASICAUTH_PASSWORD=karlitabb -p 8081:8081 mongo-express`

  ![image](https://user-images.githubusercontent.com/71090472/172038750-3893cb87-cfb6-43a5-897c-5314fe08f87c.png)

  - Puedes visitar el cliente DBMS en la URL <http://localhost:8081//>

    ![image](https://user-images.githubusercontent.com/71090472/172038759-52882ee2-5ffe-4a98-b3be-9a25b508a432.png)

- Después de tener nuestros dos contenedores iniciales de `Mongo` y del cliente de `Mongo Express` en ejecución, vamos a construir una imagen taggeada específicamente para este laboratorio con la cual ejecutaremos la solución propuesta en `GO` para que se conecté con el contenedor de mongo, pero ahora por medio de la docker network custom que hemos creado
  - Construimos la imagen con el comando `docker build -t lab6 .`

    ![image](https://user-images.githubusercontent.com/71090472/172039289-f94c4e19-1067-445e-896a-8c52336e5b6f.png)

  - Instanciamos un contenedor de la imagen construída previamente con el comando `docker run -d --network lab6 --name mongogo lab6`

    ![image](https://user-images.githubusercontent.com/71090472/172039317-e81ffb74-ad83-45a9-9805-c4f6eee19477.png)

  - Visita el cliente de `Mongo Express` para poder ver los cambios reflejados

    ![image](https://user-images.githubusercontent.com/71090472/172039387-5c137bc9-21ac-4e54-ba0d-bcedae8411f0.png)

## Recursos

- <https://docs.docker.com/network/>
- <https://hub.docker.com/_/mongo-express>
