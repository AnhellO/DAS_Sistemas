# Examen Especial

## Información

- Fecha de aplicación: `Martes 30 de Agosto del 2021`
- Maestro: `Angel Santiago Jaime Zavala`

## Previo

- Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing)
- La carpeta del examen tendrá que llamarse `../Examen Especial/..`
- Si el ejemplo solamente necesita comandos escritos entonces agregalos en un archivo `.md` (Markdown) que anexes por separado dentro de tu carpeta con las soluciones al examen. También es importante adjuntar las demás evidencias que se piden por cada ejercicio, como screenshots por ejemplo

## Especificaciones

Este ejercicio va a consistir en desarrollar una pequeña API con datos parseados y mapeados desde un archivo `XML` en crudo.

Crea un archivo `docker-compose.yml` que ejecute **4** contenedores:

- El **1er contenedor** ejecutará un servidor de base de datos y su nombre deberá de ser `db`
  - Para almacenar los datos puedes utilizar cualquier motor de base de datos que gustes, desde `SQLite` hasta `MySQL` o `MongoDB`
- El **2do contenedor** ejecutará un DBMS el cual se llame `dbms` y que se conectará al contenedor de `db` creado en el punto anterior. Este contenedor fungirá como el DBMS de la aplicación. Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:
  - Usuario: `das-sistemas`
  - Password: `practica-4-2021!`
- El **3er contenedor** ejecutará un programa que lleve a cabo lo siguiente:
  - Que lea el archivo XML [`people.xml`](people.xml) adjunto
  - Que guarde cada nodo de `<person>` en la base de datos del **1er contenedor**. Cada nodo tendrá que ser un registro por separado, pero todos estos registros pueden vivir en una sola colección/tabla
  - Asegúrate de construir el respectivo `Dockerfile` para esta imagen y de instalar todas las dependencias necesarias en el mismo
- El **4to contenedor** ejecutará otro programa que lleve a cabo lo siguiente:
  - Levantará una pequeña "`API`" que mostrará todos los registros guardados desde el `XML` a través del endpoint/recurso de `/people`, por lo tanto tendrá que conectarse al **1er contenedor** de la base de datos de tal manera que pueda acceder a los registros de la misma. Estos registros tendrán que ser servidos en formato `JSON` y la API tendrá que funcionar por medio de algún router
  - Aparte del endpoint/recurso de `/people`, tendremos que agregar otro endpoint/recurso que nos muestre un JSON con la información en particular para cada persona y que sea accesible por medio de un nuevo endpoint/recurso con la forma `/people/{id}`, en donde `{id}` es igual al `ID` del registro en la `BD`
  - Asegúrate de construir el respectivo `Dockerfile` para esta imagen y de instalar todas las dependencias necesarias en el mismo
  - Finalmente, este contenedor en particular tendrá que ser ejecutado en modo "_daemonizado_" y deberá de estar accesible a través del puerto `7777`

## Requerimientos

- Puedes utilizar cualquier lenguaje de programación para desarrollar tu solución
- Puedes utilizar dependencias y/o librerías externas, solamente asegúrate de utilizar el correcto manejador de dependencias para el lenguaje que uses
- Adjuntar un archivo `README.md` que contenga una descripción de tu solución junto con las instrucciones para poder probarlo

## Bonus

Cada ítem que implementes de la siguiente lista te dará **1** punto adicional sobre la cantidad de puntos extra que ya te da el completar la práctica con su correcto funcionamiento.

- Utilizar `Python` o `GO` como lenguaje principal
- Utilizar `MongoDB` como base de datos
- Implementar el [`CRUD`](https://developer.mozilla.org/es/docs/Glossary/CRUD) completo para la aplicación
- Si implementaste el CRUD, utilizar `RabbitMQ` para enrobustecer esta parte de la aplicación
- Si implementaste el CRUD, llevar a cabo pruebas de cada una de las operaciones con `Postman` o `Insomnia` y adjuntar un _export_ con todas las peticiones que hiciste de prueba
- Implementar la solución utilizando `Domain Driven Design`
- Agregar una suite robusta de tests unitarios y/o funcionales
- Agregar documentación y comentarios en el código (diagramas de la arquitectura de la aplicación, UMLs, docblocks, etcétera)
- Utilizar [Swagger](https://swagger.io/) en tu proyecto y agregar un contenedor nuevo con el [`Swagger UI`]((https://hub.docker.com/r/swaggerapi/swagger-ui)) de la aplicación
- Agregar un frontend para la aplicación a través de un nuevo contenedor de `Docker`
- Si agregaste un frontend y agregaste el CRUD, que este provea la funcionalidad completa de `CRUD`  desde la misma `GUI`

## Deadline

- `Jueves 2 de Septiembre del 2021 a las 11:00 PM`
