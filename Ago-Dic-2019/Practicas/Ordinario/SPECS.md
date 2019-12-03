# Examen Ordinario

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Ordinario/..`
* Incluye los archivos de tus bases de datos `.db` y los archivos `.html` generados dentro del pull request final
* **NO** envíes tu pull request ni hagas commit de tu proyecto hasta la hora límite (`20:00` del Domingo `1º de Diciembre, 2019`) para evitar que este sea copiado :wink:

## Ejercicios

#### Parte 1

* Crea un script en `Python` que consuma datos de la siguiente API: [`https://rickandmortyapi.com/`](https://rickandmortyapi.com/)
* Los datos consumidos deberán de ser guardados en una base de datos de `SQLite` de la siguiente manera
  * Guardar cada uno de los `characters` en una tabla de `personajes` o `characters`, con todos los campos posibles
  * Guardar cada una de los `locations` en una tabla de `locaciones` o `locations`, con todos los campos posibles
  * Guardar cada uno de los `episodes` en una tabla de `episodios` o `episodes`, con todos los campos posibles
  * **OJO:** Deberás de establecer las relaciones `uno a muchos` o `muchos a muchos` entre aquellas tablas en las que sea posible hacerlo. Por ejemplo, un episodio puede tener múltiples personajes, pero un personaje también puede aparecer en múltiple episodios :wink:
  * Anexa un diagrama entidad-relación de la base de datos resultante

#### Parte 2

* Con otro script nuevo en `Python`, y utilizando [`SQLAlchemy`](https://github.com/sqlalchemy/sqlalchemy) o [`Peewee`](https://github.com/coleifer/peewee) como `ORM`:
  * Genera un archivo estático `index.html`, el cual contenga un enlace a cada una de las entidades/tablas en la base de datos
  * Para cada una de las entidades también deberás de generar un archivo de índice `.html`, el cual ahora liste cada una de las filas/registros existentes para esa entidad
  * Para finalizar, para cada registro existente ahora deberás de generar un archivo `.html` el cual contenga la información específica de ese registro
  * Puedes tomar el directorio de [`ejemplo`](ejemplo/) como base para llevar a cabo los puntos anteriores

#### Parte 3

* Crea una pequeña app/script en `Python`, el cual haga exactamente lo mismo que en la **Parte 2**, pero ahora generando las páginas dinámicamente, es decir, sin crear archivos `.html` -> ([estático vs dinámico](http://cefire.edu.gva.es/file.php/1/Comunicacion_y_apertura/B3_PaginaWeb/pgina_web_esttica_vs_dinmica.html))
  * Para este paso puedes utilizar cualquier herramienta o librería externa que te sea útil

## Recursos

* http://anh.cs.luc.edu/handsonPythonTutorial/ch4.html
* http://python.zirael.org/ch-dynamic_pages.html
* https://realpython.com/python-web-applications/
* https://code.tutsplus.com/articles/python-from-scratch-create-a-dynamic-website--net-22787
* https://wiki.python.org/moin/Routing
* https://www.tutorialspoint.com/python_network_programming/python_routing.htm
* https://pypi.org/project/Routes/
* https://hackersandslackers.com/the-art-of-building-flask-routes/