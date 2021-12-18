# Práctica 3

## Objetivo

* Mejorar en el aprendizaje y conocimiento sobre [contenedores de Linux](https://linuxcontainers.org/) y [Docker](https://www.docker.com/), específicamente sobre la construcción de imágenes

## Especificaciones

Crea un `Dockerfile` que cumpla con los siguientes requisitos:

* Que extienda de la imágen base de [`Python3`](https://hub.docker.com/_/python)
* Que utilice el directorio `/usr/src` como el directorio de trabajo
* Que clone el siguiente repositorio: <https://github.com/joaoventura/flask-static-site>
* Que instale todas las dependencias necesarias especificadas en el archivo de [`requirements.txt`](https://github.com/joaoventura/flask-static-site/blob/master/requirements.txt) por medio de `pip`
* Y finalmente que ejecute el script [`site.py`](https://github.com/joaoventura/flask-static-site/blob/master/site.py), justo como se especifíca en el [`README`](https://github.com/joaoventura/flask-static-site#development--building) del repositorio
* Ten en cuenta que los contenedores creados en base a esta imágen deben de ser accesibles desde el exterior :wink:

Construye una imágen basada en el `Dockerfile` que acabas de crear y llámala `{mi-user}/static_flask`, donde `{mi-user}` equivale a tu usuario de [`DockerHub`](https://hub.docker.com/). Una vez que hayas creado la imagen envíala a tu cuenta de `DockerHub`. Debe de estar accesible similar a como lo está en [este ejemplo](https://hub.docker.com/r/anhellojz/static_flask). Asegúrate de adjuntar el link a ella en tus resultados del ejercicio.

Para finalizar, ejecuta un nuevo contenedor basado en la imágen recién creada que se llame `flask`, que corra "_daemonizado_", y que esté accesible a través del puerto `5000` de tu máquina.

Anexa los comandos utilizados para llevar a cabo este ejercicio.

## Deadline

* `Domingo 9 de Mayo a las 11:59pm`
