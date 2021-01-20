# Práctica 2

## Objetivo

* Mejorar en el aprendizaje y conocimiento sobre [contenedores de Linux](https://linuxcontainers.org/) y [Docker](https://www.docker.com/)
* Investigar más sobre la orquestación de contenedores por medio de [Docker Compose](https://docs.docker.com/compose/)

## Especificaciones

* Crea un archivo `docker-compose.yml` por medio del cual instancies **tres** contenedores:
  * **Contenedor A**
    * Se encargará de ejecutar una instalación de `Mongo`
    * Prueba que `Mongo` funciona correctamente desde el contenedor y que es accesible utilizando un cliente como `PHPMoAdmin` o <https://robomongo.org/> (esto no necesita incluirse en la práctica, solamente es para pruebas tuyas :wink:)
  * **Contenedor B**
    * Deberá de instalar las siguientes dependencias
      * <https://api.mongodb.com/python/current/tutorial.html>
      * <https://requests.readthedocs.io/es/latest/>
    * Éste contenedor incluirá y ejecutará un script de python que se llame `fetch.py`, y que se conectará con el contenedor de `Mongo` para llevar a cabo lo descrito en los siguientes puntos:
      * Utiliza la librería `requests` para conectarte con la API <https://pipl.ir/> y obtener **100** diferentes usuarios auto-generados de la misma
      * Estos "_fake users_" deben de almacenarse en una colección del contenedor de `Mongo` utilizando la librería de `pymongo`. Tu decides la manera en que serán almacenados, pero la creatividad siempre premia :wink:
      * Puedes acceder a tu contenedor de `Mongo` y verificar que los usuarios fueron almacenados correctamente. Completamente opcional, pero puedes adjuntar algunos screenshots a tu práctica para comprobar este paso
  * **Contenedor C**
    * Tendrá otra pequeño script de python, el cual se llamara `view.py`
    * Éste se encargará de mostrar un usuario al azar de tu base de datos en `Mongo`. Algo similar a lo que hace <https://github.com/AnhellO/pokepy>, pero tomando la información de tu base de datos previamente llenada
    * Los usuarios tendrán que mostrarse en formato `HTML`, usando etiquetas como `<table>`, `<ul>` y/o similares. Tu decides si utilizar templates y/o estilos CSS. Opcional también es que puedes utilizar [Flask](https://flask.palletsprojects.com/en/1.1.x/) para hacer este paso aún más fácil :wink:
* Finalmente crea un archivo `README.md`, al cual le hagas commit junto con los demás archivos de tu práctica. En él deberás de describir tu experiencia después de investigar sobre `Mongo`, `requests` y sobre todo `Docker Compose` y describir el aprendizaje obtenido después de utilizarlos un poco, así como los pros y contras que pudiste detectar de las tecnologías después de llevar acabo la práctica

## Recursos

* <https://medium.com/faun/consuming-rest-apis-with-python-eb86c6b724c5>
* <https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3>
* <https://j2logo.com/tutorial-flask-espanol/>

## Deadline

* `Jueves 19 de Noviembre a las 06:59pm`
