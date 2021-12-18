Ejercicio 1


Respuesta:

No se puede crear un contenedor con mongo dónde ya tenga una base de datos y una colección solo con comandos, se necesita un script que haga ese trabajo.

Comandos ejecutados:
1.- docker run -d --name=mongo_db -p 27027:27017 -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz -v C:\Users\Kryz\Documents\DAS_Sistemas\Ene-Jun-2021\guerrero-lopez-cristian-edgardo\SEGUNDO_PARCIAL\Ejercicio_1\docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d mongo:4.2