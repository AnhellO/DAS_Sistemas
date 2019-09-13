# 1er. Examen Parcial

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Primer Parcial/..`
* Cada ejercicio deberá estar en una carpeta por separado, es decir `../Primer Parcial/Ejercicio 1/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request ni hagas commit de tu código hasta la hora límite (`12:00pm` de hoy `Febrero 28, 2019`) para evitar que este sea copiado :wink:

## Ejercicios

#### Ejercicio 1

* Elabore una clase `Figura`. De esta clase heredarán las clases `Circulo`, `Triangulo` y `Rectangulo`:
  * Para cada clase, agregar la función `area`
  * Para cada clase, sobreescribe la función `__str__`, para poder obtener una representación del objeto como string
  * Para finalizar, crean la función (`main`), en la cual instancies y juegues con al menos 5 objetos diferentes (en total) para cada una de las clases pedidas anteriormente

#### Ejercicio 2

* Implementa el patrón de diseño `Factory Method` tomando como referencia el ejercicio anterior, de tal manera que podamos crear múltiples instancias/figuras dentro de la misma función `main`, pero ahora utilizando la factoría.
  * Re-utiliza todo tu código existente, pero dentro de un nuevo archivo
  * Crea al menos 5 nuevas instancias de diferente tipo, pero por medio del `Factory`

#### Ejercicio 3

* Para el ejemplo de código en el archivo [facade.py](facade.py):
  * Implementa la funcionalidad necesaria utilizando el patrón de diseño `Facade` para poder **prender**, **apagar**, y **reiniciar** una instancia de la clase `Computadora`
  * Ejemplo al prender la computadora:
    * `Click!`
    * `Pzzzzzzzt!`
    * `Beep Beep!`
    * `Inicializando componentes...`
    * `...`
    * `Listo!`
  * Explica la lógica implementada detrás de tu enfoque

#### Ejercicio 4

* Para el ejemplo de código en el archivo [strategy.py](strategy.py):
  * Implementa la funcionalidad necesaria utilizando el patrón de diseño `Strategy` para que se puedan jugar los 4 niveles del videojuego con los tres diferentes personajes **en una sola ejecución** del programa
  * Ejemplo para un personaje:
    * `Jugamos nivel 1 con Bowser: Fire!`
    * `Jugamos nivel 2 con Bowser: Shell!`
    * `Jugamos nivel 3 con Bowser: Big Fire!`
    * `Jugamos nivel final con Bowser: Fire! Shell! Big Fire!`
  * Explica la lógica implementada detrás de tu enfoque

## Puntos extra sobre el parcial (1 por ejercicio extra :wink:)

* Implementa tus soluciones de manera simple y sencilla por medio del estilo `syntactic sugar` de Python
* Implementa el patrón de diseño `Builder` para poder crear instancias de la clase `Computadora` del ejercicio 1 con diferentes componentes
