# 1er. Examen Parcial

## Especificaciones y Requerimientos

- Para las partes teóricas, contesta sobre las hojas en blanco provistas para el examen
- Para las partes prácticas, desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta de práctica en este caso tendría que llamarse `../Primer Parcial/..`
- Total Parte Teórica: 50%
- Total Parte Práctica: 50%

## Parte Teórica

1. ¿Qué es una Clase?
2. ¿Qué es un Atributo?
3. ¿Qué es una Función?
4. ¿Qué es un Objeto?
5. ¿Qué es la Herencia?
6. ¿Qué es una Interface?
7. ¿Qué es UML?
8. Ejemplifica un diagrama de clases
9. Ejemplifica un diagrama de objetos
10. ¿Qué es un patrón de diseño de software?
11. Mencione el objetivo de los patrones de diseño creacionales
12. Mencione 1 patrón creacional y sus objetivos (que busca solucionar)
13. Mencione el objetivo de los patrones de diseño estructurales
14. Mencione 1 patrón estructural y sus objetivos (que busca solucionar)
15. Mencione el objetivo de los patrones de diseño de comportamiento
16. Mencione 1 patrón de comportamiento y sus objetivos (que busca solucionar)

## Parte Práctica

* Suponga que tiene un sistema de archivos tipo [UNIX](http://math.uprm.edu/~luis/courses/unix/images/jerarquia.gif). El funcionamiento de este tipo de sistema de archivos es comúnmente representado por medio de un árbol jerárquico. Cada directorio puede contener 0 o varios directorios, pero también 0 o varios archivos. El principal objetivo es moverse a través del sistema de archivos de manera sencilla, mientras se puede tener ubicado cada archivo a través de una ruta
  * Implemente el patrón Composite en python para ilustrar este ejemplo
  * Agregue los respectivos diagramas UML de clases que reflejen la solución

* Suponga que se está construyendo una librería de clases para representar componentes de GUI. Se ha decidido que en vez de que un programador defina la posición de los componentes GUI (Button, List, Dialog, etcétera) sobre una ventana, se incluyan manejadores de disposición de componentes (layout manager), cada uno de los cuales distribuye un conjunto dado de componentes gráficos de acuerdo a algún esquema de distribución: horizontalmente, verticalmente, en varias filas, en forma de una matriz, etcétera. Debe ser posible cambiar en tiempo de ejecución la distribución elegida inicialmente. Suponga que la clase Panel (Cliente) es la que representa a un contenedor de componentes gráficos, diseña una solución para introducir en la librería los manejadores de componentes (layouts)
  * Implemente el patrón Strategy en python para dar solución a este ejemplo
  * Agregue los respectivos diagramas UML de clases que reflejen la solución

## Puntos Extra

* Menos W.E.T. y más D.R.Y.
* Implementa el patrón FactoryMethod sobre el ejercicio práctico 2 para crear diferentes objetos layout