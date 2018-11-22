# 2do. Examen Parcial

## Especificaciones y Requerimientos

#### Mi API

* **Campos Gonzalez Ruben:** [https://jikan.moe/](https://jikan.moe/)
* **Enriquez Carrizales Daniel De Jesus:** [https://openlibrary.org/developers/api](https://openlibrary.org/developers/api)
* **Garcia De Santiago Maximiliano:** [https://anapioficeandfire.com/](https://anapioficeandfire.com/)
* **Garcia Muñoz Jesus Armando:** [http://opendata.emtmadrid.es/Servicios-web/BUS](http://opendata.emtmadrid.es/Servicios-web/BUS)
* **Gutierrez Garcia Cynthia Neftali:** [https://github.com/15Dkatz/official_joke_api](https://github.com/15Dkatz/official_joke_api)
* **Lopez Meza Andres:** [https://api.chucknorris.io/](https://api.chucknorris.io/)
* **Martinez Medina Orlando Miguel:** [https://launchlibrary.net/docs/1.3/api.html](https://launchlibrary.net/docs/1.3/api.html)
* **Ontiveros Perales Alma Daniela:** [https://reisapi.ruter.no/help](https://reisapi.ruter.no/help)
* **Perez Montes David Israel:** [https://swapi.co/](https://swapi.co/)
* **Perez Morin Genesis D.:** [http://jsonplaceholder.typicode.com/](http://jsonplaceholder.typicode.com/)
* **Rodriguez Garcia Angela Aracely:** [https://any-api.com/nba_com/nba_com/docs/API_Description](https://any-api.com/nba_com/nba_com/docs/API_Description)
* **Vázquez Seca Claudia Abelina:** [https://randomuser.me/](https://randomuser.me/)
* **Vela Torralba Ernesto:** [https://www.metaweather.com/api/](https://www.metaweather.com/api/)

#### Ejercicio 1

* De alguno de todos los endpoints disponibles en la API que te fue asignada, obtén al menos 100 elementos (o todos los que estén disponibles para ese endpoint, si es que hay menos), y genera un archivo para cada uno de esos elementos, los cuales deberás guardar en una nueva carpeta dentro de la carpeta principal del examen del 2do parcial (ejemplo `/2do-parcial/html/`), llamada `/html/`.

#### Ejercicio 2

* Crea una base de datos en `SQLite`, con al menos 5 columnas que representen a cada uno de los datos obtenidos de la API (o todas las columnas que haya disponibles, si es que son menos de 5). Guarda todos esos elementos junto con una columna extra que sea la ruta al archivo `JSON` generado en el ejercicio 1, ejemplo `/mi/carpeta/del/repo/2do-parcial/`.

#### Ejercicio 3

* Genera una tabla `HTML`, en la cual enlistes todas las columnas de los elementos ya guardados en la base de datos en el ejercicio 2. La tabla deberá de verse similar a la siguiente tabla:

``` html
<!DOCTYPE html>

<html>
	<head>
		<style>
			table {
			    font-family: arial, sans-serif;
			    border-collapse: collapse;
			    width: 100%;
			}

			td, th {
			    border: 1px solid #dddddd;
			    text-align: left;
			    padding: 8px;
			}

			tr:nth-child(even) {
			    background-color: #dddddd;
			}
		</style>
	</head>
	<body>
		<h2>Items de la Base de Datos</h2>
		<table>
		  	<tr>
			    <th>Encabezado de la Columna 1</th>
			    <th>Encabezado de la Columna 2</th>
			    <th>Encabezado de la Columna 3</th>
			    <th>Encabezado de la Columna 4</th>
			    <th>Encabezado de la Columna 5</th>
			    <th>Encabezado de la Columna 6</th>
			</tr>
			<tr> ... </tr> <!-- Y deberán ser 100 rows o más en total aquí ;) -->
		</table>
	</body>
</html>
```

## Hints

* Puedes crear un archivo `.py` por separado para cada ejercicio, o hacerlos todos en un solo archivo, como más se te facilite
* Puedes probar tu `HTML` del ejercicio 3 en tu navegador web directamente

## Referencias

* [https://searchmicroservices.techtarget.com/definition/RESTful-API](https://searchmicroservices.techtarget.com/definition/RESTful-API)
* [https://tecnorush.com/que-es-una-api-y-para-que-sirve-bien-explicado/](https://tecnorush.com/que-es-una-api-y-para-que-sirve-bien-explicado/)
* [https://github.com/interagent/http-api-design](https://github.com/interagent/http-api-design)
* [https://github.com/toddmotto/public-apis](https://github.com/toddmotto/public-apis)