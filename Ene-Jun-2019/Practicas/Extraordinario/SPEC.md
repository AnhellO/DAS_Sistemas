# Ordinario

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Extraordinario/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request hasta la hora límite (`05:00am` del `Junio 2, 2019`) para evitar que este sea copiado :wink:

## Ejercicios

### Patrones de Diseño

#### Ejercicio 1

Para el ejemplo de código en el archivo [composite.py](composite.py):

* Implementa la funcionalidad necesaria utilizando el patrón de diseño [Composite`](https://sourcemaking.com/design_patterns/composite) para que sea posible crear una interfaz gráfica sencilla que contenga múltiples componentes, como sucedería en una GUI real.
  * Algunos componentes pueden contener otros componentes, pero también hay componentes que no pueden/tengan que contener más componentes
  * Deberás de tomar la siguiente [imagen de ejemplo](https://semantic-ui.com/images/examples/login.png) como caso de prueba para tu implementación del patrón `composite`
  * Ejemplo:
  ```
    Componente 'Ventana' contiene 'Imagen'
    Componente 'Imagen': imagen.jpg
    Componente 'Ventana' contiene 'Etiqueta'
    Componente 'Etiqueta': "Log-in to your account"
    Componente 'Ventana' contiene 'Panel'
    Componente 'Panel' contiene 'Input'
    Componente 'Panel' contiene 'Input'
    Componente 'Panel' contiene 'Botón'
    Componente 'Botón' contiene 'Etiqueta'
    ...
  ```

#### Ejercicio 2

Para el ejemplo de código en el archivo [ocp.py](ocp.py):

* Analiza y refactoriza el código para utilizar el `Open/Closed Principle` de manera correcta
* Explica la lógica implementada detrás de tu enfoque
* Con base en el código/enfoque original y en los cambios que realizaste, contesta a las siguientes preguntas (puedes contestarlas con comentarios dentro de tu código):
  * ¿Qué pasaría si quisieramos sumar las áreas de otros tipos de figuras?
  * ¿Qué tendríamos que hacer para ahora poder sumar volúmenes además de las áreas?

#### Ejercicio 3



#### Ejercicio 4




#### Deadline

* `2019-06-07 03:00am`