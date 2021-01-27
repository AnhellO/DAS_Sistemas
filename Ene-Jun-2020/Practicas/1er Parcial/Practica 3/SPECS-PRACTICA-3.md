# Práctica 3

## Objetivo

* Conocer más a fondo sobre los patrones de diseño con ejercicios aplicados a  algunos de los patrones existentes
* Resolver los ejercicios propuestos haciendo correcto uso del patrón indicado para cada uno

## Especificaciones

#### Ejercicio 1

Partiendo del ejemplo de código en el archivo [prototype.py](prototype.py), supongamos que se crea una instancia de la clase `Oveja`  con nombre `Dolly`, ¿qué lógica de código necesitaríamos implementar para poder clonar a esta instancia de la clase `Oveja`?.

Implementa el patrón de diseño [Prototype](https://sourcemaking.com/design_patterns/prototype) para ilustrar este ejemplo. Este patrón nos permite crear copias de objetos existentes independientemente de su clase, y así poder modificar las nuevas copias a necesidad

#### Ejercicio 2

Suponga que tiene un sistema de archivos tipo [UNIX](http://math.uprm.edu/~luis/courses/unix/images/jerarquia.gif). El funcionamiento de este tipo de sistema de archivos es comúnmente representado por medio de una estructura de datos de tipo árbol jerárquico. Cada directorio puede contener 0 o varios directorios, pero también 0 o varios archivos. El principal objetivo es moverse a través del sistema de archivos de manera sencilla, mientras se puede tener ubicado cada archivo a través de una ruta, justo como ser haría si te movieses dentro de la misma terminal.

Partiendo del ejemplo de código en el archivo [composite.py](composite.py), implementa el patrón de diseño [Composite](https://sourcemaking.com/design_patterns/composite) para ilustrar este ejemplo. Este patrón nos describe a un conjunto de objetos que se tratan de la misma manera que una instancia individual del mismo tipo de objeto

#### Ejercicio 3

Partiendo del ejemplo de código en el archivo [chain-of-responsibility.py](chain-of-responsibility.py), imaginemos que existen varias formas de pago disponibles en una cuenta, y que cada una tiene un balance/monto específico. Si deseamos comprar un artículo que cuesta $200, pero en determinada forma de pago solamente tenemos disponible un balance de $150, ¿cómo podemos implementar la lógica en el programa de tal manera que podamos llevar a cabo la compra del artículo con alguna de las otras cuentas y formas de pago que tenemos disponibles?.

Apóyate del patrón de diseño [Chain of Responsibility](https://sourcemaking.com/design_patterns/chain_of_responsibility) para darle solución al problema planteado anteriormente. Este patrón nos plantea que podemos crear una cadena de objetos de tal manera que una petición/input inicial pase de un objeto a otro hasta que exista un objeto que satisfaga la petición original.

## Requisitos Adicionales

* Explica con comentarios dentro del mismo código la lógica utilizada detrás de tus soluciones propuestas

## Deadline

* `Domingo 15 de Marzo a las 10:00pm`