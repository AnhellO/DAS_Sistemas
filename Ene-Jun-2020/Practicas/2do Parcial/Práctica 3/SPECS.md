# Práctica 3

### Objetivo

* Mejorar en el aprendizaje y conocimiento sobre [contenedores de Linux](https://linuxcontainers.org/) y [Docker](https://www.docker.com/).
* Aprender e investigar sobre Redis`, y poner en práctica el conocimiento adquirido.

### Especificaciones

* Crea un archivo `docker-compose.yml` por medio del cual instancies dos contenedores:
  * **Contenedor A**
    * Tendrá la instalación de `Redis`
    * Prueba que `Redis` funciona correctamente desde el contenedor utilizando el cliente de `redis-cli`
  * **Contenedor B**
    * Deberá instalar las siguientes dependencias
      * https://github.com/andymccurdy/redis-py
      * https://faker.readthedocs.io/en/master/
    * Deberá de poder acceder al contenedor de `Redis`
    * Éste incluirá y ejecutará el script de python que se conecta con el contenedor de `Redis` y que lleva a cabo lo descrito en el siguiente punto
* `app.py` script
  * Utiliza la librería `Faker` para generar una lista de 100 `email` (direcciones de correo electrónico) falsos
  * Estos `emails` deben almacenarse en el storage de `Redis` utilizando la librería de `redis-py`. Los `emails` serán identificados por una llave única que también tendrá que ser generada por medio de la librería de `Faker` (revisa los generadores para `md5`, `sha1` y `sha256` en la documentación de `Faker` para mejor referencia)
* Accede a tu contenedor de `Redis` y verifica que las nuevas llaves fueron almacenadas. Puedes adjuntar screenshots a tu práctica para comprobar este paso
* Finalmente crea un archivo `README.md`, al cual le hagas commit junto con los demás archivos de tu práctica. En él deberás de describir tu experiencia después de investigar sobre `Redis` y utilizarlo un poco, así los pros y contras que pudiste detectar en la tecnología después de llevar acabo la práctica

### Hints
* No es necesario publicar la imagen en https://hub.docker.com/

### Recursos

* Tutoriales de Docker que ya se han compartido email y durantes las mismas clases.
* Libro introductorio de Redis: https://redislabs.com/ebook/foreword/.
* Tutoriales de Redis:
  * https://www.tutorialspoint.com/redis/index.htm
  * http://try.redis.io/
  * https://markheath.net/post/exploring-redis-with-docker

### Deadline

* `Domingo 17 de Mayo a las 11:59pm`.