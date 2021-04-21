# Solución

1. Crea el contenedor de `Mongo`: `docker run --name mongo -d -p 27017:27017 mongo`
   1. Probamos la conexión al contenedor de `MongoDB` en la máquina local a través de un DBMS cliente como [`Robo3T`](https://robomongo.org/) o [`Compass`](https://www.mongodb.com/products/compass)
2. Crea el contenedor de `Redis`: `docker run --name redis -d -p 6379:6379 redis`
   1. Probamos la conexión al contenedor de `Redis` en la máquina local a través de un DBMS cliente como [`redis-cli`](https://redis.io/topics/rediscli) o [Medis](https://github.com/luin/medis)
3. Creamos [script de `Python`](parte-3/script.py) e instala dependencias en local para probar
   1. `pip install pymongo`
   2. `pip install redis`
4. Dockerizamos script de `Python` -> [`Dockerfile`](parte-3/Dockerfile)
5. Construye imágen de `Docker` para script de `Python`: `docker build -t nombre-que-quieras-para-la-imagen .`
6. Crea "_network_" para comunicar los contenedores entre si: `docker network create pymonred`
7. Agrega los contenedores de `Mongo` y de `Redis` a la nueva red
   1. `docker network connect pymonred mongo`
   2. `docker network connect pymonred redis`
8. Ejecuta contenedor de este script con: `docker run --name py1 -d --network pymonred anhellojz/pymongoredis:0.2`
9. Revisa que la información se guardó correctamente entre los contenedores de `Mongo` y de `Redis` a través de alguno de los DBMS antes mencionados, o bien directamente a través de los contenedores
10. Detén y remueve todos los contenedores