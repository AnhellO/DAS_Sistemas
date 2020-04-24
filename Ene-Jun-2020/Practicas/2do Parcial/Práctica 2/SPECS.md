# Práctica 2

### Objetivo

* Mejorar en el aprendizaje y conocimiento sobre [contenedores de Linux](https://linuxcontainers.org/) y [Docker](https://www.docker.com/).
* Poner en práctica el conocimiento adquirido del tema de manejo de bases de datos por medio de Python

### Especificaciones

* Crear una pequeña app que funcione dentro de un container de docker. Deberás de crear un `Dockerfile` nuevo para tu aplicación. Recuerda instalar todas las dependencias necesarias dentro de tu contenedor. Tu decides cuáles dependencias instalar en base a las librerías que quieras utilizar para desarrollar tu práctica. Recuerda también que tu práctica debe de funcionar y correr dentro de un container creado a partir de la imágen generada en base a tu `Dockerfile`.
* Como **1er. paso** deberás de analizar y estudiar la siguiente API: https://age-of-empires-2-api.herokuapp.com/docs/#/. Esta será la API con la que estarás trabajando durante la práctica.
* Para el **2do. paso** tendrás que modelar y crear una base de datos vacía en `SQLite`, basado en las entidades y campos disponibles en la API. Tendrás que crear la base de datos en un script/archivo de `Python` por separado. Aquí puedes utilizar el cliente/tookit de terminal `SQLite` para verificar y jugar con tu base de datos recién creada.
* Para el **3er. paso** deberás de crear un nuevo script en `Python` que obtenga todos los datos existentes/disponibles en la API, es decir, todas las `civilizations`, `units`, `structures` y `technologies` disponibles. Estos datos tendrán que ser insertados a las base de datos que creaste en el paso anterior.
* Para el **4to. paso** tendrás que crear 1 archivo HTML para cada una de las entidades disponibles en la API. Cada archivo `HTML` deberá de contener un tabla estática de `HTML` que muestre todos los datos obtenidos de la API para cada entidad, pero leyéndolos desde tu base de datos. El formato y diseño del `HTML` queda a tu elección, y puedes utilizar algún framework web como `Flask` para mostrar el `HTML` si así tu lo deseas :wink:. 
* Y como **último paso**, crea un archivo `README.md` en el cual documentes todos los pasos que se necesitan seguir para poder correr tu aplicación (por ejemplo, como construir la imágen de docker, crear el contenedor, el orden de los scripts que se tiene que ejecutar, en que rutas y/o de que manera ver los archivos HTML, etcétera)

### Recursos

* Tutoriales de Docker que ya se han compartido email y durantes las mismas clases.
* ORMs discutidos en clase: https://www.fullstackpython.com/object-relational-mappers-orms.html

### Deadline

* `Sábado 2 de Mayo a las 11:00pm`.