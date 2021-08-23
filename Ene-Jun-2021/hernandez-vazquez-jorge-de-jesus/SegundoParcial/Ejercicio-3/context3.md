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



docker volume create redis_volume  

docker network create new_network-redis

docker run -d -p 6379:6379 --name redis_new2 -v redis_volume --network=new_network_redis redis

docker build -t georgehdz94/redis_json .

docker push georgehdz94/redis_json

IMAGEN CREADA
https://hub.docker.com/r/georgehdz94/redis_json


docker run -d -p 6320:6379 --name redis_json_py --network=new_network_redis georgehdz94/redis_json

 