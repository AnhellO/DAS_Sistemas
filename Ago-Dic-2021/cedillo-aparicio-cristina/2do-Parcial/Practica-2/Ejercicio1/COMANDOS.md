# Práctica 2 Parcial 2

## Ejercicio 1
* Comandos
`docker run --name=mongo_db -d -p 27027:27027 -e ME_CONFIG_MONGODB_ADMINUSERNAME=foo -e ME_CONFIG_MONGODB_ADMINPASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz mongo:4.4`

`docker exec -it mongo_db bash`

`db.qux.insertOne({name:"al",age:18,status:"D",groups:["politics","news"]})`