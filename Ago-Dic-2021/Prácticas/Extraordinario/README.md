# Examen Extraordinario

## Previo

* Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing)
* La carpeta del examen tendrá que llamarse `../Extraordinario/..`

## Especificaciones

Este ejercicio va a consistir en conectarnos con la [API de GitHub](https://docs.github.com/en/rest).

Queremos descargar y almacenar en una base de datos todos los issues del repositorio de <https://github.com/pallets/flask> que contengan la etiqueta/label de `bug`. Los campos que nos interesan son los siguientes:

* URL real del issue (la que se puede visitar desde GitHub)
* Título del issue
* Número del issue
* Nombre del autor del issue
* Lista de todas las tags para ese issue ('`bug`' debe de estar entre esas etiquetas, pero puede haber más etiquetas como la etiqueta 'docs' por ejemplo)
* Estado del issue
* Título del milestone al que pertenece
* Descripción del milestone al que pertenece

Finalmente debemos de ejecutar una lectura a la base de datos con la cual obtengamos todos los issues desde la base de datos y los imprimamos uno por uno a terminal con el siguiente formato:

``` bash
****** Issue #1902 ******
- URL: <https://github.com/pallets/flask/issues/1902>
- Título: 'Import error with some examples'
- Autor: 'rnelsonchem'
- Tags: ['bug', 'cli', 'docs']
- Estado: 'closed'
- Milestone
  - Título: '1.0'
  - Descripción: ''
```

### Requerimientos

* Utiliza `Python` como lenguaje principal de programación
* Para almacenar los datos puedes utilizar cualquiera de los motores de bases de datos vistos en clase: `MySQL`, `PostgreSQL`, `Redis` o `MongoDB`
* Agrega tests unitarios y/o funcionales
* Agrega documentación y comentarios en el código
* Dockeriza el proyecto
* Adjunta un archivo `SOLUTION.md` que contenga una descripción de tu solución junto con las instrucciones para poder probarlo
* Tu decides como arquitecturar el proyecto, pero debes de adjuntar un diagrama de como lo arquitecturaste y explicar el por qué de hacerlo de X o Y manera. Asegúrate de adjuntar esta información junto con la imagen de tu diagrama en el archivo `SOLUTION.md`

### Tips

* Toma en cuenta que el API de GitHub solamente permite **60** peticiones sin autenticación por día

## Deadline

* `Martes 21 de Diciembre a las 12pm`
