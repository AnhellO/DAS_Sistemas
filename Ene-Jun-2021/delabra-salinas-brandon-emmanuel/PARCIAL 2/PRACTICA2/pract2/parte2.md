Parte 2
Crea 2 contenedores por medio del cliente CLI de docker:

El 1er contenedor ejecutará un servidor de MongoDB y su nombre deberá de ser m1
El 2do contenedor ejecutará un cliente de Mongo Express el cual se llame mexpress y que se conectará al contenedor m1 creado en el punto anterior. Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:
Usuario: DAS
Password: abcde123?!
Anexa los comandos utilizados para tu solución así como los screenshots necesarios que sirvan de evidencia para comprobar que llevaste a cabo este ejercicio en tu equipo.

Creando network
    docker network create --driver bridge p2_net
Creando contenedor asignado al network
    docker run -d -p 27017:27017 --network p2_net --name m2 mongo
Asignando el usiario y contraseña
    docker run --name=mexpress --network p2_net -e ME_CONFIG_MONGODB_SERVER=m2 -e MONGO_INITDB_ROOT_USERNAME=HELP -e MONGO_INITDB_ROOT_PASSWORD=HELPX2 -p 8081:8081 mongo-express