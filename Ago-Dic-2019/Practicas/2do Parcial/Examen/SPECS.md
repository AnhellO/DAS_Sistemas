# 2do. Examen Parcial

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Segundo Parcial/..`
* Cada ejercicio deberá estar en una carpeta por separado, es decir `../Segundo Parcial/Ejercicio 1/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request ni hagas commit de tu código hasta la hora límite (`03:00am` de mañana `Noviembre 22, 2019`) para evitar que este sea copiado :wink:

## Ejercicios

#### Ejercicio 1 - Guardando los datos

* Crea un script en `Python` que consuma datos de la siguiente API [`https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2`](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2)
  * Deberás de leer la documentación de la API para saber como funciona y como utilizarla
  * Ejemplo de endpoint de la API -> [`http://musicbrainz.org/ws/2/artist/020bfbb4-05c3-4c86-b372-17825c262094?fmt=json`](http://musicbrainz.org/ws/2/artist/020bfbb4-05c3-4c86-b372-17825c262094?fmt=json)
* Los datos consumidos deberán de ser guardados en una base de datos de `SQLite`. Los datos que deberás de obtener son los siguientes:
  * Todas las bandas cuyo `area.name = "Los Angeles"`
  * Las bandas deben de tener `tags` con la palabra `rock` y/o `metal` incluído en el `name` del tag
  * Debes de almacenar al menos 5 campos extras aparte del nombre de la banda en una tabla llamada `artistas` o similar
  * Guarda al menos `100` artistas diferentes en la base de datos
  * Para cada una de las bandas deberás de almacenar los discos que lanzaron exclusivamente en los `US` (`country = "US"`), en otra tabla por separado a la de `artistas`

#### Ejercicio 2 - Jugando con los datos



#### Ejercicio 3 - Mostrando los datos




## Puntos extra sobre el parcial (1 por ejercicio extra :wink:)