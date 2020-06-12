# Proyecto Ordinario

### Especificaciones

* Crea un archivo `docker-compose.yml` por medio del cual instancies cuatro contenedores:
  * **Contenedor A**
    * Este contenedor se encargará de correr un scrapper para obtener al menos `100` artistas de la API de last.fm: https://www.last.fm/api/. Debes de obtener al menos `5` datos adicionales aparte del nombre de la banda o artista, y dentro de estos datos adicionales debe de encontrarse una lista de al menos `5` canciones que pertenezcan al artista. Revisa la documentación de la API para que puedas ver todos los endpoints disponibles
    * Toda esta información debe de ser guardada dentro de la base de datos en memoria de `Redis` que se instanciará por medio del contenedor `D`
    * Puedes utilizar el nombre del artista o algún hash generado como llave para guardar los datos en `Redis`
  * **Contenedor B**
    * Este contenedor se encargará de correr otro scrapper por separado que obtenga las letras de las `5` canciones guardadas para cada artista que guardaste en la DB de `Redis` por medio del contenedor `A`. Las letras las deberás de obtener de la siguiente API: https://lyricsovh.docs.apiary.io/#. Estas deben de ser guardadas junto a la información del artista dentro de la misma DB
  * **Contenedor C**
    * Este contenedor estará a cargo de correr una pequeña web-app que muestre un índice de todos los artistas existentes en la DB de `Redis` a través de la página principal. Para cada artista tendremos un link a una página nueva, y en la página nueva de cada artista se debe de mostrar toda la información obtenida para cada uno de ellos junto a una lista de las canciones del artista y la letra de cada una. Esta información puede mostrarse en esa misma página, o en una página nueva, es decir, podrías terminar con algo como lo siguiente:
      * `/` (índice principal de la webapp)
      * `/artista` (página de un artista)
      * `/artista/cancion-1` (pagina de una de las canciones para ese artista)
    * Deberás utilizar el sistema de templates [`Jinja`](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/) nativo de `Flask` para mostrar el `HTML`/markup de la aplicación. Queda a tu criterio el uso de `CSS`/estilos para darle formato a la web-app
  * **Contenedor D**
    * Este contenedor deberá de tener funcionando una instalación de `Redis`
    * La instalación de `Redis` funcionará como base de datos y punto de [caché](https://en.wikipedia.org/wiki/Cache_(computing) para todos los queries de tipo `SELECT/GET` que se hagan a tu aplicación a través de la web-app
* Finalmente crea un archivo `README.md` en el que incluyas lo siguiente:
  * Los pasos detallados a seguir para hacer funcionar tu proyecto
  * La lista de URLs finales que existen en la aplicación. Estas URLs son las generadas por tu app, y no las que pertenecen a la API

### Deadline

* `Domingo 14 de Junio a las 12:00pm`
