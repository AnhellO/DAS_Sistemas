
docker run -d -p 27027:27017 --name=mongo_db -e MONGO_INITDB_ROOT_USERNAME=foo -e MONGO_INITDB_ROOT_PASSWORD=bar123 -e MONGO_INITDB_DATABASE=baz mongo:4.2

docker exec -it mongo_db bash 
mongo
use baz

db.qux.insert({
    name: "all",
    age: 18,
    status: "D",
    groups: ["politics", "news"]
    
})




