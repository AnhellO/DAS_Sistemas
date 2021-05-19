# 2do. Examen Parcial

## Previo

* Desarrolla los ejemplos de código en tu computadora y envíalos por correo electrónico al email de <asjz2892@gmail.com> por medio de un achivo comprimido `.zip`. La carpeta del examen tendrá que llamarse `../Segundo Parcial/..` y dentro de esta carpeta deberá de venir una carpeta dedicada para cada ejercicio, por ejemplo `../Segundo Parcial/Ejercicio-1/..`
* Si el ejemplo solamente necesita comandos escritos entonces agregalos en un archivo `.md` que anexes por separado dentro de tu carpeta con las soluciones al examen. También es importante adjuntar las demás evidencias que se piden por ejercicio.

## Especificaciones y Requerimientos

### Ejercicios

#### Ejercicio 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de `Docker` que corra un servidor de [`MongoDB`](https://hub.docker.com/_/mongo) versión **4.2** y que cumpla con los siguientes puntos?

* Que el contenedor se llame `mongo_db`
* Que el contenedor se mantenga en ejecución
* Que el puerto asignado a la máquina host sea el `27027`
* Que el usuario sea `foo`
* Que el password sea `bar123`
* Que se cree una base de datos llamada `baz`
* Que se cree una colección en la base de datos de `baz` llamada `qux`

Finalmente, contesta a las siguientes preguntas:

* ¿Con qué comando(s) puedo conectarme a la base de datos de `MongoDB` corriendo dentro de mi contenedor de `mongo_db`?
* ¿Cómo puedo insertar [este registro](mongodb-registro.png) en la colección de `qux` creada previamente?

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

#### Ejercicio 2

Crea 4 contenedores por medio del cliente `CLI` de `docker`:

* El **1er contenedor** ejecutará un primer servidor de [`Redis`](https://hub.docker.com/_/redis) y su nombre deberá de ser `redis_db_1`
* El **2do contenedor** ejecutará un segundo servidor de [`Redis`](https://hub.docker.com/_/redis) y su nombre deberá de ser `redis_db_2`
* El **3er contenedor** ejecutará un tercer servidor de [`Redis`](https://hub.docker.com/_/redis) y su nombre deberá de ser `redis_db_3`
* El **4to contenedor** deberá de ejecutar un servidor de [`Redis Commander`](https://hub.docker.com/r/rediscommander/redis-commander) el cual estará protegido con el usuario `DASistemas` y la contraseña `2do-parcial!` para poder acceder a él. El contenedor debe de llamarse `redis_dbms` y tendrá que conectarse con todos los contenedores de `Redis` que se crearon en los pasos previos

Verifica que puedes acceder correctamente a la interfaz de Redis commander y que los 3 contenedores de `Redis` son accesibles desde el `DBMS`.

#### Ejercicio 3

Crea un volumen que se llame `redis_volume` y que utilice el driver por default para los `Docker` volumes.

Crea un `Dockerfile` que cumpla con los siguientes requisitos:

* Que extienda de la imágen base de [`Python3`](https://hub.docker.com/_/python)
* Que utilice el directorio `/app` como el directorio de trabajo
* Que clone el siguiente repositorio: <https://github.com/joaoventura/flask-static-site>
* Que instale todas las dependencias necesarias especificadas en el archivo de [`requirements.txt`](https://github.com/joaoventura/flask-static-site/blob/master/requirements.txt) por medio de `pip`
* Y finalmente que ejecute el script [`site.py`](https://github.com/joaoventura/flask-static-site/blob/master/site.py), justo como se especifíca en el [`README`](https://github.com/joaoventura/flask-static-site#development--building) del repositorio
* Ten en cuenta que los contenedores creados en base a esta imágen deben de ser accesibles desde el exterior :wink:

Construye una imágen basada en el `Dockerfile` que acabas de crear y llámala `{mi-user}/static_flask`, donde `{mi-user}` equivale a tu usuario de [`DockerHub`](https://hub.docker.com/). Una vez que hayas creado la imagen envíala a tu cuenta de `DockerHub`. Debe de estar accesible similar a como lo está en [este ejemplo](https://hub.docker.com/r/anhellojz/static_flask). Asegúrate de adjuntar el link a ella en tus resultados del ejercicio.

Para finalizar, ejecuta un nuevo contenedor basado en la imágen recién creada que se llame `flask`, que corra "_daemonizado_", y que esté accesible a través del puerto `5000` de tu máquina.

Anexa los comandos utilizados para llevar a cabo este ejercicio.

#### Ejercicio 4

* Toma el siguiente proyecto de referencia y ejecútalo en tu máquina local: <https://github.com/nickjj/docker-flask-example>
  * Análizalo con detenimiento y estúdialo un poco
  * Asegúrate de leer la información del `README.md` sobre cómo funciona, y de jugar y experimentar un poco con él
* Elabora el diagrama de arquitectura de la aplicación
  * Puedes hacerlo a mano o bien utilizar alguna herramientas externa como <https://app.diagrams.net/>
  * Adjunta el diagrama como un archivo `.jpg` o `.png` en la carpeta de este ejercicio
  * Adicionalmente adjunta un archivo `README.md` específico para este ejercicio en el cual justifiques tu diagrama de arquitectura y el por qué de la forma en que decidiste diseñarlo

#### Ejercicio 5

* 

### Puntos Extra

* 

## Deadline

* `Viernes 21 de Mayo a las 11:59pm`
