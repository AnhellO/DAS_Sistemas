Ejercicio 3

1.- Crea un volumen que se llame redis_volume y que utilice el driver por default para los Docker volumes.

2.- Ejecuta un contenedor de Redis similar a los del ejercicio anterior pero ahora montándole el volúmen que acabas de  crear en el paso anterior.

3.- Crea un Dockerfile que cumpla con los siguientes requisitos:

4.- Que extienda de la imágen base de Python3

5.- Que utilice el directorio /app como el directorio de trabajo

6.- Que instale todas las dependencias necesarias para este ejercicio por medio de pip

7.- Que monte el volumen de redis_volume creado previamente Y finalmente que ejecute un script de Python el cual inserte los registros del archivo mock_data.json en el servidor de Redis uno por uno de la siguiente forma
{id}-{first_name}-{last_name} como llave
json_record como valor
Por ejemplo, si insertáramos el 1er registro del archivo JSON en el server de Redis de acuerdo al criterio anterior entonces esto luciría así a través de una simple instrucción en Redis: SET 1-Adelice-Castillon '{"id":1,"first_name":"Adelice","last_name":"Castillon","email":"acastillon0@intel.com","gender":"Male","ip_address":"110.188.66.73","school_number":"ca2bae7e-c200-4c5b-97ba-f14407cb19c5"}'
Es completamente opcional crear un contenedor con Redis Commander para revisar los resultados en el contenedor de Redis

COMANDOS:

ACCEDER A LA DIRECCIÓN DONDE SE ENCUENTRA EL DOCKERFILE
    CD C:\Users\brand\OneDrive\Escritorio\BREND ESCUELA 2\7 semestre\DISEÑO Y ARQUITECTURA\PARCIAL 2\Segundo_Parcial\Parte3

CREAR UNA NUEVA NETWORK
     docker network create Par2Pr3

CREAR VOLUMEN 
     docker volume create redis_volume

CREAR CONTENEDOR APARTIR DE VOLUMEN YA CREADO, ASIGNANDO UN PUERTO
     docker run -d -p 6379:6379 -v redis_volume --network Par2Pr3 --name redis_db1 redis --protected-mode no

CREAR IMAGEN A USUARIO DE DOCKER HUB
     docker build -t brend303/redis_json .

SUBIR A DOCKERFILE
     docker push brend303/redis_json

CONTENEDOR REDIS 
    docker run -d --network ejercicio3 --name ejercicio3 brend303/redis_json

DOCKER HUB
     docker pull brend303/redis_json    