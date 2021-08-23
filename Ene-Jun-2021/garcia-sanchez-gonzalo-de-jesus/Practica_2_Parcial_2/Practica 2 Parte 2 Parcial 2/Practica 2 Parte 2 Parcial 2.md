#   **Parte 2**

####**Crea 2 contenedores por medio del cliente CLI de docker:**
####**El 1er contenedor ejecutará un servidor de MongoDB y su nombre deberá de ser m1**

-   docker network create Practica2_Part2
-   docker run -d -p 27017:27017 --name **m1** --network Practica2_Part2 mongo

####**El 2do contenedor ejecutará un cliente de Mongo Express el cual se llame mexpress y que se conectará al contenedor m1 creado en el punto anterior. Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:**
####**Usuario: DAS**
####**Password: abcde123?!**

-   docker run -d --name Mongo_Express --network Practica2_Part2 -e ME_CONFIG_MONGODB_SERVER=**m1** -e ME_CONFIG_BASICAUTH_USERNAME=**DAS** -e ME_CONFIG_BASICAUTH_PASSWORD=**abcde123?!** -p 8081:8081 mongo-express

####**Anexa los comandos utilizados para tu solución así como los screenshots necesarios que sirvan de evidencia para comprobar que llevaste a cabo este ejercicio en tu equipo.**