# Guía

La intención de esta guía es involucrarse con el uso de Dockerfiles y la construcción de imágenes en Docker.

1. Clona el repositorio de <https://github.com/AnhellO/pokepy> en esta ubicación
2. Metete al directorio a través de la CLI y ejecuta el comando `docker build` para construir una nueva imágen de Docker en base al Dockerfile existente en el repositorio, por ejemplo `docker build -t fulanito-hub/pokepy-ejemplo:1.0 .`
3. Instancia un contenedor en base a esa nueva imagen utilizando `docker run`
