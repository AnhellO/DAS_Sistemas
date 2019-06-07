# Ordinario

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Extraordinario/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request hasta la hora límite (`05:00am` de `Junio 7, 2019`) para evitar que este sea copiado :wink:

## Ejercicios

### Patrones de Diseño

#### Ejercicio 1

Para el ejemplo de código en el archivo [composite.py](composite.py):

* Implementa la funcionalidad necesaria utilizando el patrón de diseño [`composite`](https://sourcemaking.com/design_patterns/composite) para que sea posible crear una interfaz gráfica sencilla que contenga múltiples componentes, como sucedería en una GUI real.
  * Algunos componentes pueden contener otros componentes, pero también hay componentes que no pueden/tengan que contener más componentes
  * Deberás de tomar la siguiente [imagen de ejemplo](https://semantic-ui.com/images/examples/login.png) como caso de prueba para tu implementación del patrón `composite`
  * Ejemplo:
  ```
    Componente 'Ventana' contiene 'Imagen'
    Componente 'Imagen': imagen.jpg
    Componente 'Ventana' contiene 'Etiqueta'
    Componente 'Etiqueta': "Log-in to your account"
    Componente 'Ventana' contiene 'Panel'
    Componente 'Panel' contiene 'Input'
    Componente 'Panel' contiene 'Input'
    Componente 'Panel' contiene 'Botón'
    Componente 'Botón' contiene 'Etiqueta'
    ...
  ```

#### Ejercicio 2

Para el ejemplo de código en el archivo [ocp.py](ocp.py):

* Analiza y refactoriza el código para utilizar el `Open/Closed Principle` de manera correcta
* Explica la lógica implementada detrás de tu enfoque
* Con base en el código/enfoque original y en los cambios que realizaste, contesta a las siguientes preguntas (puedes contestarlas con comentarios dentro de tu código):
  * ¿Qué sucedería si quisieramos sumar las áreas de otros tipos de figuras?
  * ¿Qué tendríamos que hacer para poder sumar volúmenes además de áreas?

#### Ejercicio 3

Utilizando la siguiente API pública -> [https://restcountries.eu/](https://restcountries.eu/):

* Crea un script en `python` que obtenga todos los países de la API y los guarde en una tabla `paises` dentro de una base de datos en `SQLite`.
  * Crea la base de datos y sus tablas en una clase por separado a la que uses para obtener los registros de la API.
  * Puedes comenzar a ayudarte de [peewee](https://github.com/coleifer/peewee) o de tus clases propias desde este punto.

#### Ejercicio 4

* Utilizando la base de datos que resultó del ejercicio anterior:
  * Crea un archivo `.html` que contenga una tabla con todos los países, similar a la [siguiente tabla](https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses#Pa%C3%ADses)
  * Apoyándote de [peewee](https://github.com/coleifer/peewee), o bien, creando una pequeña clase que funja como [mini-ORM](https://www.fullstackpython.com/object-relational-mappers-orms.html), crea un nuevo script en python el cual resuelva los siguientes queries de `SQL`:
    1. Contar la cantidad total de países
    2. Obtener todos los datos solamente para `México`
    3. Obtener todos los países que hablen el idioma español
    4. Obtener todos los países que pertenezcan al continente europeo


#### Deadline

* `2019-06-07 05:00am`