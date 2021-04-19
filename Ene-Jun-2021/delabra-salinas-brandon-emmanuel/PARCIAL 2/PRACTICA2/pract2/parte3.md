Parte 3
Crea 3 contenedores por medio del cliente CLI de docker:

El 1er contenedor ejecutará un servidor de MongoDB y su nombre deberá de ser mongo
El 2do contenedor deberá de ejecutar un servidor de Redis y su nombre deberá de ser redis
El 3er contenedor deberá de ejecutar un script de Python que cumpla con los siguientes criterios:
Que genere 1000 números aleatorios en el rango de [1000, 1000000]
Que inserte los números pares en el contenedor de mongo
Que inserte los números impares en el contenedor de redis
Para este contenedor en específico tendrás que construir una imágen por medio de un nuevo Dockerfile

    docker run -d -p 6379:6379 --name redis --network p2_net redis

    docker run -d -p 27017:27017 --network p2_net --name mongo mongo

    docker build -t python-p3 .

    docker run -it -p 2308:2308 --name pythonRand --network p2_net python-p3