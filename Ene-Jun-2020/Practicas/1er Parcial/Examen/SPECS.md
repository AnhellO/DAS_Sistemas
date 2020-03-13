# 1er. Examen Parcial

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Primer Parcial/..`
* Cada ejercicio deberá estar en una carpeta por separado, es decir `../Primer Parcial/Ejercicio 1/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request ni hagas commit de tu código hasta la hora límite (`Viernes 13 de Marzo, 2020 a las 12:00pm`) para evitar que este sea copiado :wink:

## Ejercicios

#### Ejercicio 1

* Crea una clase `Page` que represente a una página dentro de un sitio web. La clase deberá de contener múltiples atributos que pertenezcan a una página web, por ejemplo url, folder o path, links o hipervínculos, contenido de texto, título (`<h1>`), etiqueta de título (`<title>`), meta-descripción, formato (`HTML`, `XML`, `JSON`, etc), etcétera (Recurso: https://es.wikipedia.org/wiki/P%C3%A1gina_web)
* Crea una 2da clase `Website` que represente a un sitio web como un todo/conjunto. La clase deberá de contener múltiples atributos que describan a un sitio web, por ejemplo dominio, subdominio, páginas que forman parte del sitio, entre otros (Recurso: https://mx.godaddy.com/blog/que-es-un-sitio-web/)
  * La clase `Website` deberá tener un atributo que contenga a la colección de páginas de forman parte del sitio. Los objetos de esta colección deberán de ser de tipo `Page`
  * Implementa una función `buscador`, que reciba dos parámetros, uno de tipo `Website`, y el otro de tipo `Page`. La función deberá de llevar a cabo una búsqueda dentro del conjunto de páginas del sitio para determinar si es que la página existe

#### Ejercicio 2

* Implementa el patrón de diseño decorador sobre las clases y objetos del `Ejercicio 1` para que:
  * Decores objetos del tipo `Page`, de tal manera que si su formato es `HTML`, agregues `CSS` sobre las etiquetas de `HTML` que forman parte del contenido de la página (Recurso: https://www.w3.org/Style/Examples/011/firstcss.en.html)
  * Ejemplo:
    * Contenido no decorado: `<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p>`
    * Contenido decorado: `<p style="color:blue;text-align:center;">Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p>`
* Puedes implementar el patrón de diseño desde 0 con sus actores/clases propias, o bien, utilizar los decoradores nativos de Python

#### Ejercicio 3

* Crea un clase `Response`, que se encargué de servir objetos tipo `Page` creados en el `Ejercicio 1`
  * Implementa el patrón de diseño strategy junto a la clase `Response` para que esta pueda servir diferentes objetos `Page` en base a su tipo/formato (`HTML`, `XML`, `JSON`, etc.) (Recurso: https://en.wikipedia.org/wiki/Request%E2%80%93response)
  * Ejemplo, evaluando `page.getTipo() == 'html'`:
    ```
    Response:
    - Page: <url>
    - Type: HTML
    - Content: <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p>
    ```

#### Ejercicio 4

_Coming soon..._

#### Ejercicio 5

_Coming soon..._

