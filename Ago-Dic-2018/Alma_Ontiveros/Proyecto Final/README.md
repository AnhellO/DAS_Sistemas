#**"Descripción y especificaciones del funcionamiento de la app"**

## Descripción y datos que se necesitarán:
* En si la app sirve como si fuera un sistema de órdenes de tacos y se pueden hacer los pedidos corriendo el MenuTacos.py pidiendo un taco a la vez y esta aplicacion te da las opciones Menu, Pedidos, Ver los Pedidos y Eliminar pedidos.
* La estructura fue diseñada como el patrón de Diseño Abstract Factory.
* En cada creación de tabla agregué diferentes propiedades como se pidió en el proyecto:
  - Taco: IDTACO como PK, name, ingprincipal, salsas, condimentos, sasonadores y cubierta
  - Cliente: IDCLIENTE como PK, name, email, location, phone y picture
  - Orden: IDORDEN como PK, IDTACO como fk, IDCLIENTE como fk, total y fecha
* Utilice GIT BASH en Windows y tuve que instalar varias cosas como:
  - Python 3 (en lo personal tengo Python 3.7.1)
  - pip
  - requests
  - sqlite3 (https://www.sqlite.org/download.html en esa página pude descargarlo en el SO que estoy manejando)
  - BeautifulSoup 4 (este no lo descargué, ya lo tenía junto con el Python que descargue en Windows)
  - lxml

## ¿Cómo funciona esto?:
* Para que funcione y ver que todos los programas están correctos, corrí la clase "BaseDatosTacos_init.py" y esta te crea una base de datos.

* Despues, correr la clase "Datos.py"
  Esta clase sirve o funciona para que traiga los datos desde la API Tacos "http://taco-randomizer.herokuapp.com" y tambien la API de clientes "https://randomuser.me/" y es quien corre todos los metodos get (las clases son AppCliente.py y AppTacos.py). La primera API te arroja todos los nombres de los tacos junto con sus ingredientes o requerimientos que solicitamos en la tabla Tacos y ahi mismo se van a ir guardando. En la segunda API la de clientes va a ir extrayendo clientes al azar junto con todos los datos que solicitamos en la tabla Cliente y tambien como con la tabla Tacos, los clientes junto con las referencias requeridas se iran guardando en la tabla mencionada.

* Luego de que corrimos Datos.py y no haya existido ningun problema, ya ahora si corremos la clase MenuTaco.py
Esto para ver si funciona el menu y si en cada opcion corren correctamente los datos que corresponden a cada una.
Es para que sea mas dinamica la clase con el cliente, o sea la aplicación.


## Referencias:
* http://taco-randomizer.herokuapp.com/
* https://randomuser.me/
* https://www.sqlite.org/download.html
* https://docs.google.com/presentation/d/1Zx81UxMtDwOXr35cwMMZQ_6uQkALDfzSgbxxLwBtl40/edit#slide=id.g25eb4e6dae_0_12
* https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python
* https://jarroba.com/scraping-python-beautifulsoup-ejemplos/
* https://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup
* https://platzi.com/blog/expresiones-regulares-python/