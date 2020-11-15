# Proyecto Ordinario - Equipo 4

## Equipo

* Jesús Angel
* David Aguirre
* Diego Rodríguez

## Tema

* Micro-Services Architecture

## Especificaciones

* Crear un nuevo repositorio para el proyecto final en la cuenta de cualquiera de los miembros del equipo
  * Los miembros restantes deberán de crear un fork de este repositorio y contribuir en él conforme se vaya desarrollando la práctica
  * Al final cada elemento del equipo deberá de subir un link al repositorio del proyecto final en su propia carpeta de alumno dentro de un archivo `md` el cual deberá de estar bajo una nueva sub-carpeta que se llame `Ordinario`
* Crear un archivo `docker-compose.yml` por medio del cual se instancien **5** contenedores:
  * **Contenedor A**
    * _DB_
  * **Contenedor B**
    * _DB Admin_
  * **Contenedor C**
    * _Scraper/Fetcher/Consumer de una API_
    * _API opcional de entre las disponibles en <https://github.com/public-apis/public-apis>_
  * **Contenedor D**
    * _Flask o cualquier otro MVC_
    * _Métodos GET y POST_
  * **Contenedor E**
    * _Message Queue Broker_
* Crear un archivo `README.md` en el que incluyas lo siguiente:
  * Un diagrama de la arquitectura de tu proyecto y un diagrama de la base de datos. Pueden apoyarse de alguna herramienta como <https://github.com/mingrammer/diagrams> o <https://app.diagrams.net/> para generar los diagramas del proyecto
  * Los pasos a seguir, detallados y concisos, para hacer funcionar el proyecto, de tal manera que pueda ser revisado sin mayores complicaciones
  * La lista de URLs finales que existen en la aplicación, ya sea en un archivo `.txt`, `.md` o `.csv`
* Finalmente, agreguen un video en equipo, en donde se exponga a detalle su proyecto y se hagan pruebas con él. Queda a criterio del propio equipo el como llevar a cabo la presentación, pero sí es necesario que cada miembro participe en la misma
  * Llevar a cabo este punto por medio de MS Teams y agregar el archivo `.mp4` a la carpeta del proyecto final de cada alumno
  * La exposición no debe tener una duración mayor a **15** minutos

## Recursos

### Arquitectura

* <https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch04.html>
* <https://www.microservices.com/>
* <https://microservices.io/patterns/microservices.html>
* <https://medium.com/hashmapinc/the-what-why-and-how-of-a-microservices-architecture-4179579423a9>
* <https://github.com/GoogleCloudPlatform/microservices-demo>
* <https://microservices-scaffold.readthedocs.io/en/latest/>
* <https://medium.com/@sonusharma.mnnit/building-a-microservice-in-python-ff009da83dac>
* <https://www.paradigmadigital.com/dev/como-construir-microservicios-en-python-1-2/>
* <https://codigofacilito.com/articulos/microservcios>
* <https://steemit.com/spanish/@jza/nameko-framework-de-microservicios-con-python>
* <https://ichi.pro/es/microservicios-de-python-api-objetos-y-modelos-de-datos-de-almacenamiento-170228015369526>

### Librerías

* <https://www.rabbitmq.com/getstarted.html>
* <https://github.com/Pungyeon/go-rabbitmq-example/blob/master/README.md>
* <https://kafka.apache.org/>
* <https://redislabs.com/blog/use-redis-event-store-communication-microservices/>
* <https://docs.celeryproject.org/en/stable/getting-started/introduction.html>
* <https://autobahn.readthedocs.io/en/latest/asynchronous-programming.html>
* <https://xpdays.com.ua/programs/event-driven-systems-with-mongodb/>
* <https://github.com/python-microservices>
* <https://nameko.readthedocs.io/en/stable/>

## Deadline

* `Lunes 30 de Noviembre a las 11:59pm`
