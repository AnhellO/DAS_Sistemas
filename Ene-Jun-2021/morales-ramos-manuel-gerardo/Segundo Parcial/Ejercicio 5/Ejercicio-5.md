# Ejercicio 5

Para levantar los contenedores sólo es necesario tipear

`docker-compose up`

![creating-volume](./images/docker-compose.png)

---

Verificamos los datos de la base de redis

`docker exec -it redis redis-cli`

Y

`KEYS *`

![creating-network](./images/redis-cli.png)
