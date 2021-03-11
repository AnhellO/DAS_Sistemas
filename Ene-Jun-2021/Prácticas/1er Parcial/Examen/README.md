# 1er. Examen Parcial

## Previo

* Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen en este caso tendrá que llamarse `../Primer Parcial/..`
* Cada ejercicio deberá estar en una carpeta por separado, es decir `../Primer Parcial/Ejercicio 1/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request ni hagas commit de tu código hasta la hora límite (`Sábado 13 de Marzo del 2020 a las 11:59pm`) para evitar que este sea copiado :wink:
* Explica la lógica utilizada detrás de cada uno de los ejercicios. Pueden ser como un archivo de texto por separado, o bien, como comentarios dentro del mismo código

## Especificaciones y Requerimientos

### Ejercicios

#### Ejercicio 1

* Crea una clase `PaginaWeb` que represente a un [documento dentro de un sitio web](https://es.wikipedia.org/wiki/P%C3%A1gina_web). La clase deberá de contener los siguientes atributos:
  * `url`: URL final de la página
  * `ruta`: Ruta de archivos de la página
  * `formato`: Tipo de contenido de la página, puede ser `HTML`, `XML`, `JSON`, etcétera
  * `contenido`: String con el contenido de la página. Este tendrá que ser acorde al `formato` de la página, es decir, si nuestra página es de formato `XML`, entonces el contenido deberá de ser `XML`
  * `título`: Título de la página, equivalente a la etiqueta `<h1>`
  * `slug`: Versión "_slugificada_" del título, por ejemplo, para un "_Título Como Este_", tendríamos un "_titulo-como-este_" en versión slug
  * `meta-tags`: lista que contiene las diferentes [meta-etiquetas](https://es.ryte.com/wiki/Meta_Etiqueta) del sitio
* Crea una 2da clase llamada `SitioWeb` que represente a un [sitio web como un todo/conjunto](https://mx.godaddy.com/blog/que-es-un-sitio-web/). La clase deberá de contener los siguientes atributos, los cuales describan a un sitio web:
  * `dominio`: 
  * `categoría`: categoría del sitio
  * `paginas`: lista de páginas que forman parte del sitio. Los objetos de esta colección deberán de ser de tipo `PaginaWeb`
* Asegúrate de implementar la función `__str__` para ambas clases

#### Ejercicio 2

* Implementa el patrón de diseño [`Decorator`](https://refactoring.guru/design-patterns/decorator) de tal manera que agreguemos la funcionalidad de un `buscador` interno a instancias de la clase `SitioWeb`. El decorador tendrá que recibir como parámetro un objeto del tipo `PaginaWeb`, y la función decorada deberá de llevar a cabo una búsqueda dentro del conjunto de páginas del sitio para determinar si es que la página existe o no.
* Puedes codificar el patrón de diseño desde 0, o bien puedes utilizar los decoradores nativos de Python para llevar esto a cabo

#### Ejercicio 3

* Partiendo de la suite de tests unitarios en el archivo [`facade_test.py`](facade_test.py):
  * Imagina que tenemos una lavadora "_todo-en-uno_" que puede lavar ropa, enjuagarla y también centrifugarla, pero todas estas tareas se llevan a cabo por separado. Como todo el sistema es bastante complejo, necesitamos abstraer las complejidades de los subsistemas. Necesitamos un sistema que pueda automatizar toda la tarea sin nuestra perturbación o interferencia.
  * Crea un nuevo archivo/módulo `facade.py` e implementa el patrón de diseño [`Facade`](https://refactoring.guru/design-patterns/facade) de tal manera que podamos ocultar o abstraer las complejidades de los subsistemas de nuestra lavadora en una única interfaz
  * Asegúrate de que todos los tests del archivo de pruebas unitarias pasa sin problema alguno al probar tu solución

#### Ejercicio 4

* Partiendo del siguiente [diagrama UML](chain-of-reponsibility.jpg), y complementando con el caso de uso propuesto a continuación:
  * Tenemos de ejemplo un cajero automático, el cual debe de distribuir el dinero en billetes de $50 primero, luego en billetes de $20 y al final en billetes de a $10
  * Este orden predeterminado de la "_cadena_" ayuda a garantizar que se distribuya el número mínimo de billetes. De lo contrario, podría dispensar 5 x $10 cuando hubiera sido mejor dispensar 1 x $50
  * Codifica la solución utilizando el patrón de diseño [`Chain of Responsibility`](https://refactoring.guru/design-patterns/chain-of-responsibility)
  * Agrega la respectiva suite de tests unitarios para este ejercicio. Recuerda utilizar un enfoque `T.D.D.` :wink:

#### Ejercicio 5

* Para el ejemplo de código en el archivo [srp.py](srp.py):
  * Analiza y refactoriza el código de tal manera que se utilice el [`Single Responsibility Principle`](https://dev.to/annalara/solid-programming-part-1-single-responsibility-principle-1ki6) de la manera correcta
  * Utiliza un enfoque "_Red-Green Refactoring_" como el visto en clase, de tal manera que agregues la suite de tests unitarios necesaria a la par de que vas refactorizando el código propuesto :wink:
  * Explica la lógica implementada detrás de tu enfoque y contesta a las siguientes preguntas (todo esto como comentarios dentro de tu código):
    * ¿Qué sucedería si quiero agregar otro formato de serialización más complejo como `XML` o `Yaml`?
    * ¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase `Usuario`?

### Puntos Extra

* Implementa la suite de tests unitarios para el **Ejercicio 1**. En esta suite se deben de probar al menos 3 posibles casos de prueba para el comportamiento de una instancia de la clase `SitioWeb`
  * **(5 puntos sobre 100)**
* Implementa el patrón de diseño `Proxy` para agregar una capa de autenticación básica con `usuario` y `password` a objetos de la clase `SitioWeb` del ejercicio 1
  * **(5 puntos sobre 100)**
* Generar diagrama UML para el Ejercicio 1
  * **(2 puntos sobre 100)**
* Generar diagrama UML para el Ejercicio 2
  * **(2 puntos sobre 100)**
* Generar diagrama UML para el Ejercicio 3
  * **(2 puntos sobre 100)**
