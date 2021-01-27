# Examen Extraordinario

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Examen Extraordinario/..`
* Incluye los archivos de tus bases de datos `.db` generados dentro del pull request final
* La hora límite para subir tus soluciones a los ejercicios del examen es hasta las `12:00pm del Viernes 6 de Diciembre del 2019`

## Ejercicios

#### Parte 1

* Crea un script en `Python` que consuma información de la siguiente API:
  * [`https://pokeapi.co/`](https://pokeapi.co/) (Utiliza la `v2` de la API)
  * Deberás guardar la información en una base de datos en SQLite utlizando [`SQLAlchemy`](https://github.com/sqlalchemy/sqlalchemy) o [`Peewee`](https://github.com/coleifer/peewee) como `ORM`, y que cumpla con los siguientes criterios:
    * Obtener `100` pokemón **al azar** de la API y guardarlos en la BD
      * Agregar al menos 10 campos/columnas diferentes a la table de `pokemon` aparte del `id` y del `nombre` del pokemon
      * Agregar un campo espefícico que contenga un link a la imágen del pokemon e.g. [`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png`](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png)

#### Parte 2

* Partiendo de la BD (base de datos) del ejercicio anterior, crea una pequeña app que haga uso del micro-framework [`flask`](https://www.palletsprojects.com/p/flask/), cuyo propósito sea mostrar una galería de pokemon existentes en la DB
  * La app/galería debe de contener lo siguiente:
    * Un mensaje de bienvenida a la galería
    * Una `<table>` que organice a los pokemon por tipo (es decir, tipo `water`, `fire`, `grass`, etc.)
      * Cada tipo debe de ligar a una nueva página en la app, la cual nos muestre todos los pokemon existentes en la BD para ese tipo en espefícico
      * Para cada pokemon existente debemos de tener aparte una nueva página por separado la cual nos muestre toda la información espefícica existente para ese pokemon
        * Agrega una tag de `<img>` la cual muestre la imágen del pokemon que se está describiendo
    * Un link que nos lleve a otra página la cual muestre a todos los pokemon existentes en la base de datos, sin excepción
      * Al igual que el punto anterior, para cada pokemon existente debemos de tener aparte una nueva página por separado la cual nos muestre la información espefícica de ese pokemon, incluyendo la imágen del mismo
* Te puedes apoyar de las siguientes rutas para saber como estructurar la app/galería (**OJO:** el nombre de las rutas no tiene que ser el mismo)
  * `/poke-gallery/`
  * `/poke-gallery/{type}/`
  * `/poke-gallery/{type}/{pokemon}`
  * `/poke-gallery/all/`
  * `/poke-gallery/all/{pokemon}`

#### Parte 3

* Agrega un botón en la página principal de la galería el cual nos permita agregar un nuevo pokemon al azar a nuestra BD
  * La app deberá de volver a consumir de la API de pokemón en este punto
  * Debemos validar que el pokemón no exista ya en la DB
  * Al terminar de agregar el pokemón hay que mostrar un mensaje el cual notifique al usuario que se pudo agregar el nuevo registro exitosamente. El mensaje deberá de contener un link a la vista del pokemón dentro de nuestra app, ejemplo: `Nuevo pokemón Venusaur agregado exitosamente: /poke-gallery/all/{pokemon}`


## Recursos

* http://anh.cs.luc.edu/handsonPythonTutorial/ch4.html
* http://python.zirael.org/ch-dynamic_pages.html
* https://realpython.com/python-web-applications/
* https://code.tutsplus.com/articles/python-from-scratch-create-a-dynamic-website--net-22787
* https://wiki.python.org/moin/Routing
* https://www.tutorialspoint.com/python_network_programming/python_routing.htm
* https://pypi.org/project/Routes/
* https://www.palletsprojects.com/p/flask/
* https://opensource.com/article/18/4/flask
* https://hackersandslackers.com/the-art-of-building-flask-routes/
* https://www.tutorialspoint.com/php/php_get_post.htm