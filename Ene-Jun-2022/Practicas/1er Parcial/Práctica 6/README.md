# Práctica 6

## Objetivo

- Mejorar en el aprendizaje y conocimiento sobre patrones de diseño
- Mejorar en el manejo y uso de la filosofía `T.D.D.` y su mantra `Red-Green-Refactor`

## Especificaciones

Resuelve los siguientes ejercicios propuestos utilizando los patrones de diseño correspondientes.

Asegúrate de generar las respectivas pruebas unitarias que satisfagan la implementación propuesta para cada patrón. Idealmente deberías de seguir la filosofía `T.D.D.`, pero puedes sentirte libre de hacerlo de la manera contraria, siempre y cuando adjuntes la suite de pruebas unitarias para cada ejercicio.

### Ejercicio 1

**Composite Pattern:** <https://refactoring.guru/es/design-patterns/composite>.

Suponga que tiene un sistema de archivos tipo [UNIX](http://math.uprm.edu/~luis/courses/unix/images/jerarquia.gif). El funcionamiento de este tipo de sistema de archivos es comúnmente representado por medio de una estructura de datos de tipo árbol jerárquico. Cada directorio puede contener 0 o varios directorios, pero también 0 o varios archivos. El principal objetivo es moverse a través del sistema de archivos de manera sencilla, mientras se puede tener ubicado cada archivo a través de una ruta, justo como se haría si te movieras a través de la misma terminal.

Partiendo del código inicial en el archivo [composite.py](composite.py), implementa el patrón de diseño `Composite` para ilustrar este ejemplo.

### Ejercicio 2

**Prototype Pattern:** <https://refactoring.guru/es/design-patterns/prototype>.

Partiendo del código base en el archivo [prototype.py](prototype.py), supongamos que se crea una instancia de la clase `Oveja` con el nombre de `Dolly`, ¿qué lógica de código necesitaríamos implementar para poder clonar a esta instancia de la clase `Oveja`?

Implementa el patrón de diseño `Prototype` para ilustrar este ejemplo.

### Ejercicio 3

**Template Method Pattern:** <https://refactoring.guru/es/design-patterns/template-method>.

Implementa el patrón de diseño `Templated Method` para el siguiente diagrama UML:

![Templated Method](template-method.png)

### Ejercicio 4

**Visitor Pattern:** <https://refactoring.guru/es/design-patterns/visitor>.

...

### Ejercicio 5

**Factory Method Pattern:** <https://refactoring.guru/es/design-patterns/factory-method>.

Implementa el patrón de diseño `Factory Method` para el diagrama UML propuesto en la sección de "_Pseudocódigo_" de la página de Refactoring Guru.

## Deadline

- `Domingo 13 de Marzo a las 11:59pm`
