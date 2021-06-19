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

Comandos:
cd "C:\Users\lulif\Documents\DAS_Sistemas\Ene-Jun-2021\flores-escalante-lucely-liliana\Segundo Parcial\Ejercicio 3"
docker network create p2e3
docker volume create redis_volume
docker run -d -p 6379:6379 -v redis_volume --network P2E3 --name redis_db1 redis --protected-mode no
docker build -t lucelyflores27/redis_json .
docker push lucelyflores27/redis_json
docker run -d --network p2e3 --name p2e3 lucelyflores27/redis_json

