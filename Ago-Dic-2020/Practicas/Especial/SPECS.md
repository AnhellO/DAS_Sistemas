# Examen Especial

## Información

- Fecha de aplicación: `Martes 26 de Enero del 2021`
- Maestro: `Angel Santiago Jaime Zavala`

## Previo

- Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing)
- La carpeta del examen tendrá que llamarse `../Examen Especial/..`
- Cada ejercicio tendrá que ir en una carpeta por separado dentro de la carpeta de `Examen Especial/`, por ejemplo `Examen Especial/Ejercicio-1/..`
- Si el ejemplo solamente necesita comandos escritos entonces agregalos en un archivo `.md` (Markdown) que anexes por separado dentro de tu carpeta con las soluciones al examen. También es importante adjuntar las demás evidencias que se piden por cada ejercicio, como screenshots por ejemplo

## Ejercicios

### Ejercicio 1

- Crea una clase `Vehiculo` que cumpla con los siguientes puntos
  - Que tenga los atributos de instancia `velocidad_maxima`, `kilometraje` y `capacidad`
  - Que tenga un atributo de clase llamado `random` con cualquier valor
  - Que implemente la función nativa de Python para poder obtener una representación en `string` de un objeto instanciado de la clase

### Ejercicio 2

- Crea una clase `Autobus` que herede de la clase `Vehiculo` del ejercicio anterior
  - Añade una función `tarifa()`, en donde el cargo de tarifa predeterminado de cualquier vehículo es igual a la `capacidad de asientos del vehículo x 100`. Si el vehículo es una instancia de autobús, debemos agregar un **10%** adicional a la tarifa completa como cargo de mantenimiento. Entonces, la tarifa total por instancia de autobús será igual a `monto final = tarifa total + 10% de la tarifa total`
- Crea una lista que contenga varias instancias de las clases de `Vehiculo` y de`Autobus` e iterala a través de un ciclo, llevando a cabo la siguiente evaluación:
  - Si el objeto es una instancia de la clase `Autobus` entonces imprime el mensaje `"Soy un autobús! -> {informacion del autobus}"`
  - En caso contrario no imprimas ningún mensaje y continua iterando la lista

### Ejercicio 3

- Crea un diagrama UML que modele y represente a cada una de las clases creadas en el par de ejecicios anteriores
- Puedes hacerlo a mano o por medio de alguna herramienta de software, como a ti te sea más cómodo, solamente asegúrate de adjuntar screenshots o fotografías de los diagramas de UML que hayas creado

### Ejercicio 4

