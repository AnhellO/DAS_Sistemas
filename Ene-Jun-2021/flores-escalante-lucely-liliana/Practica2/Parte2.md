Crea 2 contenedores por medio del cliente CLI de docker:

    El 1er contenedor ejecutará un servidor de MongoDB y su nombre deberá de ser m1

    El 2do contenedor ejecutará un cliente de Mongo Express el cual se llame mexpress y que se conectará al contenedor m1 creado en el punto anterior. Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:
        Usuario: DAS
        Password: abcde123?!

Anexa los comandos utilizados para tu solución así como los screenshots necesarios que sirvan de evidencia para comprobar que llevaste a cabo este ejercicio en tu equipo.

docker network create prac2

docker run --name=m1 --network=prac2 -d -p 3306:3306 mongo:latest

docker run --name=mexpress --network=prac2 -d -p 8081:8081 -e ME_CONFIG_BASICAUTH_USERNAME=DAS -e ME_CONFIG_BASICAUTH_PASSWORD=abcde123?! -e ME_CONFIG_MONGODB_SERVER=m1 mongo-express     
