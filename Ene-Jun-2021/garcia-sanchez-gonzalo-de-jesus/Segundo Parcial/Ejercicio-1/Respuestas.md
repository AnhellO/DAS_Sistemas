# Gonzalo Garcia

# CREO EL CONTENEDOR CON LO QUE NOS INDICA
docker run -d -p 27027:27017 --name=mongo_db -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz mongo:4.2

# COMANDO PARA EJECUTAR MONGO ( conectarme a la base de datos de MongoDB corriendo dentro de mi contenedor de mongo_db )
docker exec -it mongo_db bash

# PARA ENTRAR A MONGO
mongo 27027 o simplemente  monngo

# PARA INSERTAR LO QUE NOS PIDEN 
db.qux1.insert({
    name: "all",
    age: 18,
    status: "D",
    groups: ["politics", "news"]
    
})




