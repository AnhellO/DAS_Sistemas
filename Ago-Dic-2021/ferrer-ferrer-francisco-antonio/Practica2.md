# Ejercicio 1
¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de Docker que corra un servidor de MongoDB versión 4.4 y que cumpla con los siguientes puntos?

<docker run -dp 27027:27027 --name mongo_db -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 mongo>

Que el contenedor se llame mongo_db
Que el contenedor se mantenga en ejecución
Que el puerto asignado a la máquina host sea el 27027
Que el usuario sea foo
Que el password sea bar123
Que se cree una base de datos llamada baz
Que se cree una colección en la base de datos de baz llamada qux


¿Con qué comando(s) puedo conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db?
 
<docker exec -it mongo_db /bin/bash>

¿Cómo puedo insertar este registro en la colección de qux creada previamente?

mongo
<use baz>
<db.qux.InsertOne({name: "all", age:18, status:"D", groups:["politics", "news"]})>

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.



# Ejercicio 2
Crea 4 contenedores por medio del cliente CLI de docker:

El 1er contenedor ejecutará un primer servidor de Redis y su nombre deberá de ser redis1
El 2do contenedor ejecutará un segundo servidor de Redis y su nombre deberá de ser redis2
El 3er contenedor ejecutará un tercer servidor de Redis y su nombre deberá de ser redis3
El 4to contenedor deberá de ejecutar un servidor de Redis Commander el cual estará protegido con el usuario DASistemas y la contraseña Ya-Casi-Se-Acaba-El-Semestre! para poder acceder a él. El contenedor debe de llamarse redis_dbms y tendrá que conectarse con todos los contenedores de Redis que se crearon en los pasos previos
Verifica que puedes acceder correctamente a la interfaz de Redis Commander y que los 3 contenedores de Redis son accesibles desde el DBMS.

Nota: También puedes resolver este ejercicio por medio de Docker Compose.

<servidores>
 docker run -dp 1234:6379 --name redis1 Redis
 docker run -dp 1235:6379 --name redis2 Redis
 docker run -dp 1236:6379 --name redis3 Redis


<docker run -dp 8081:8081 --name redis_dbms -e HTTP_USER=DASistemas -e HTTP_PASSWORD=Ya-Casi-Se-Acaba-El-Semestre! rediscommander/redis-commander REDIS_HOSTS=redis1,redis2,redis3> 

<<<<<<<<Incompleto>>>>>>>>
No se que sigue de aqui xd


# Ejercicio 3
Crea un volumen que se llame redis_volume y que utilice el driver por default para los Docker volumes.

Ejecuta un contenedor de Redis similar a los del ejercicio anterior pero ahora montándole el volúmen que acabas de crear en el paso anterior.

Crea un Dockerfile que cumpla con los siguientes requisitos:

Que extienda de la imágen base de Python3
Que utilice el directorio /app como el directorio de trabajo
Que instale todas las dependencias necesarias para este ejercicio por medio de pip
Que monte el volumen de redis_volume creado previamente
Y finalmente que ejecute un script de Python el cual inserte los registros del archivo mock_data.json en el servidor de Redis uno por uno de la siguiente forma
{id}-{first_name}-{last_name} como llave
json_record como valor
Por ejemplo, si insertáramos el 1er registro del archivo JSON en el server de Redis de acuerdo al criterio anterior entonces esto luciría así a través de una simple instrucción en Redis: SET 1-Adelice-Castillon '{"id":1,"first_name":"Adelice","last_name":"Castillon","email":"acastillon0@intel.com","gender":"Male","ip_address":"110.188.66.73","school_number":"ca2bae7e-c200-4c5b-97ba-f14407cb19c5"}'
Es completamente opcional crear un contenedor con Redis Commander para revisar los resultados en el contenedor de Redis
Construye una imágen basada en el Dockerfile que acabas de crear y llámala {mi-user}/redis_json, donde {mi-user} equivale a tu usuario de DockerHub. Una vez que hayas creado la imagen envíala a tu cuenta de DockerHub. Debe de estar accesible similar a como lo está en este ejemplo. Asegúrate de adjuntar el link a ella en tus resultados del ejercicio.

Para finalizar, ejecuta un nuevo contenedor basado en la imágen recién creada que se llame redis_json_py que sirva como muestra de que tu script y tu imagen funcionan correctamente.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.