# Práctica 5

## Objetivo

- Mejorar en el aprendizaje y conocimiento sobre `Python` y `POO`
  - Manejo de interfaces, clases abstractas y herencia en Python

## Especificaciones

### Parte 1 - Lectura

Lee algunos o todos los artículos que se adjuntan a continuación.

- <https://realpython.com/python-interface/>
- <https://www.godaddy.com/engineering/2018/12/20/python-metaclasses/>
- <https://www.analyticslane.com/2020/10/05/clases-abstractas-en-python/>
- <https://ellibrodepython.com/abstract-base-class>
- <https://rico-schmidt.name/pymotw-3/abc/index.html>
- <https://docs.python.org/es/dev/library/abc.html>

### Parte 2 - Práctica

Resuelve los siguientes ejercicios haciendo uso del conocimiento adquirido previamente en la parte 1.

#### Ejercicio 1

Partiendo del siguiente código base:

```python
from abc import ABC, abstractmethod
 
class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass
```

Sobrescribe el método abstracto `num_of_sides` para los siguientes tipos de figuras:

- Triángulo
- Cuadrado
- Pentágono
- Hexágono

#### Ejercicio 2

Partiendo de las clases propuestas en el siguiente ejemplo de código:

```python
class Human:
    def move(self):
        print("I can walk and run")
 
class Snake:
    def move(self):
        print("I can crawl")
 
class Dog:
    def move(self):
        print("I can bark")
 
class Lion:
    def move(self):
        print("I can roar")
```

Genera un nivel de abstracción mayor en el que todas las clases compartan una única clase abstracta en común. ¿Cómo llevarías esto a cabo?

#### Ejercicio 3

Toma el ejemplo de código propuesto a continuación:

```python
import abc
from abc import ABC, abstractmethod
 
class A(ABC):
    def print_function(self):
        print("Abstract Base Class")

class B(A):
    def print_function(self):
        super().print_function()
        print("subclass")

```

Realizando las modificaciones pertinentes, ¿cómo podríamos obtener la siguiente salida?:

```shell
Abstract Base Class
Subclass
```

## Deadline

- `Domingo 13 de Marzo a las 11:59pm`
