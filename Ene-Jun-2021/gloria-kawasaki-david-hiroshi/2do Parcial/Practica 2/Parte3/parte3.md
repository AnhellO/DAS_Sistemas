Parte 3

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
- sudo pip3 install redis (ya que no tenía instalada la librería de redis para la app)
- sudo docker network create p2p3
- sudo docker run --network p2p3 -d -p 27017:27017 --name m1 mongo
- sudo docker run -d -p 6379:6379 --network=p2p3 --name redis redis --protected-mode no
- sudo docker ps
- sudo docker build -t hiroshigk/randgen .
- sudo docker run -d --network p2p3 --name randgen hiroshigk/randgen
- sudo docker logs m1
- sudo docker logs redis
- sudo docker network inspect p2p3