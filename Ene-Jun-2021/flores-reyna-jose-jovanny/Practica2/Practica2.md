# Practica 2 - Parte 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MySQL versión 8 y que cumpla con los siguientes puntos?

Que el contenedor se llame mysql_db
Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)
Que el puerto asignado a la máquina host sea el 4000
Que el usuario sea foo
Que el password sea bar123
Que se cree una base de datos llamada baz

Con el comando: docker run --name=mysql_db -p 4000:4000 -e MYSQL_ROOT_PASSWORD=secret-pw -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_NAME=baz -d mysql:8

Finalmente, ¿con qué comando(s) puedo conectarme a mi base de datos de MySQL corriendo dentro de mi contenedor de mysql_db?

Se puede conectar al contenedor con el siguiente comando docker exec -it mysql_db bash y luego a MySQL por medio del comando mysql -u root -p

Parte 2
Crea 2 contenedores por medio del cliente CLI de docker:

El 1er contenedor ejecutará un servidor de MongoDB y su nombre deberá de ser m1
El 2do contenedor ejecutará un cliente de Mongo Express el cual se llame mexpress y que se conectará al contenedor m1 creado en el punto anterior. Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:
Usuario: DAS
Password: abcde123?!

Comenzaremos creando una network custom con el comando: "docker network create parte2" luego vamos a jecutar el contedor MongoDB, conectandolo a nuestra red con el comando: "docker run -d -p 27017:27017 --name m1 --network parte2 mongo"

Procedemos a ejecutar el contenedor Mongo Express con el comando: "docker run -d --name mexpress --network parte2 -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=DAS -e ME_CONFIG_BASICAUTH_PASSWORD=abcde123?! -p 8081:8081 mongo-express

Crea 3 contenedores por medio del cliente CLI de docker:

El 1er contenedor ejecutará un servidor de MongoDB y su nombre deberá de ser mongo
El 2do contenedor deberá de ejecutar un servidor de Redis y su nombre deberá de ser redis
El 3er contenedor deberá de ejecutar un script de Python que cumpla con los siguientes criterios:
Que genere 1000 números aleatorios en el rango de [1000, 1000000]
Que inserte los números pares en el contenedor de mongo
Que inserte los números impares en el contenedor de redis
Para este contenedor en específico tendrás que construir una imágen por medio de un nuevo Dockerfile
Asegúrate de probar que todo funciona correctamente y de que el 3er contenedor puede conectarse a los otros dos contenedores sin problema alguno.

Comenzamos creando nuestra network custom con el comando: "docker network create parte3", para ejecutar un servidor redis utilizamos el comando: "docker run -d -p 6379:6379 --network=parte3 --name redis redis --protected-mode no". Podemos verificar nuestra network con el comando: "docker network inspect parte3"