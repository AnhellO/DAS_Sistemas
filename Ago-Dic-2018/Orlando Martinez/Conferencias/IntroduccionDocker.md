#Click IT "Introducción a Docker"
En esta se nos explico lo que es Docker y a grandes rasgos es una tecnología de virtualización usada esencialmente para aislar los procesos y aplicaciones del sistema principal (Host) y brindar mayor seguridad a las aplicaciones y al sistema que las hospeda.

###¿Qué es un contenedor?
Un contenedor es una forma de separar procesos de manera independiente, y estos también pueden ser agrupados en imágenes que después serán usadas para lanzar un container pero que al mismo tiempo pueden hacer uso de recursos del sistema como cpu,ram,kernel,etc...

###¿Que es una imagen de Docker?
Una imagen de Docker es un conjunto de capas, cada una de estas se genera cada vez que realizamos algún cambio a la imagen base que nos encontremos usando en ese momento.
Esto es posible gracias a ciertos comandos y entre los mas importantes están:

- MAINTAINER
- FROM
- ADD
- COPY
- RUN
- ENV
- ENTRYPOINT CMD


En resumen una de las razones para usar Docker es porque permite la creación de ambientes inmutables. Además de ser muy portable, y es muy fácil de lanzar un container en caso de que se requiera uno más o que el actual falle.