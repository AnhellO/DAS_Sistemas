# Exámen 2do. Parcial

### Especificaciones

* Crea un archivo `docker-compose.yml` por medio del cual instancies cuatro contenedores:
  * **Contenedor A**
    * Ejecutará un script en python el cual se encargué de obtener la lista de todos los personajes existentes en la siguiente API: https://www.breakingbadapi.com/
    * Los items deberán de guardarse en la base de datos que correrá dentro del contenedor `B`
  * **Contenedor B**
    * Se encargará de alojar una base de datos en `MySQL`, la cual almacenará los datos obtenidos de la API, y de la cual se obtendrán los datos que se mostrarán en el contenedor `D`
  * **Contenedor C**
    * Este contenedor ejecutará una instalación de `PHPMyAdmin` que tendrá como host a la base de datos que vive dentro del contenedor `B`. Deberías poder analizar y revisar tus datos desde la interfaz que provee `PHPMyAdmin`
    * Una vez que tus datos estén en la DB y que `PHPMyAdmin` funcione correctamente, deberás de exportar los datos existentes en la DB a un archivo `CSV`, el cual se tendrá que agregar a la carpeta del exámen
  * **Contenedor D**
    * Tendrá que ejecutar una pequeña app que funcione con `Python` y `Flask`
    * La app tendrá una página principal que contenga una tabla con la lista de todos los personajes obtenidos de la API, y para cada personaje un link a una página nueva para cada uno
    * La página individual para cada personaje tiene que mostrar algo similar a lo siguiente: https://www.dropbox.com/s/3p6qffjbwuxzzx1/Screenshot%202020-05-14%2019.35.21.png?dl=0. Se debe de mostrar toda la información disponible del personaje, la cual tendrás que obtener por medio del contenedor `A`
    * En esta ocasión no podrás utilizar `HTML` nativo, ya que tendrás que hacer uso de los templates nativos de `Flask`: https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/
* Finalmente crea un archivo `README.md` en el que incluyas lo siguiente:
  * Los pasos a seguir para hacer funcionar tu práctica de exámen
  * La lista de URLs que tiene tu aplicación

### Hints
* No es necesario publicar la imagen en https://hub.docker.com/

### Deadline

* `Viernes 15 de Mayo a las 02:00am`.
