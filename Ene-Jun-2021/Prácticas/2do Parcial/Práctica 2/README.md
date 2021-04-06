# Práctica 2

## Objetivo

* Mejorar en el aprendizaje y conocimiento sobre [contenedores de Linux](https://linuxcontainers.org/) y [Docker](https://www.docker.com/)
* Poner en práctica el conocimiento teórico obtenido sobre arquitectura de software

## Especificaciones

### Parte 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de `Docker` que corra un servidor de [`MySQL`](https://hub.docker.com/_/mysql) versión **8** y que cumpla con los siguientes puntos?

* Que el contenedor se llame `mysql_db`
* Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)
* Que el puerto asignado a la máquina host sea el `4000`
* Que el usuario sea `foo`
* Que el password sea `bar123`
* Que se cree una base de datos llamada `baz`

Finalmente, ¿con qué comando(s) puedo conectarme a mi base de datos de `MySQL` corriendo dentro de mi contenedor de `mysql_db`?

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

### Parte 2

Crea 2 contenedores por medio del cliente `CLI` de `docker`:

* El **1er contenedor** ejecutará un servidor de [`MongoDB`](https://hub.docker.com/_/mongo) y su nombre deberá de ser `m1`
* El **2do contenedor** ejecutará un cliente de [`Mongo Express`](https://hub.docker.com/_/mongo-express) el cual se llame `mexpress` y que se conectará al contenedor `m1` creado en el punto anterior. Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:
  * Usuario: `DAS`
  * Password: `abcde123?!`

Anexa los comandos utilizados para tu solución así como los screenshots necesarios que sirvan de evidencia para comprobar que llevaste a cabo este ejercicio en tu equipo.

### Parte 3

Crea 3 contenedores por medio del cliente `CLI` de `docker`:

* El **1er contenedor** ejecutará un servidor de [`MongoDB`](https://hub.docker.com/_/mongo) y su nombre deberá de ser `mongo`
* El **2do contenedor** deberá de ejecutar un servidor de [`Redis`](https://hub.docker.com/_/redis) y su nombre deberá de ser `redis`
* El **3er contenedor** deberá de ejecutar un script de `Python` que cumpla con los siguientes criterios:
  * Que genere **1000** números aleatorios en el rango de `[1000, 1000000]`
  * Que inserte los números pares en el contenedor de `mongo`
  * Que inserte los números impares en el contenedor de `redis`
  * Para este contenedor en específico tendrás que construir una imágen por medio de un nuevo `Dockerfile`

Asegúrate de probar que todo funciona correctamente y de que el **3er contenedor** puede conectarse a los otros dos contenedores sin problema alguno.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste a cabo este ejercicio en tu equipo.

## Deadline

* `Domingo 18 de Abril a las 11:59pm`
