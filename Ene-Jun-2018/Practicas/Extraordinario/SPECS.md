# Examen Extraordinario

## Especificaciones y Requerimientos

- Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta en este caso tendría que llamarse `../Extraordinario/..`
- Total Práctico: 100%

1. Para el ejemplo de código en el archivo [decorator.py](decorator.py):

* Implementa la funcionalidad necesaria para que el texto también pueda ser impreso de las siguientes maneras en HTML:
  * Resaltado: `<b>Texto</b>`
  * Cursiva: `<i>Texto</i>`
  * Subrayado: `<u>Texto</u>`
  * El texto deberá de poder imprimirse con uno o varios de los formatos especificados
  * Ejemplo:
  ```
    ¡Texto Normal!
    <b>¡Texto Resaltado!</b>
    <b><u>¡Texto Resaltado y Subrayado!</u></b>
    <b><u><i>¡Aplicando todos los formatos!</i></u></b>
  ```
* Explica la lógica implementada detrás de tu enfoque

2. Para el ejemplo de código en el archivo [prisoner.py](prisoner.py):

* Refactoriza implementando el `Liskov Substitution Principle`
* Explica el porqué de tus cambios

## Puntos Extra

* Menos W.E.T. y más D.R.Y.
* Implementa un breve ejemplo del `Dependency Inversion Principle` utilizando el módulo de [python-dependency-injector](https://github.com/ets-labs/python-dependency-injector) utilizando instrumentos musicales como objetos