Ejercicio 5
Toma cualquiera de los 3 primeros ejercicios y trasládalo a que funcione por medio de Docker Compose, tú eliges cual.

Asegúrate de probar que funciona correctamente y no te olvides de adjuntar el archivo docker-compose.yml en la carpeta de tu solución.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

El ejercico que se usara para esta actividad sera el 1

sudo docker run -d --name=mongo_db -p 27027:27017 -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz -v ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js mongo:4.2