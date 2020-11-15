# Proyecto Ordinario - Equipo 2

## Equipo

* Aguilar Cedillo Jonathan Ivan
* Chavez Muñoz Juan Arnoldo
* Salazar Coronado Juan Daniel

## Tema

* Hexagonal Architecture

## Especificaciones

### Inicio

Crear un nuevo repositorio para el proyecto final en la cuenta de cualquiera de los miembros del equipo.

Los miembros restantes deberán de crear un fork de este repositorio y contribuir en él conforme se vaya desarrollando la práctica.

Al final cada elemento del equipo deberá de subir un link al repositorio del proyecto final en su propia carpeta de alumno dentro de un archivo `.md` el cual deberá de estar bajo una nueva sub-carpeta que se llame `Ordinario`.

### Desarrollo

Crear un archivo `docker-compose.yml` por medio del cual se instancien **4** contenedores:

#### Contenedor A - DB

* Se encargará de correr un servidor de base de datos en alguno de los motores de base de datos que se revisaron en clase, es decir, elegir entre `PostgreSQL`, `MySQL`, `MongoDB` y `Redis`. Esta base de datos almacenará la información de nuestra aplicación en general
* La base de datos debe de tener persistencia habilitada, es decir, no importa cuantas veces iniciemos o detengamos nuestro container de `PostgreSQL`, incluso si lo removemos, los datos que previamente almacenamos estarán disponible en el host/equipo local. Recuerda usar volúmenes para lograr esto :wink:

#### Contenedor B - DBMS/DBAdmin

* Se encargará de ejecutar alguno de los `DBMS` que vimos en clase, dependiendo del motor de base de datos elegido. También es posible investigar e implementar algún otro `DBMS` que funcione sobre `Docker` y que sea más sencillo y/o a gusto del equipo
* Este contenedor se conectará con la base de datos del contenedor `A` de tal manera que podamos visualizar el esquema de datos creado para este proyecto

#### Contenedor C - API Scraper/Fetcher/Consumer

* Este contenedor se encargará de correr un scraper/consumer para obtener los datos de una API
* La API es opcional de entre las disponibles en <https://github.com/public-apis/public-apis>, pero debe de contar con al menos 3 diferentes endpoints/recursos. Por ejemplo, tenemos la API de <https://developer.marvel.com/docs>, y `/v1/public/characters`, `/v1/public/comics`, `/v1/public/creators`, `/v1/public/events`, `/v1/public/series` y `/v1/public/stories` son cada uno diferentes recursos, es decir que tenemos **6** endpoints/recursos en esta API
* La API elegida debe de ser diferente entre cada uno de los **4** equipos, y no puede elegirse la API de Marvel que se mostró en el ejemplo del punto anterior
* Se deben de obtener todos los datos disponibles en la `API` para cada endpoint/recurso y estos no deben de guardarse en una sola tabla, por lo que hay que analizar, definir y estructurar correctamente la base de datos al momento de diseñarla

#### Contenedor D - Front-End

* _Flask o cualquier otro MVC..._
* _Métodos GET y POST..._

#### Requerimientos extra

* .
* .
* .

### Conclusión

Crear un archivo `README.md` en el que se incluya lo siguiente:

* Un diagrama de la arquitectura de tu proyecto y un diagrama de la base de datos (`DER`). Pueden apoyarse de algunas herramientas como <https://github.com/mingrammer/diagrams> o <https://app.diagrams.net/> para generar los diagramas del proyecto. Este diagrama también debe de incluirse como imágen dentro del proyecto final
* Los pasos a seguir, detallados y concisos, para hacer funcionar el proyecto, de tal manera que pueda ser revisado sin mayores complicaciones

Finalmente, agreguen un video en equipo, en donde se exponga a detalle su proyecto y se hagan pruebas con él. Queda a criterio del propio equipo el como llevar a cabo la presentación, pero sí es necesario que cada miembro participe en la misma

* Llevar a cabo este punto por medio de `MS Teams` y agregar el archivo `.mp4` a la carpeta del proyecto final de cada alumno
* La exposición no debe tener una duración mayor a **15** minutos

## Recursos

* <https://alistair.cockburn.us/hexagonal-architecture/>
* <https://fideloper.com/hexagonal-architecture>
* <https://www.qwan.eu/2020/08/20/hexagonal-architecture.html>
* <https://alexgrover.me/posts/python-hexagonal-architecture>
* <https://medium.com/@edusalguero/arquitectura-hexagonal-59834bb44b7f>
* <https://apiumhub.com/es/tech-blog-barcelona/arquitectura-hexagonal/>
* <https://openwebinars.net/blog/que-es-la-arquitectura-hexagonal/>

## Deadline

* `Lunes 30 de Noviembre a las 11:59pm`
