Crea 3 contenedores por medio del cliente CLI de docker:

    El 1er contenedor ejecutará un servidor de MongoDB y su nombre deberá de ser mongo
    El 2do contenedor deberá de ejecutar un servidor de Redis y su nombre deberá de ser redis
    El 3er contenedor deberá de ejecutar un script de Python que cumpla con los siguientes criterios:
        Que genere 1000 números aleatorios en el rango de [1000, 1000000]
        Que inserte los números pares en el contenedor de mongo
        Que inserte los números impares en el contenedor de redis
        Para este contenedor en específico tendrás que construir una imágen por medio de un nuevo Dockerfile

Asegúrate de probar que todo funciona correctamente y de que el 3er contenedor puede conectarse a los otros dos contenedores sin problema alguno.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste a cabo este ejercicio en tu equipo.

Comandos utilizados:

docker network inspect prac2

docker run --network=prac2 --name=m1 -d -p 27017:27017 mongo

docker run --network=prac2 --name=redis -d -p 6379:6379 redis --protected-mode no

docker build -t lucelyflores27/generadornumerosaleatorios .

docker run --network=prac2 --name=Aleatorios -d lucelyflores27/generadornumerosaleatorios

docker ps -a

docker logs m1

docker logs redis