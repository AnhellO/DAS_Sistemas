////////////////////////////////////////////////////Requerimientos/////////////////////////////////////////////////////////////////
Es necesario instalar
Python 3, pip, BeautifulSoup 4, lxml, requests, sqlite3

////////////////////////////////////////////////////Descripcion////////////////////////////////////////////////////////////////////
En este proyecto cree una APP que simula los servicios que da una taqueria desde un sitio web, utilice la informacion proporcionada por un link, en el cual tuve la necesidad de Scrappear la inforamcion con ayuda de BeautifulSoup para cada una de las recetas que proporcionaba esta pagina, tambien diseñe una bases de datos con el nombre Data Base Gran Taco (DBGT) el cual se mostrara al correr el programa, en esta base de datos almacene la informacion necesaria para hacer que funcione esta app.
diviertete un poco utilizando esta app.
por ultimo jugue un poco con las API por que atraves de ella pude sacar clientes de manera random que son los que simulan la compra.

////////////////////////////////////////////////////Funcionamiento/////////////////////////////////////////////////////////////////
Hice un file llamado MetodosDB.py en la cual fabrique todos los metodos de la base de datos los cuales se pueden utilizar para la clase main.

en el file BDall.py meti los metodos abstractos para evitar que se creen los objetos desde la clase main.

BDprincipal.py este sirve para crear las tablas necesarias para mi base de datos.

Main.py se explica solo XD.

setup.py sirve basicamente para llenar la base de datos.

TacoScrapi.py es el codigo con el que Scrappie toda la informacion.

MenApi.py aqui es donde saque la informacion de la api.

///////////////////////////////////////////////////////Diagramas///////////////////////////////////////////////////////////////////

Diagrama Entidad Relación
[Entidad-Relacion](/EntidadRel.png)

Diagrama de Clases
[Diagrama_de_Clases](/Clases.png)

/////////////////////////////////////////Herramientas utilizadas y Referencias/////////////////////////////////////////////////////
http://taco-randomizer.herokuapp.com/.
https://randomuser.me/
https://markdown.es/sintaxis-markdown/?fbclid=IwAR2F0uVvbghVXlYdtzPdNSFwJoUoWFoTh6T3iQXA96YV7bVNBiqN-I-ALHM#imagenes 
https://docs.google.com/presentation/d/1Zx81UxMtDwOXr35cwMMZQ_6uQkALDfzSgbxxLwBtl40/edit#slide=id.g25eb4e6dae_0_12
algunos de los links que proporciono en los recursos
https://github.com/AnhellO/DAS_Sistemas/blob/development/Ago-Dic-2018/Pr%C3%A1cticas/Ordinario/SPECS.md
