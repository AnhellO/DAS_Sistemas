# Práctica 2 - Parte 3


El 1er contenedor ejecutará un servidor de MongoDB y su nombre deberá de ser mongo

-  docker network create mongo_network   (crea red con el nombre de mongo_network)
-  docker run -d -p 27018:27017 --name mongo --network mongo_network mongo (crea contenedor con el nombre de mongo y se conecta ala red de mongo_network)

El 2do contenedor deberá de ejecutar un servidor de Redis y su nombre deberá de ser redis

- docker run -d -p 6379:6379 --network mongo_network --name redis redis --protected-mode no (crea contenedor con el nombre de redis, se conecta ala red de mongo_network, se le asigna puerto 6379)

El 3er contenedor deberá de ejecutar un script de Python que cumpla con los siguientes criterios:
Que genere 1000 números aleatorios en el rango de [1000, 1000000]
Que inserte los números pares en el contenedor de mongo
Que inserte los números impares en el contenedor de redis
Para este contenedor en específico tendrás que construir una imágen por medio de un nuevo Dockerfile

- docker build -t aliciapruebas/parte_3 . (construye la imagen de python)
- docker run -d --network mongo_network --name py aliciapruebas/parte_3 (crea contenedor nuevo con la imágen  de python)
- 
Se usaron los sig comandos:
-docker logs py.(para ver las impreciones dek script)
- redis-cli -h 0.0.0.0 -p 6379 (se uso el cliente CLI de redis )
- KEYS * (muestra los id de los datos ingresados)
- GET (id) ( se uso varias veces la instruccion para verificar que se hayan ingresado los números correctos).
- exit (salir de cli de redis)
- docker exec -it m1 /bin/bash ( conectarse al contenedor de Mongo ) , mongo
- show dbs;(mostar bases de datos) 
- Use Numeros_pares (usar la base de datos Numeros_pares)
-  db.numero.find() (muestra los datsos ingresados del script)
-  exit( salir de cli dde mongo)
-  sudo docker stop $(sudo docker ps -q -a) Detiene todos los contenedores