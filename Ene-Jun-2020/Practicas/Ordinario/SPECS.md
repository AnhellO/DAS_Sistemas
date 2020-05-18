# Proyecto Ordinario

### Especificaciones

* Crea un archivo `docker-compose.yml` por medio del cual instancies cinco contenedores:
  * **Contenedor A**
    * Se encargará de correr un servidor de [`PostgreSQL`](https://hub.docker.com/_/postgres), el cual contendrá la base de datos que almacenará los datos de nuestra app en general
    * La base de datos debe de tener persistencia habilitada para el host, es decir, no importa cuantas veces iniciemos o detengamos nuestro container de `PostgreSQL`, los datos que previamente almacenamos estarán disponible en el host/equipo local
  * **Contenedor B**
    * Este contenedor correrá un servidor de https://www.pgadmin.org/ (en docker: https://hub.docker.com/r/dpage/pgadmin4/) que se conectará con la base de datos `postgres` del contenedor `A` de tal manera que podamos visualizar la base de datos creada para este proyecto
  * **Contenedor C**
    * Este contenedor se encargará de correr un scrapper para obtener todos los superhéroes de la `API` de https://superheroapi.com/ en base al criterio definido en la sección de `Detalles Adicionales`
    * Se deben de obtener todos los datos disponibles en la `API` para cada superhéroe y estos no deben de guardarse en una sola tabla, por lo que hay que analizar, definir y estructurar correctamente la base de datos al momento de diseñarla
  * **Contenedor D**
    * Este contenedor estará a cargo de correr una pequeña web-app que muestre un índice de todos los superhéroes existentes en la `API` a través de la página principal. Para cada superhéroe tendremos un link a una página nueva
    * En la página nueva se debe de mostrar toda la información obtenida para cada personaje, junto a una imágen del mismo (en caso de que no tuviera alguna en la `API`, hay que obtener la imágen desde otra fuente)
    * Deberás utilizar el sistema de templates `Jinja` nativo en el framework de `Flask`: https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/
  * **Contenedor E**
    * Este contenedor deberá de tener funcionando una instalación de `Redis`
    * La instalación de `Redis` funcionará como punto de [caché](https://en.wikipedia.org/wiki/Cache_(computing)) para todos los queries de tipo `SELECT/GET` que se hagan a tu aplicación a través de la web-app. Es decir, tendrás que cachear todos los queries que se hagan a la aplicación y que busquen acceder a la información existente en la base de datos
* Finalmente crea un archivo `README.md` en el que incluyas lo siguiente:
  * Un diagrama de la arquitectura de tu proyecto y un diagrama de la base de datos. Puedes apoyarte de alguna herramienta como https://github.com/mingrammer/diagrams para generar los diagramas de tu proyecto
  * Los pasos a seguir para hacer funcionar tu proyecto
  * La lista de URLs finales que existen en la aplicación
  * Una comparativa de tiempo después de hacer un query a un subconjunto de las URLs existentes en la aplicación (50 - 100 URLs) para cada uno de los siguientes escenarios (para esto deberás de medir el tiempo que toma cada request):
    * Request directo a la `API` de superheroes
    * Request a la información desde la DB de `PostgreSQL`
    * Request al nodo de caché en `Redis`

### Recursos
* https://www.postgresqltutorial.com/
* https://www.tutorialspoint.com/postgresql/index.htm
* https://github.com/khezen/compose-postgres
* https://pynative.com/python-postgresql-tutorial/
* http://docs.peewee-orm.com/en/latest/peewee/database.html#using-postgresql
* https://docs.sqlalchemy.org/en/13/dialects/postgresql.html
* https://realpython.com/primer-on-jinja-templating/
* https://dev.to/heroku/first-steps-to-caching-postgresql-queries-with-redis-2m71
* https://redislabs.com/ebook/part-1-getting-started/chapter-2-anatomy-of-a-redis-web-application/2-4-database-row-caching/

### Detalles Adicionales
* Equipo A (Angela, Juan, Emilio y Fer): Todos los superhéroes de DC
* Equipo B (Luz, Daniel y Jorge): Todos los superhéroes de Marvel

### Deadline

* `Domingo 31 de Mayo a las 11:59pm`.
