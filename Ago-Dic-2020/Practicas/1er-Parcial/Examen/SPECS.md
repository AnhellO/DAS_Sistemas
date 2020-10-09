# 1er. Examen Parcial

## Previo

- Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen en este caso tendría que llamarse `../Primer Parcial/..`

## Especificaciones y Requerimientos

## Ejercicios

#### Ejercicio 1

- Crea una clase `Pista`, la cual modele una _"pista musical"_ (canción):
  - Esta deberá de tener al menos **4** atributos
    - El 1er atributo debe de ser el `nombre` de la pista
    - El 2do atributo debe de ser `starred` o `favorita`, que será de tipo `bool` (es decir, la pista puede marcarse como favorita o no)
    - El 3er atributo deberá de ser la duración de la pista. Este puede ser de tipo `int`, `flotante` o hasta [`time`](https://docs.python.org/3/library/datetime.html)
    - El 4to atributo es opcional
  - También deberá tener al menos **2** funciones más aparte de los setters/getters que pudieras agregar para los atributos (es opcional el comportamiento de cada una)
- Crea una clase `ReproductorMusical` (también puede llamarse `AppMusical` o cualquier sinónimo relacionado). Esta tendrá el objetivo de modelar un objeto _"disco"_ de la vida real, y deberá de tener al menos **3** atributos, 1 de ellos deberá de ser alguna estructura de datos que se encargue de almacenar `1 o más` pistas. Las funciones con las que contará esta clase se describen a continuación:
  - Una función que nos permita agregar `pistas` a una instancia de la clase
  - Otra función que nos devuelva todas las `pistas` marcadas como favoritas en el reproductor musical
  - Finalmente, agrega una última función que nos devuelva todas las pistas ordenádas por duración de la pista, desde la más corta a la más larga (ascendentemente)

#### Ejercicio 2

- Complementando tus resultados del ejercicio 1. Imagina que queremos darle la funcionalidad a nuestro _"reproductor musical"_ de poder integrar plug-ins a él. Estos plug-ins se encargan de **agregar nueva funcionalidad** al reproductor musical, como por ejemplo, mostrar las letras de una determinada canción, decirte pistas relacionadas al género de la canción, devolverte la información del artista material de la canción, o hasta customizar el reproductor musical a que tenga una imágen de fondo, etcétera
- Implementa el patrón de diseño decorador, de tal manera que podamos **"decorar"** nuestras instancias de la clase `ReproductorMusical` con `Plugins`
  - Al menos dos plugins con diferente funcionalidad entre si necesitan agregarse en este punto
  - Puedes implementar esto con el patrón de diseño desde 0, o bien, utilizando los decoradores nativos de `Python`, como a ti se te haga más sencillo :wink:

#### Ejercicio 3

_Pendiente..._

#### Ejercicio 4

_Pendiente..._

#### Ejercicio 5

_Pendiente..._

## Puntos Extra

- Implementa la suite de tests unitarios para el **Ejercicio 1**. En esta suite se deben de probar al menos 10 posibles casos de prueba para el comportamiento de una instancia de la clase `ReproductorMusical` -> _(5 puntos sobre 100)_
