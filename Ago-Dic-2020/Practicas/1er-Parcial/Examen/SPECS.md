# 1er. Examen Parcial

## Previo

* Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen en este caso tendría que llamarse `../Primer Parcial/..`

## Especificaciones y Requerimientos

### Ejercicios

#### Ejercicio 1

* Crea una clase `Pista`, la cual modele una _"pista musical"_ (canción):
  * Esta deberá de tener al menos **4** atributos
    * El 1er atributo debe de ser el `nombre` de la pista
    * El 2do atributo debe de ser `starred` o `favorita`, que será de tipo `bool` (es decir, la pista puede marcarse como favorita o no)
    * El 3er atributo deberá de ser la duración de la pista. Este puede ser de tipo `int`, `flotante` o hasta [`time`](https://docs.python.org/3/library/datetime.html)
    * El 4to atributo es opcional
  * También deberá tener al menos **2** funciones más aparte de los setters/getters que pudieras agregar para los atributos (es opcional el comportamiento de cada una)
* Crea una clase `ReproductorMusical` (también puede llamarse `AppMusical` o cualquier sinónimo relacionado). Esta tendrá el objetivo de modelar un objeto _"disco"_ de la vida real, y deberá de tener al menos **3** atributos, 1 de ellos deberá de ser alguna estructura de datos que se encargue de almacenar `1 o más` pistas. Las funciones con las que contará esta clase se describen a continuación:
  * Una función que nos permita agregar `pistas` a una instancia de la clase
  * Otra función que nos devuelva todas las `pistas` marcadas como favoritas en el reproductor musical
  * Finalmente, agrega una última función que nos devuelva todas las pistas ordenádas por duración de la pista, desde la más corta a la más larga (ascendentemente)

#### Ejercicio 2

* Complementando tus resultados del ejercicio 1. Imagina que queremos darle la funcionalidad a nuestro _"reproductor musical"_ de poder integrar plug-ins a él. Estos plug-ins se encargan de **agregar nueva funcionalidad** al reproductor musical, como por ejemplo, mostrar las letras de una determinada canción, decirte pistas relacionadas al género de la canción, devolverte la información del artista material de la canción, o hasta customizar el reproductor musical a que tenga una imágen de fondo, etcétera
* Implementa el patrón de diseño decorador, de tal manera que podamos **"decorar"** nuestras instancias de la clase `ReproductorMusical` con `Plugins`
  * Al menos dos plugins con diferente funcionalidad entre si necesitan agregarse en este punto
  * Puedes implementar esto con el patrón de diseño desde 0, o bien, utilizando los decoradores nativos de `Python`, como a ti se te haga más sencillo :wink:

#### Ejercicio 3

* Partiendo de la suite de tests unitarios en el archivo [`proxy_test.py`](proxy_test.py):
  * Imagina que estamos agregando un sistema de autenticación para los diferentes sistemas existentes en la empresa en donde trabajamos, y en cada uno de ellos hay diferentes roles/tareas que se pueden hacer o no hacer en base al nivel de permisos del usuario (para casos prácticos, solamente hay **3** niveles disponibles en esta práctica)
  * Crea un nuevo archivo/módulo `proxy.py` e implementa la funcionalidad necesaria para que nuestro nuevo sistema de autenticación funcione como un sistema de `Proxy` que llevará a cabo la asignación/accesibilidad de operaciones en base al nivel de permisos

#### Ejercicio 4

* Partiendo de la suite de tests unitarios en el archivo [`builder_test.py`](builder_test.py):
  * Tenemos una pizzeria que vende en línea, y queremos darle la posibilidad al usuario de que arme su propia pizza a su gusto, como el quiera (_al cliente lo que pida!!!_), por lo cual tenemos que darle la flexibilidad a nuestra página en línea para que se puedan registrar pizzas compradas con los ingredientes seleccionados (los cuales pueden ser varios)
  * Crea un nuevo archivo/módulo `builder.py` e implementa el patrón de diseño `Builder` para que el código de nuestra paginita web pueda ir construyendo la pizza deseada en base a los ingredientes seleccionados

### Puntos Extra

* Implementa la suite de tests unitarios para el **Ejercicio 1**. En esta suite se deben de probar al menos 10 posibles casos de prueba para el comportamiento de una instancia de la clase `ReproductorMusical`
  * **(5 puntos sobre 100)**
* Para el ejemplo de código en el archivo [composite.py](composite.py):
  * Implementa la funcionalidad necesaria utilizando el patrón de diseño `Composite` para que sea posible crear una interfaz gráfica sencilla que contenga múltiples componentes, como sucedería en una GUI real.
    * Algunos componentes pueden contener otros componentes, pero también hay componentes que no tengan más componentes
    * Deberás de tomar la siguiente [imagen de ejemplo](https://semantic-ui.com/images/examples/login.png) como caso de prueba para tu implementación del patrón `Composite`
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
  * **(10 puntos sobre 100)**
* Implementa la suite de tests unitarios para el ejercicio de puntos extra de composite, tomando el caso de uso propuesto como caso de prueba en la suite
  * **(5 puntos sobre 100)**
