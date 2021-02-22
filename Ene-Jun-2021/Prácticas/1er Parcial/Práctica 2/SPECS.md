# Práctica 2

## Objetivo

* Desarrollar la capacidad de análisis y de solución de problemas de programación orientada a objetos
* Expandir conocimientos sobre el tema de patrones de diseño de software orientado a objetos
* Comenzar a involucrarse con el uso de [T.D.D.](https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas)

## Especificaciones

Supón que estás desarrollando un videojuego en donde puedes crear un personaje principal al inicio de la historia. A este personaje principal le pueden ser equipados múltiples aditamentos que funcionan para mejorarlo.

Inicialmente tu personaje no tiene ningún aditamento, pero después puedes agregarle una armadura y/o también una espada. Ambos aditamentos pueden ser agregados juntos o por separado, y de igual manera más aditamentos extras pueden crearse/agregarse para el personaje.

Lo anterior se resume a que nuestro personaje puede ser "_wrappeado_" por aditamentos extra que funcionan como mejora para él.

## Parte 1

Implementa la solución para el problema propuesto en las especificaciones utilizando el patrón de diseño decorador desde 0, es decir, implementando la interfaz y las clases necesarias que forman parte del [diagrama UML del patrón](decorator-uml.png).

La suite de pruebas unitarias debe de pasar sin problema alguno y esta **NO** debe de ser modificada por tu propia cuenta.

## Parte 2

Agrega **2** aditamentos extra para el personaje, como un anillo de magia, un collar de protección contra magia o un escudo.

En esta ocasión **SÍ** podrás y tendrás que modificar las pruebas unitarias, de tal manera que agregues un par de funciones de prueba para el nuevo par de aditamentos que añadiste.

## Parte 3

Implementa la misma solución pero ahora utilizando los [decoradores nativos de python](https://pythones.net/decoradores-en-python-oop/). Esta solución tendrá que ser creada en un archivo por separado, y tendrás que utilizar la misma suite de tests unitarios que ya está existente para realizar pruebas unitarias de este nueva solución.

Al igual que con la parte 1 y para esta parte en concreto, la suite de pruebas unitarias debe de pasar sin problema alguno y ya no debería ser modificada ni alterada de nuevo (con excepción de la parte 2 en donde se agregaron nuevas funciones de prueba).

## Parte 4

Lee sobre el patrón de diseño [Composite](https://refactoring.guru/es/design-patterns/composite).

Anexa un archivo [Markdown](https://es.wikipedia.org/wiki/Markdown) con una síntesis de qué es lo que entendiste sobre este patrón de diseño y cómo es que funciona :wink:.

## Recursos

* <https://refactoring.guru/design-patterns/decorator>
* <https://refactoring.guru/es/design-patterns/decorator/>
* <https://www.tutorialspoint.com/design_pattern/decorator_pattern.htm>
* <https://sourcemaking.com/design_patterns/decorator>
* <https://python-patterns.guide/gang-of-four/decorator-pattern/>
* <https://www.genbeta.com/desarrollo/patrones-de-diseno-decorator>
* <https://realpython.com/primer-on-python-decorators/>
* <https://codigofacilito.com/articulos/decoradores-python>
* <https://recursospython.com/guias-y-manuales/decoradores/>

## Deadline

* `Domingo 28 de Febrero a las 11:59pm`
