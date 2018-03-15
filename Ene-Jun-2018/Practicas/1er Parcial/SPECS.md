# 1er. Examen Parcial

## Especificaciones y Requerimientos

- Para las partes teóricas, contesta sobre las hojas en blanco provistas para el examen
- Para las partes prácticas, desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta de práctica en este caso tendría que llamarse `../Primer Parcial/..`
- Total Parte Teórica: 50%
- Total Parte Práctica: 50%

## Parte Teórica

### OOP

- ¿Qué es una Clase?
- ¿Qué es un Atributo?
- ¿Qué es una Función?
- ¿Qué es un Objeto?
- ¿Qué es la Herencia?
- ¿Qué es una Interface?
- ¿Qué es UML?
- Ejemplifica un diagrama de clases
- Ejemplifica un diagrama de objetos
- ¿Qué es un patrón de diseño de software?
- Mencione el objetivo de los patrones de diseño creacionales
- Mencione 1 patrón creacional y sus objetivos (que busca solucionar)
- Mencione el objetivo de los patrones de diseño estructurales
- Mencione 1 patrón estructural y sus objetivos (que busca solucionar)
- Mencione el objetivo de los patrones de diseño de comportamiento
- Mencione 1 patrón de comportamiento y sus objetivos (que busca solucionar)

## Parte Práctica

- Suponga que tiene un sistema de archivos tipo UNIX: http://math.uprm.edu/~luis/courses/unix/images/jerarquia.gif
  - El funcionamiento de este tipo de sistema de archivos es comúnmente representado por medio de un árbol jerárquico
  - Cada directorio puede contener 0 o varios directorios, pero también 0 o varios archivos
  - Implemente el patrón Composite en python para dar solución a este ejemplo
  - Agregue los respectivos diagramas UML de clases que reflejen la solución

- Suponga que se está construyendo una librería de clases para representar componentes de GUI. Se ha decidido que en vez de que un programador defina la posición de los componentes GUI (Button, List, Dialog, etcétera) sobre una ventana, se incluyan manejadores de disposición de componentes (layout manager), cada uno de los cuales distribuye un conjunto dado de componentes gráficos de acuerdo a algún esquema de distribución: horizontalmente, verticalmente, en varias filas, en forma de una matriz, etcétera. Debe ser posible cambiar en tiempo de ejecución la distribución elegida inicialmente. Suponga que la clase Panel (Cliente) es la que representa a un contenedor de componentes gráficos, diseña una solución para introducir en la librería los manejadores de componentes (layouts)
  - Implemente el patrón Strategy en python para dar solución a este ejemplo
  - Agregue los respectivos diagramas UML de clases que reflejen la solución

## Puntos Extra

- Menos W.E.T. y más D.R.Y.
- Implementa el patrón FactoryMethod sobre el ejercicio práctico 1 para crear objetos empleado