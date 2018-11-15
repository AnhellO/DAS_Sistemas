# 1er. Examen Parcial

## Especificaciones y Requerimientos

#### Ejercicio 1

* Elabore una clase `Instrumento Musical`. De esta clase heredarán las clases `Guitarra` y `Batería`:
  * Para cada clase, agregar como mínimo 3 atributos y 2 funciones (aparte de los setters/getters)
  * Para cada clase, sobreescribe la función `__str__`
  * Para finalizar, elabora una clase principal (main), en la cual crees y juegues con al menos 5 instancias diferentes para cada una de las clases pedidas anteriormente

#### Ejercicio 2

* Para el ejemplo de código en el archivo [decorator.py](decorator.py):
  * Implementa la funcionalidad necesaria utilizando el patrón de diseño `Decorador` para que se le pueda agregar leche, vainilla, y/o canela al cafecito, y para que se pueda modificar su precio original en base a los ingredientes agregados
  * Ejemplo:
    * `Cafecito! con Vainilla! A solo 32 pesitos!`
    * `Cafecito! con Leche! A solo 28 pesitos!`
    * `Cafecito! con Canela! A solo 30 pesitos!`
    * `Cafecito! con Leche! con Canela! A solo 33 pesitos!`
  * Puedes utilizar los decoradores nativos de Python :wink:
  * Explica la lógica implementada detrás de tu enfoque

#### Ejercicio 3

* Para el ejemplo de código en el archivo [iterator.py](iterator.py):
  * Implementa la funcionalidad necesaria utilizando el patrón de diseño `Iterator`:
    * Para poder eliminar estaciones de radio del contenedor `Estaciones`
    * Para poder recorrer/iterar la lista de estaciones de radio por medio del ciclo `for` comentado en el ejemplo de código
  * Ejemplo:
    * Antes de borrar:
	    ``` python
	    89.9
	    101.2
	    102.3
	    100.4
	    ```
	* Después de borrar `x` elemento:
		``` python
	    101.2
	    102.3
	    100.4
		```
  * Puedes utilizar los iteradores nativos de Python :wink:
  * Explica la lógica implementada detrás de tu enfoque

#### Puntos extra sobre el parcial (1 punto por ejercicio extra :wink:)

* Implementa el patrón de diseño `Factory Method` sobre la creación de objetos del **Ejercicio 1**
* Para el ejemplo de código en el archivo [builder.py](builder.py), implementa la funcionalidad necesaria utilizando el patrón de diseño `Builder` para poder crear hochos y burguers al gusto del comenzal :smile:
  * Ejemplo:
    * Para una burguer vegetariana:
   		``` python
   		Preparamamos el pan!
   		Agregamos las verduras!
   		Agregamos los condimentos!
   		La hacemos combo!
   		```
