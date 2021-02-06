# Práctica 1

## Objetivo

* Mejorar en el manejo de las estructuras básicas de control y de flujo de Python
* Mejorar en el manejo de listas
* Mejorar en el manejo de clases y objetos

## Especificaciones

### Parte 1

Crea una clase `Vehiculo` que cumpla con los siguientes puntos:

* Que tenga los atributos de instancia `velocidad_maxima`, `kilometraje` y `capacidad`
* Que tenga un atributo de clase llamado `random` con cualquier valor
* Que implemente la función nativa de Python para poder obtener una representación en `string` de un objeto instanciado de la clase

### Parte 2

Crea una clase `Autobus` que herede de la clase `Vehiculo` de la parte anterior:

* Añade una función `tarifa()`, en donde el cargo de tarifa predeterminado de cualquier vehículo es igual a la `capacidad de asientos del vehículo x 100`. Si el vehículo es una instancia de autobús, debemos agregar un **10%** adicional a la tarifa completa como cargo de mantenimiento. Entonces, la tarifa total por instancia de autobús será igual a `monto final = tarifa total + 10% de la tarifa total`

### Parte 3

Mediante la función `main()`, crea una lista que contenga varias instancias de las clases de `Vehiculo` y de la clase `Autobus`, e iterala a través de un ciclo, llevando a cabo la siguiente evaluación:

* Si el objeto es una instancia de la clase `Autobus` entonces imprime el mensaje `"Soy un autobús! -> {informacion del autobus}"`
* En caso contrario no imprimas ningún mensaje y continua iterando la lista

## Recursos

* <https://www.freecodecamp.org/espanol/news/python-if-name-main/>
* <https://docs.python.org/es/3/tutorial/classes.html>
* <https://realpython.com/python3-object-oriented-programming>
* <https://docs.python.org/3/tutorial/datastructures.html>
* <https://www.w3schools.com/python/python_ref_string.asp>

## Deadline

* `Sábado 13 de Febrero a las 11:00pm`
