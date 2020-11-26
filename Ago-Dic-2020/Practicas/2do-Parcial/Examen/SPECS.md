# 2do. Examen Parcial

## Previo

- Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen en este caso tendría que llamarse `../Segundo Parcial/..`
- Si el ejemplo solamente necesita comandos escritos entonces agregalos en un archivo `.md` que anexes por separado dentro de tu carpeta con las soluciones al examen. También es importante adjuntar las demás evidencias que se piden por ejercicio.

## Ejercicios

### Ejercicio 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de `Docker` que corra un servidor de [`MySQL`](https://hub.docker.com/_/mysql) versión **8** y que cumpla con los siguientes puntos?

- Que el contenedor se llame `mysql_db`
- Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)
- Que el puerto asignado a la máquina host sea el `4000`
- Que el usuario sea `foo`
- Que el password sea `bar123`
- Que se cree una base de datos llamada `baz`

Finalmente, ¿con qué comando(s) puedo conectarme a mi base de datos de `MySQL` corriendo dentro de mi contenedor de `mysql_db`?

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

### Ejercicio 2

Crea 2 contenedores por medio del cliente `CLI` de `docker`:

- El **1er contenedor** ejecutará un servidor de [`Redis`](https://hub.docker.com/_/redis) y su nombre deberá de ser `redis`
- El **2do contenedor** deberá de ejecutar un servidor de [`Redis Commander`](https://hub.docker.com/r/rediscommander/redis-commander) el cual tiene que estar protegido con usuario y contraseña para poder acceder a él. El contenedor debe de llamarse `commander`

Asegúrate de probar que todo funciona correctamente y que el servidor de `redis-commander` puede contectarse al de `redis` sin problema alguno visitando la URL correcta.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

### Ejercicio 3

Crea un volumen que se llame `mongo_volume` y que utilice el driver por default para los `Docker` volumes.

Ejecuta un contenedor de [`MongoDB`](https://hub.docker.com/_/mongo) que se llame `mongo` y que monte el volumen creado en el paso anterior, y una vez que todo este listo ejecuta los siguientes pasos:

- Corre el script [`populate.py`](ejercicio-3/populate.py)
- Luego corre el otro script [`find.py`](ejercicio-3/find.py), deberías de obtener una salida como la siguiente:

``` shell
##### RECORDS #####
{'_id': ObjectId('5fbf475bece16a8442cfe774'), 'first_name': 'foo', 'last_name': 'bar', 'email': 'foo@mail.com'}
{'_id': ObjectId('5fbf475bece16a8442cfe775'), 'first_name': 'foo', 'last_name': 'baz', 'email': 'baz@mail.com'}
{'_id': ObjectId('5fbf475bece16a8442cfe776'), 'first_name': 'bar', 'last_name': 'baz', 'email': 'bar@mail.com'}
{'_id': ObjectId('5fbf475bece16a8442cfe777'), 'first_name': 'fulano', 'last_name': 'mengano', 'email': 'fulano@mail.com'}
{'_id': ObjectId('5fbf475bece16a8442cfe778'), 'first_name': 'zultano', 'last_name': 'perengano', 'email': 'zultano@mail.com'}
```

Ahora detén y borra el contenedor de `mongo`, y levanta un nuevo contenedor que también ejecute un servidor de `MongoDB` y que utilice el mismo volumen de `mongo_volume` previamente creado, pero que en esta ocasión se llame `mongo2`.

Vuelve a ejecutar el script de [`find.py`](ejercicio-3/find.py) y contesta a la siguiente pregunta: ¿Cuál fue nuestra salida en está ocasión?

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

### Ejercicio 4

Crea un `Dockerfile` que cumpla con los siguientes requisitos:

- Que extienda de la imágen base de [`Python3`](https://hub.docker.com/_/python)
- Que utilice el directorio `/usr/src` como el directorio de trabajo
- Que clone el siguiente repositorio: <https://github.com/joaoventura/flask-static-site>
- Que instale todas las dependencias necesarias especificadas en el archivo de [`requirements.txt`](https://github.com/joaoventura/flask-static-site/blob/master/requirements.txt) por medio de `pip`
- Y finalmente que ejecute el script [`site.py`](https://github.com/joaoventura/flask-static-site/blob/master/site.py), justo como se especifíca en el [`README`](https://github.com/joaoventura/flask-static-site#development--building) del repositorio
- Ten en cuenta que los contenedores creados en base a esta imágen deben de ser accesibles desde el exterior :wink:

Construye una imágen basada en el `Dockerfile` que acabas de crear y llámala `{mi-user}/static_flask`, donde `{mi-user}` equivale a tu usuario de [`DockerHub`](https://hub.docker.com/). Una vez que hayas creado la imagen envíala a tu cuenta de `DockerHub`. Debe de estar accesible similar a como lo está en [este ejemplo](https://hub.docker.com/repository/docker/anhellojz/static_flask/). Asegúrate de adjuntar el link a ella en tus resultados del ejercicio.

Para finalizar, ejecuta un nuevo contenedor basado en la imágen recién creada que se llame `flask`, que corra "_daemonizado_", y que esté accesible a través del puerto `5000` de tu máquina.

Anexa los comandos utilizados para llevar a cabo este ejercicio.

### Ejercicio 5

Crea un archivo `docker-compose.yml` que ejecute 3 contenedores:

- El **1er contenedor** ejecutará un servidor de [`PostgreSQL`](https://hub.docker.com/_/postgres) y su nombre deberá de ser `postgres`
  - Este debe de crear una base de datos que se ajuste al archivo [`data.json`](ejercicio-5/data.json). Tu decides como modelarla, pero lo importante es que la(s) tabla(s) en la `BD` tengan **al menos 10** diferentes columnas para varios de los registros existentes en el archivo
- El **2do contenedor** deberá de ejecutar un servidor de [`PgAdmin`](https://hub.docker.com/r/dpage/pgadmin4/) el cual debe de tener acceso al servidor de base de datos del _1er contenedor_. El contenedor debe de llamarse `pgadmin`
- El **3er contenedor** deberá de ejecutar un script de `Python` que tome todos los registros existentes en el archivo [`data.json`](ejercicio-5/data.json) y los inserte en la base de datos del _1er contenedor_
  - Para llevar a cabo esta parte puedes utilizar algún ORM como [`Peewee`](http://docs.peewee-orm.com/en/latest/) o [`SQLAlchemy`](https://www.sqlalchemy.org/), o bien [`SQL` "_crudo_"](https://www.postgresqltutorial.com/postgresql-python/)

## Deadline

- `Viernes 27 de Noviembre a las 02:00am`
- OJO: Si terminas el examen antes de la hora límite, no lo subas a `GitHub` hasta que se aproxime la hora para que este no sea copiado :wink:
