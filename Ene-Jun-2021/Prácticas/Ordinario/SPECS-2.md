# Proyecto Ordinario - Equipo 2 - Hexagonal Architecture

## Equipo

* David Hiroshi Gloria Kawasaki
* Lucely Liliana Flores Escalante
* Cristian Edgardo Guerrero Lopez
* Jose Fernando Pérez Arroyo
* Brandon Emmanuel Delabra Salinas

## Tema

Imagina que nos contrataron para construir la aplicación web de una librería y necesitamos desarrollar el _backend_ que se hará cargo de ello. Queremos listar algunos o todos los libros con sus respectivos autores y los demás atributos de su ficha descriptiva. Y también queremos ser capaces de agregar, actualizar y borrar libros de los registros de la base de datos.

**Hexagonal Architecture:** Implementa el proyecto siguiendo los lineamientos y requisitos del patrón de arquitectura hexagonal.

## Especificaciones

### Inicio

Crear un nuevo repositorio para el proyecto final en la cuenta de cualquiera de los miembros del equipo.

Los miembros restantes deberán de crear un fork de este repositorio y contribuir en él conforme se vaya desarrollando la práctica.

Al final cada elemento del equipo deberá de subir un link al repositorio del proyecto final en su propia carpeta de alumno dentro de un archivo `.md` el cual deberá de estar bajo una nueva sub-carpeta que se llame `Ordinario`.

### Desarrollo

Crear un archivo `docker-compose.yml` por medio del cual se instancien **5** contenedores:

#### Contenedor A - DB

* Se encargará de correr un servidor de base de datos en alguno de los motores de base de datos que se revisaron en clase, es decir, se puede elegir entre `PostgreSQL`, `MySQL`, `MongoDB` y `Redis`. Esta base de datos almacenará la información de nuestra aplicación en general
* La base de datos debe de tener persistencia habilitada, es decir, no importa cuantas veces iniciemos o detengamos nuestro container de base de datos, incluso si lo removemos, los datos que previamente almacenamos estarán disponible en el host/equipo local. Recuerda usar volúmenes para lograr esto :wink:

#### Contenedor B - DBMS/DBAdmin

* Se encargará de ejecutar alguno de los `DBMS` que vimos en clase, dependiendo del motor de base de datos elegido. También es posible investigar e implementar algún otro `DBMS` que funcione sobre `Docker` y que sea más sencillo y/o a gusto del equipo
* Este contenedor se conectará con la base de datos del contenedor `A` de tal manera que podamos visualizar el esquema de datos creado para este proyecto

#### Contenedor C - Scraper or Generator

* Este contenedor se encargará de correr un script que popule la base de datos del contenedor `A` con los datos que deberán de mostrarse a través de la API del contenedor `D`
* Los datos que tienen que generarse deben de girar en torno a una **librería**. Es decir que deberás de utilizar los respectivo modelos y/o entidades necesarios para representar un registro en la base de datos, por ejemplo: libros, autores, editoriales, etcétera
* Este contenedor en especifico y su lógica de negocio quedan a la creatividad e imaginación de cada equipo (y esto se tomará en cuenta para la evaluación), pero como tip puedes generar los datos a través de alguna librería para generar datos falsos, o bien obtenerlos de alguna API/DB pública (aquí hay un [listado de referencia](https://github.com/public-apis/public-apis#books))

#### Contenedor D - API

* Para esta parte puedes utilizar `Flask` o cualquier otro framework `MVC` como [`Django`](https://www.djangoproject.com/) por ejemplo. Incluso puedes desarrollarlo "_from scratch_" (desde `0`) si lo consideras pertinente y necesario :wink:
* Este contenedor estará a cargo de ejecutar una pequeña "_web-app_" que muestre un listado de todos los libros y de las otras entidades de la librería que hayas agregado o generado por medio del contenedor `C` en formato `JSON`
* Para cada uno de los endpoints/recursos que hayas agregado, habilita las operaciones `CRUD` por medio del mismo endpoint, es decir, ser capaz de hacer un request de tipo [`HTTP - POST`](https://developer.mozilla.org/es/docs/Web/HTTP/Methods/POST) a esa ruta a través de nuestro API, de tal manera que alguien que consuma la "_web-app_" también pueda crear registros por medio de la misma. Puedes revisar los laboratorios 11 y 12 del repositorio de [docker-workshop](https://github.com/AnhellO/docker-workshop/tree/main/laboratorios) como referencia a este punto en específico. Asegúrate de que para cada endpoint/recurso se pasen todos los datos necesarios para poder llevar a cabo operaciones CRUD en la BD con éxito. Recuerda que puedes hacer pruebas para este punto en específico con algunas herramientas gratuitas como [`Postman`](https://www.postman.com/) o [`Insomnia`](https://insomnia.rest/)

#### Contenedor E - Frontend

* Agregar un contenedor extra `E` con un frontend (GUI) que consuma la API del contenedor `D`. Acá puedes utilizar tecnologías como `HTML`, `CSS`, `Javascript`, `Bootstrap`, `Vue`, `Angular` o `ReactJS` para hacer más rápido este proceso
* Queda a tu imaginación y creatividad el como luzca la interfaz final :wink:

#### Opcional - Puntos Extra

Los siguientes puntos son opcionales, sin embargo implementarlos provee **1** punto extra por cada uno sobre la calificación total final.

* Agregar tests unitarios y de integración para el proyecto
* Utilizar [Swagger](https://swagger.io/) en tu proyecto y agregar un contenedor nuevo con el [`Swagger UI`](https://hub.docker.com/r/swaggerapi/swagger-ui) de la aplicación

### Conclusión

Crear un archivo `README.md` en el que se incluya lo siguiente:

* Un diagrama de la arquitectura de tu proyecto y un diagrama de la base de datos (`DER`). Pueden apoyarse de algunas herramientas como <https://github.com/mingrammer/diagrams> o <https://app.diagrams.net/> para generar los diagramas del proyecto. Este diagrama también debe de incluirse como imágen dentro del proyecto final
* Los pasos a seguir detallados y concisos que indiquen como hacer funcionar el proyecto, de tal manera que pueda ser revisado sin mayores complicaciones

Finalmente, agreguen un video en equipo, en donde se exponga a detalle su proyecto y se hagan pruebas con él. Queda a criterio del propio equipo el como llevar a cabo la presentación, pero sí es necesario que cada miembro participe en la misma.

* Llevar a cabo este punto por medio de `MS Teams` y subir el archivo `.mp4` a algún drive público adjuntando el link de acceso al video al archivo `README`.md
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

* `Domingo 6 de Junio a las 12:00pm`
