# Práctica 2

## Objetivo

* Conocer más a fondo sobre los patrones de diseño con ejercicios de algunos de los patrones existentes
* Resolver los 5 ejercicios propuestos

## Especificaciones

1. Para el ejemplo de código en el archivo [factory-method.py](factory-method.py):

* Implementa la funcionalidad necesaria utilizando el patrón de diseño [Factory Method](https://sourcemaking.com/design_patterns/factory_method) para que sea posible traducir una o varias palabras en base al idioma requerido.
  * Las palabras y el idioma a traducir tendrán que ingresarse a través de la terminal/consola
  * Ejemplo:
  ```
    dog griego # Entrada
    Palabra "dog" traducida al griego: σκύλος # Salida
  ```

2. Para el ejemplo de código en el archivo [decorator.py](decorator.py):

* Implementa la funcionalidad necesaria utilizando el patrón de diseño [Decorador](https://sourcemaking.com/design_patterns/decorator) para que el texto también pueda ser impreso de las siguientes maneras en HTML:
  * Resaltado: `<b>Texto</b>`
  * Cursiva: `<i>Texto</i>`
  * Subrayado: `<u>Texto</u>`
  * El texto deberá de poder mostrarse con uno o varios de los formatos especificados
  * Ejemplo:
  ```
    ¡Texto Normal!
    <b>¡Texto Resaltado!</b>
    <b><u>¡Texto Resaltado y Subrayado!</u></b>
    <b><u><i>¡Aplicando todos los formatos!</i></u></b>
  ```

3. Para el ejemplo de código en el archivo [builder.py](builder.py):

* Implementa la funcionalidad necesaria utilizando el patrón de diseño [Builder](https://sourcemaking.com/design_patterns/builder) para poder crear "Hochos" y "Burguers" al gusto del comenzal :smile:
  * Ejemplo:
    * Para una hamburguesa vegetariana:
   		```
   		Preparamamos el pan!
   		Agregamos las verduras!
   		Agregamos los condimentos!
   		La hacemos combo!
   		```

4. Para el ejemplo de código en el archivo [memento.py](memento.py):

* Implementa la funcionalidad necesaria utilizando el patrón de diseño [Memento](https://sourcemaking.com/design_patterns/memento) para que se pueda salvar el estado anterior del editor de texto, tal y como lo haría un editor real con el famoso "`Undo`". Debe de ser posible salvar ese estado, y regresar a el en cualquier momento durante la ejecución.

5. Suponga que tiene un sistema de archivos tipo [UNIX](http://math.uprm.edu/~luis/courses/unix/images/jerarquia.gif). El funcionamiento de este tipo de sistema de archivos es comúnmente representado por medio de una estructura de datos de tipo árbol jerárquico. Cada directorio puede contener 0 o varios directorios, pero también 0 o varios archivos. El principal objetivo es moverse a través del sistema de archivos de manera sencilla, mientras se puede tener ubicado cada archivo a través de una ruta, justo como ser haría si te movieses dentro de la misma terminal.

* Implementa el patrón de diseño [Composite](https://sourcemaking.com/design_patterns/composite) para ilustrar este ejemplo.

## Requisitos
* Resolver todos los ejercicios utilizando `Python3`
* Explica con comentarios dentro del mismo código la lógica utilizada detrás de tus soluciones propuestas
* Enviar la práctica siguiendo los lineamientos del repositorio: [https://github.com/AnhellO/DAS_Sistemas/blob/development/README.md](https://github.com/AnhellO/DAS_Sistemas/blob/development/README.md)

## Fecha Límite

* `23:59 2019-03-02`