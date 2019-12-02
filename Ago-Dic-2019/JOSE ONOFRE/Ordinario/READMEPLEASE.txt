A continuación se muestra la información de las herramientas utilizadas para el proyecto:

API (Consumo de datos):
Se utilizo Request y la API RAMAPI referencia: https://pypi.org/project/ramapi/     pip3 install ramapi

Base de datos:

Se utilizo SQlite3 donde se almacenaron los datos obtenidos de la API

CRUD:

Se utilizaron los comandos de SQLite para hacer consulta en la base BDCharacter.db 
NOTA: BDCharacter contiene las tablas characters,locations y episodes

Se utilizo el ORM Peewee para la elaboracion de la base Base.db
NOTA: Base contiene las tablas characterp, locationp, episodep
ademas que se usaron los metodos de Peewee para la insercion y consulta de datos

HTML Estatico:
Se crearon htmls por cada uno de los personajes, locaciones o episodios.

APP HTML Dinámico:
Se cro un html base
Se utilizo el framework Flask como Backend para el CRUD utilizando el metodo POST y GET para
mostrar los datos en el HTML
referencia:  Se instalo por medio de pip3 install flask


------------BUSQUEDA DE DATOS EN LOS HTML------------------

Las busquedas se ejecutan sobre LOCALHOST, se deben de abrir los html
-busqueda.html = Para buscar Characters
-busquedaEpisodio.html = Para buscar Episodios
-busquedaLocacion.html = Para buscar Locaciones