- Para el ejemplo de código en el archivo [srp.py](ejercicio-4/srp.py):
  - Analiza y refactoriza el código para utilizar el [`Single Responsibility Principle`](https://en.wikipedia.org/wiki/Single-responsibility_principle) de manera correcta
  - Explica la lógica implementada detrás de tu enfoque (puedes contestar a esto con comentarios dentro de tu solución de código)
  - Con base en el código/enfoque original y en los cambios que realizaste, contesta a las siguientes preguntas (puedes contestarlas con comentarios dentro de tu código):
    - ¿Qué sucedería si quiero agregar otro formato de serialización más complejo como `XML` o `Yaml`?
    - ¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase `Usuario`?

### Ejercicio 5

- Crea una suite de tests unitarios para tu solución del ejercicio anterior
- Puedes utilizar la librería nativa de `Python`, [`unittest`](https://docs.python.org/3/library/unittest.html), o bien una librería externa como [`pytest`](https://docs.pytest.org/en/stable/)

### Ejercicio 6

- Se está desarrollando un juego similar a "_Age Of Empires_" que permite al usuario interactuar con personajes que juegan ciertos roles, por lo que se desea incorporar al juego la funcionalidad para crear nuevos personajes que se añaden al conjunto de personajes predefinidos
- En el juego, todos los personajes serán instancias de un pequeño conjunto de clases tales como `Heroe`, `Villano`, `Hechicero` y `Monstruo`, y cada clase tiene una serie de atributos como `nombre`, `imagen`, `altura`, `peso`, `inteligencia` y `habilidades`, y según sus valores, una instancia de la clase representa a un personaje u otro, por ejemplo podemos tener los personajes _héroe bobo_ o un _heroe listo_, o _monstruo bueno_ o _monstruo malo_
- Diseña una solución que permita al usuario crear nuevos personajes y seleccionar para cada sesión del juego personajes de una colección de personajes creados utilizando el patrón de diseño [`Prototype`](https://es.wikipedia.org/wiki/Prototipo_(patr%C3%B3n_de_dise%C3%B1o))

### Ejercicio 7

Partiendo de la suite de tests unitarios en el archivo [`state_test.py`](ejercicio-7/state_test.py):

- Tomemos de ejemplo un editor de texto, que te permite cambiar el estado del texto que se está escribiendo, es decir, si se han seleccionado mayúsculas, entonces comienza a escribir en mayúsculas, si está en minúsculas, escribe con letras minúsculas nada más, y así sucesivamente
- Crea un nuevo archivo/módulo llamado `state.py` e implementa la funcionalidad necesaria utilizando el patrón de diseño [`State`](https://en.wikipedia.org/wiki/State_pattern), de tal manera que podamos escribir a salida estándar (stdout) de las diferentes maneras que se listan a continuación:
  - Default: `Texto en default, Así como viEne`
  - Mayúsculas: `TEXTO EN MAYÚSCULAS`
  - Minúsculas: `texto en mayúsculas`
  - Título: `Texto En Título`
- Asegúrate de que la suite de tests unitarios pasa sin mayores problemas una vez que implementaste tu solución, y recuerda que este archivo **NO** debe de ser modificado

### Ejercicio 8

Crea 3 contenedores por medio del cliente `CLI` de `docker`:

- El **1er contenedor** ejecutará un servidor de [`MongoDB`](https://hub.docker.com/_/mongo) y su nombre deberá de ser `mongo`
- El **2do contenedor** deberá de ejecutar un servidor de [`Redis`](https://hub.docker.com/_/redis) y su nombre deberá de ser `redis`
- El **3er contenedor** deberá de ejecutar un script de `Python` que cumpla con los siguientes criterios:
  - Que genere **1000** números aleatorios en el rango de `[1000, 1000000]`
  - Que inserte los números pares en el contenedor de `mongo`
  - Que inserte los números impares en el contenedor de `redis`
  - Para este contenedor en específico tendrás que construir una imágen por medio de un nuevo `Dockerfile`

Asegúrate de probar que todo funciona correctamente y de que el **3er contenedor** puede conectarse a los otros dos contenedores sin problema alguno.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste a cabo este ejercicio en tu equipo.

### Ejercicio 9

Crea 3 contenedores por medio del cliente `CLI` de `docker`:

- El **1er contenedor** ejecutará un servidor de [`PostgreSQL`](https://hub.docker.com/_/postgres) y su nombre deberá de ser `postgres`
  - Este debe de crear una base de datos que se ajuste a las especificafiones solicitadas para el **3er contenedor**. Queda a tu criterio como modelar las tablas de la BD, pero asegúrate de que representan correctamente a cada tipo de objeto solicitado en el script del **3er contenedor**
  - Tenemos que crear un volúmen de `Docker` para que los datos de este contenedor se persistan en nuestro equipo host, y este tendrá que tener por nombre `postgres_volume`
- El **2do contenedor** deberá de ejecutar un servidor de [`PgAdmin`](https://hub.docker.com/r/dpage/pgadmin4/) el cual debe de tener acceso al servidor de base de datos del _1er contenedor_. El contenedor debe de llamarse `pgadmin` y nos servirá como DBMS de la aplicación
- El **3er contenedor** se encargará de crear un `Dockerfile` que cumpla con los siguientes requisitos:
  - Que extienda de la imágen base de [`Python3`](https://hub.docker.com/_/python)
  - Que utilice el directorio `/app` como el directorio de trabajo
  - Que instale las dependencias [`Peewee`](http://docs.peewee-orm.com/en/latest/) y [`requests`](https://requests.readthedocs.io/en/master/) por medio de `pip` apoyado de un archivo `requirements.txt`
  - Que contenga un script de `Python` el cual consuma todos los recursos/endpoints de la API <http://jsonplaceholder.typicode.com/> (revisa la sección de "_Resources_"). Es decir, tenemos que guardar todos los `/posts`, todos los `/comments`, y así sucesivamente hasta que guardemos también a todos los `/users`. Estos objetos tendrán que ser guardados en la DB del **1er contenedor** por medio del ORM de `Peewee`
  - Que ejecute el script anteriormente mencionado

Asegúrate de probar que todo funciona correctamente y de que el **3er contenedor** puede conectarse al **1er contenedor** sin problema alguno.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste a cabo este ejercicio en tu equipo.

### Ejercicio 10

Crea un archivo `docker-compose.yml` que ejecute 4 contenedores:

- El **1er contenedor** ejecutará un servidor de [`MongoDB`](https://hub.docker.com/_/mongo) y su nombre deberá de ser `mongo_compose`
- El **2do contenedor** ejecutará un cliente de [`Mongo Express`](https://hub.docker.com/_/mongo-express) el cual se llame `mexpress_compose`, y el cual se conectará al contenedor `mongo_compose` creado en el punto anterior. Este contenedor fungirá como el DBMS de la aplicación
  - Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:
    - Usuario: `DASistemas`
    - Password: `ex-especial567`
- El **3er contenedor** ejecutará un script de `Python` que lleve a cabo lo siguiente:
  - Que lea el archivo XML de la carpeta [`ejercicio-10/`](ejercicio-10/people.xml)
  - Que modele/mappee los nodos de `<person>` con una clase `Persona`, de tal manera que cada nodo del `XML` pueda ser representado con una instancia de la clase `Persona`
  - Que guarde cada nodo de `<person>` en una base de datos de `MongoDB` en el **1er contenedor**. Cada nodo tendrá que ser un registro por separado, pero todos estos registros pueden vivir en una sola [colección (tabla)](https://docs.mongodb.com/manual/core/databases-and-collections/) de `Mongo`
  - Asegúrate de construir el respectivo `Dockerfile` necesario para esta imagen, y de instalar todas las dependencias necesarias en el mismo
- El **4to contenedor** ejecutará un script de `Python` que lleve a cabo lo siguiente:
  - Levantará una pequeña "`API`" que mostrará todos los registros guardados desde el `XML` a través del endpoint/recurso de `/people`, por lo tanto tendrá que conectarse al **1er contenedor** de `Mongo`, de tal manera que pueda acceder a los registros de la colección. Estos registros tendrán que ser servidos en formato `JSON` y la API tendrá que funcionar por medio de `Flask`
  - Aparte del endpoint/recurso de `/people`, tendremos que agregar otro endpoint/recurso que nos muestre un JSON con la información en particular para cada persona, y que sea accesible por medio de un nuevo endpoint/recurso con la forma `/people/{id}`, en donde `{id}` es igual al ID del registro en la BD
  - Asegúrate de construir el respectivo `Dockerfile` necesario para esta imagen, y de instalar todas las dependencias necesarias en el mismo
  - Finalmente, este contenedor en particular tendrá que ser ejecutado en modo "_daemonizado_", y deberá de estar accesible a través del puerto `7777` de tu máquina. Asegúrate de verificar que funciona de manera correcta :wink:

Recuerda que **todo debe de funcionar** por medio de `docker-compose`, es decir, nada debe de hacerse manualmente ni instalando algo en el equipo host.

Anexa los comandos utilizados para tu solución así como los screenshots necesarios que sirvan de evidencia para comprobar que llevaste a cabo este ejercicio en tu equipo.

## Deadline

- `Domingo 31 de Enero del 2021 a las 6:00 PM`
