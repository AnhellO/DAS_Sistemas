Crea un volumen que se llame redis_volume y que utilice el driver por default para los Docker volumes.

Para crear un volumen, se corre el siguiente comando:
- sudo docker volume create redis_volume

Ejecuta un contenedor de Redis similar a los del ejercicio anterior pero ahora montándole el volúmen que acabas de crear en el paso anterior.

Para crear un contenedor con redis, se corre el siguiente comando:
- sudo docker run -d -p 6379:6379 -v redis_volume --network ejercicio3 --name redis_db1 redis --protected-mode no

Crea un Dockerfile que cumpla con los siguientes requisitos:

Que extienda de la imágen base de Python3
----YA
Que utilice el directorio /app como el directorio de trabajo
----YA
Que instale todas las dependencias necesarias para este ejercicio por medio de pip
----YA
Que monte el volumen de redis_volume creado previamente
----YA
Y finalmente que ejecute un script de Python el cual inserte los registros del archivo mock_data.json en el servidor de Redis uno por uno de la siguiente forma
{id}-{first_name}-{last_name} como llave
json_record como valor
----YA
Por ejemplo, si insertáramos el 1er registro del archivo JSON en el server de Redis de acuerdo al criterio anterior entonces esto luciría así a través de una simple instrucción en Redis: SET 1-Adelice-Castillon '{"id":1,"first_name":"Adelice","last_name":"Castillon","email":"acastillon0@intel.com","gender":"Male","ip_address":"110.188.66.73","school_number":"ca2bae7e-c200-4c5b-97ba-f14407cb19c5"}'
----YA
Es completamente opcional crear un contenedor con Redis Commander para revisar los resultados en el contenedor de Redis

Para construir el dockerfile, se corre el siguiente comando:
- sudo docker build -t hiroshigk/redis_json .

Y para hacer push a la iamgen creada, se corre el siguiente comando:
- d push hiroshigk/redis_json

Link para ver la imagen en mi perfil de docker:
- https://hub.docker.com/repository/docker/hiroshigk/redis_json

Y para crear un contenedor con la imagen creada, se corre el siguiente comando:
- sudo docker run -d --network ejercicio3 --name ejercicio3 hiroshigk/redis_json
