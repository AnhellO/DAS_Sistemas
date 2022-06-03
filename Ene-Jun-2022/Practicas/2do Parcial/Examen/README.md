# 2do. Examen Parcial

## Previo

* Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen en este caso tendrá que llamarse `../Segundo Parcial/..`
* Cada ejercicio deberá estar en una carpeta por separado, es decir `../Segundo Parcial/Ejercicio 1/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request ni hagas commit de tu código hasta la hora límite (`Domingo 5 de Junio del 2022 a las 11:59pm`) para evitar que este sea copiado :wink:
* Explica la lógica utilizada detrás de cada uno de los ejercicios. Pueden ser como un archivo de texto por separado, o bien, como comentarios dentro del mismo código

## Especificaciones

* Crea un archivo `docker-compose.yml` por medio del cual instancies cuatro contenedores:
  * **Contenedor A**
    * Ejecutará un script en python el cual se encargué de obtener una lista de todos los issues existentes (abiertos y cerrados) en el repositorio de Flask a través de la API de GitHub:
      * API GitHub: <https://docs.github.com/es/rest>
      * Repositorio de Flask: <https://github.com/pallets/flask/>
    * Los items deberán de guardarse en la base de datos que correrá dentro del contenedor `B`
  * **Contenedor B**
    * Se encargará de alojar una base de datos en `MongoDB` o en `Redis` (tu decides cuál utilizar), la cual almacenará los datos obtenidos de la API, y de la cual se obtendrán los datos que se mostrarán en el contenedor `D`
  * **Contenedor C**
    * Este contenedor ejecutará una instalación de un DBMS que tendrá como host a la base de datos que vive dentro del contenedor `B`. Deberías poder analizar y revisar tus datos desde la interfaz que provee ese DBMS
  * **Contenedor D**
    * Tendrá que ejecutar una pequeña app que funcione con `Python` y `Flask` como API propia
    * La app tendrá una página principal que contenga una tabla con la lista de todos los issues obtenidos de la API, y para cada issue un link a una página nueva para cada uno
    * La página individual para cada issue tiene que mostrar una tabla de `HTML` que describa toda la información del issue por completo. Se debe de mostrar toda la información disponible del issue, la cual tendrás que obtener por medio del contenedor `A`
    * En esta ocasión no podrás utilizar `HTML` nativo, ya que tendrás que hacer uso de los templates nativos de `Flask`: <https://flask.palletsprojects.com/en/2.1.x/tutorial/templates/>
* Finalmente crea un archivo `README.md` en el que incluyas lo siguiente:
  * Los pasos a seguir para hacer funcionar tu práctica de exámen
  * La lista de URLs que tiene tu aplicación

## Hints

* No es necesario publicar la imagen en <https://hub.docker.com/>
* Ten en cuenta que la API de GitHub tiene un límite de peticiones por hora y por día. Te toca a ti investigar cual es este límite y tener cuidado de no superarlo :wink:

## Deadline

* `Domingo 5 de Junio del 2022 a las 11:59pm`
