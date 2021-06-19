docker pull mongo

mushu@mushu:~$ cd Escritorio/Segundo\ Parcial/Ejercicio-1/
mushu@mushu:~/Escritorio/Segundo Parcial/Ejercicio-1$ docker ps

mushu@mushu:~/Escritorio/Segundo Parcial/Ejercicio-1$ docker ps

mushu@mushu:~/Escritorio/Segundo Parcial/Ejercicio-1$ docker exec -it mongo_db /bin/bash
root@9070c7faf94d:/# mongo
MongoDB shell version v4.2.14
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("e1f7108b-b5dc-4e73-a7bb-654dd2a49728") }
MongoDB server version: 4.2.14
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
	https://docs.mongodb.com/
Questions? Try the MongoDB Developer Community Forums
	https://community.mongodb.com
> use admin
switched to db admin
> db.auth("foo","bar123")
1
> show dbs 
admin   0.000GB
config  0.000GB
local   0.000GB
> use baz
switched to db baz
> db.qux.save({name:'al', age: 18, status: "D",groups: ["politics","news"]})
WriteResult({ "nInserted" : 1 })
> db.qux.find()
{ "_id" : ObjectId("60a85c7ef75d43eac4edcaa3"), "name" : "al", "age" : 18, "status" : "D", "groups" : [ "politics", "news" ] }
> exit
bye
root@9070c7faf94d:/# exit
exit
mushu@mushu:~/Escritorio/Segundo Parcial/Ejercicio-1$ docker stop
"docker stop" requires at least 1 argument.
See 'docker stop --help'.

Usage:  docker stop [OPTIONS] CONTAINER [CONTAINER...]

Stop one or more running containers
mushu@mushu:~/Escritorio/Segundo Parcial/Ejercicio-1$ docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                                           NAMES
9070c7faf94d   mongo:4.2   "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes   0.0.0.0:27027->27017/tcp, :::27027->27017/tcp   mongo_db
mushu@mushu:~/Escritorio/Segundo Parcial/Ejercicio-1$ docker stop mongo_db
mongo_db
mushu@mus