version: '4.1'
services:
  mongo:
    image: mongo
    container_name: mongo_db
    ports:
      - 27027:27027
    environment: 
      MONGO_INITDB_USERNAME: foo
      MONGO_INITDB_PASSWORD: bar123   

###########################################################

docker compose up

docker exec -it mongo_db mongo

use mongo_db

db.createCollection('qux')

db.qux.insert({"name":"al","age":18,"status":"D","groups":["politics","news"]})

db.qux.find();