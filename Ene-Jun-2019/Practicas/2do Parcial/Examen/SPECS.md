# 2do. Examen Parcial

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Segundo Parcial/..`
* Cada ejercicio deberá estar en una carpeta por separado, es decir `../Segundo Parcial/Ejercicio 1/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request ni hagas commit de tu código hasta la hora límite (`2:00am` de hoy `Mayo 16, 2019`) para evitar que este sea copiado :wink:

## Ejercicios

#### Ejercicio 1

* Para el ejemplo de código en el archivo [srp.py](srp.py):
  * Analiza y refactoriza el código para utilizar el `Single Responsibility Principle` de manera correcta
  * Explica la lógica implementada detrás de tu enfoque
  * Con base en el código/enfoque original y en los cambios que realizaste, contesta a las siguientes preguntas (puedes contestarlas con comentarios dentro de tu código):
    * ¿Qué sucedería si quiero agregar otro formato de serialización más complejo como `XML` o `Yaml`?
    * ¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase `Usuario`?

#### Ejercicio 2

* Utilizando la siguiente API https://randomuser.me/:
  * Crea un script en `python` que obtenga al menos 100 **diferentes (únicos, no repetidos)** usuarios de la API
  * Al final todos los usuarios obtenidos desde la API deberán de guardarse juntos en un solo archivo JSON

#### Ejercicio 3

* Partiendo del archivo JSON que generaste en el ejercicio anterior:
  * Modela y crea una base de datos en `SQLite` que se encargue de almacenar los usuarios existentes en el archivo JSON
  * Crea un nuevo script en `python` que lea y procese el archivo JSON resultante para insertar los usuarios obtenidos desde la API en la base de datos

#### Ejercicio 4

* Utilizando solamente `SQL`, realiza las siguientes consultas a la base de datos resultante después de almacenar toda la información necesaria:
  1. Obtener/seleccionar todos los emails existentes en la base de datos
  2. Contar cuantas mujeres existen al final en la base de datos
  3. Contar cuantos hombres existen al final en la base de datos
  4. Obtener todos usuarios existentes en la base de datos mostrando solamente su nombre completo, su email, y su dirección
* Crea un archivo `.sql` con las consultas resultantes