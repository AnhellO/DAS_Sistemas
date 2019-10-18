# 1er. Examen Parcial

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Primer Parcial/..`
* Cada ejercicio deberá estar en una carpeta por separado, es decir `../Primer Parcial/Ejercicio 1/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request ni hagas commit de tu código hasta la hora límite (`01:00am` de mañana `Octubre 18, 2019`) para evitar que este sea copiado :wink:

## Ejercicios

#### Ejercicio 1 - OOP Basics

* Crea una clase base abstracta `Vehiculo`. De esta clase heredarán las clases `Automovil`, `Avion` y `Barco`:
  * Agrega la función abstracta `traslado()` en la clase `Vehiculo` y sobreescribela en cada una las clases hijas con una funcionalidad específica
  * Para cada clase sobreescribe la función `__str__`, de tal manera que podamos obtener una representación del objeto como string
  * Crea la función `main` en la cual instancies y juegues con al menos 5 objetos diferentes (en total) para cada una de las clases pedidas anteriormente
  * Crea una función dentro de tu test principal la cual reciba como parámetros una lista de objetos tipo vehículo y un tipo en específico (ya sea 'marítimo', 'terrestre' o 'aéreo'), y devuelva una nueva lista filtrada con los objetos del tipo especificado en el segundo parámetro

#### Ejercicio 2 - Command Pattern

* Para el ejemplo de código en el archivo [command.py](command.py):
  * Implementa la funcionalidad necesaria utilizando el patrón de diseño `Command` para poder llevar a cabo cada de unas de las acciones de la televisión por medio de la clase `ControlRemoto`
  * Ejemplo al encender la televisión:
    * `Encendida!`
  * De acuerdo al patrón de diseño `Command`, debemos de tener la posibilidad de deshacer la acción realizada. Implementa la funcionalidad necesaria para poder deshacer cada acción llevada a cabo con la televisión

#### Ejercicio 3

* Coming soon...

#### Ejercicio 4

* Coming soon...

## Puntos extra sobre el parcial (1 por ejercicio extra :wink:)

* Implementa tus soluciones de manera simple y sencilla por medio del estilo `syntactic sugar` de Python
