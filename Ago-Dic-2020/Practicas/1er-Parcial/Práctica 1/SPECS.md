# Práctica 1

## Objetivo

* Mejorar en el manejo de las estructuras básicas de control y de flujo de Python
* Mejorar en el manejo de listas y listas comprimidas
* Comenzar a involucrarse con el manejo de clases y objetos

## Especificaciones

Dada una cadena que representa una matriz de números, devuelve las filas y las columnas requeridas para esa matriz.

Por ejemplo, dada la siguiente cadena con saltos de línea en ella:

```python
9 8 7
5 3 2
6 6 7
```

y que representa a la siguiente matriz:

```python
    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7
```

tu código debe de ser capaz de imprimir lo siguiente:

* Una lista de las filas en base al número de fila provisto, partiendo desde el índice 0 y leyendo cada fila de izquierda a derecha y de arriba hacia abajo
* Una lista de las columnas en base al número de columna provisto, partiendo desde el índice 0 y leyendo cada columna de arriba a abajo y de izquierda a derecha

Dicho esto, las filas para nuestra matriz de ejemplo serían las siguientes:

```python
9, 8, 7
5, 3, 2
6, 6, 7
```

y sus columnas serían:

```python
9, 5, 6
8, 3, 6
7, 2, 7
```

Si el número de fila solicitado fuera `1`, yo imprimiría una nueva lista con lo siguiente:

```python
[9, 8, 7]
```

mientras que si el número de columna requerido fuera `2`, mi resultado sería:

```python
[8, 3, 6]
```

Para este ejercicio necesitas hacer uso de clases. Puedes partir del esqueleto de código que está en el archivo de [matrix.py](matrix.py) si así lo deseas.

Si tienes dudas sobre el tema de clases, puedes consultar más sobre ellas en el libro de python de la clase, o bien darles un vistazo a los links provistos en la sección de recursos.

## Recursos

* <https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes>
* <https://realpython.com/python3-object-oriented-programming/#how-to-define-a-class-in-python>
* <https://docs.python.org/3/tutorial/datastructures.html>
* <https://www.w3schools.com/python/python_ref_string.asp>

## Deadline

* `Domingo 6 de Septiembre a las 12:00pm`
