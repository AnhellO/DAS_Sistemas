# Bienvenido a la App de Taquitos

"Aquí podrás ordenar tu taquito especial de entre la gran variedad de Taquitos"

## Descripción:

* Proyecto Final de la materia Diseño y Arquitectura de Software.
* La aplicación sirve como un sistema de órdenes, simulando ser un restaurant o
  local de tacos. En el que se puede ver el menú, realizar pedidos, ver el pedido
  y hasta eliminarlo.
* Es algo básico su funcionamiento, ya que sólo se puede pedir un taco por orden
  pero cumple con las especificaciones que debía tener el proyecto.
* La estructura de las clases fue diseñada a partir del patrón de Diseño Abstract Factory.

## Requerimientos:

* Es necesario tener instalados:
  - Python 3 (de la versión .6 en adelante)
  - pip (Para instalar las librerías que utilizarémos)
  - BeautifulSoup 4 (Para realizar el scrapping de la web generadora de taquitos)
  - lxml (para el parseo de los datos obtenidos)
  - requests (para realizar las peticiones)
  - sqlite3 (como librería manejadora de la base de datos)

## Funcionamiento:

* Primeramente es necesario correr la clase "db_tacos_init.py", la cual generará
  nuestra base de datos con sqlite3.

* Lo siguiente que hay que hacer, es correr la clase "setup.py".
  Esta es la encargada de correr los métodos get para la extracción de datos
  de la página "http://taco-randomizer.herokuapp.com/" que genera tacos con
  ingredientes escogidos al azar. Para luego insertarlos a la base de datos
  en la tabla "Tacos".
  Y a su vez, tambien se encarga de extraer los datos de la Api generadora de
  clientes "https://randomuser.me/" que nos genera un usuario al azar con
  sus respectivos datos. Y al igual que con los tacos, inserta los datos a
  la base de datos en la tabla "Users".
  (Los métodos de extracción se encuentran en las clases:
    - taco_scrapi.py
    - usuarios_api.py

* Una vez lista nuestra base de datos, podemos correr la clase "Main".
  Que se funciona como nuestro método principal, en el que podemos interactuar
  con la aplicación.
  Este depende de la base de datos, por lo cual ya no es necesario scrappear nada
  ni sacar datos de la Api.
  Aca las opciones para interactuar son las de Ver Menú, Realizar Pedido,
  Ver Pedido y Eliminar Pedido.

* Para la creación de los objetos se utilizó el Patrón de Diseño Abstract
  Factory, como se puede ver en la clase "bases", la cual desprende las abstractas
  que se utilizan.

## Diagramas:

* Diagrama Entidad Relación de la Base de Datos:
![Entidad-Relacion](/EntidadRel.png)

* Diagrama de Clases:
![Diagrama_de_Clases](/Clases.png)

## Herramientas utilizadas y Referencias:
* http://taco-randomizer.herokuapp.com/
* https://randomuser.me/
* https://markdown.es/sintaxis-markdown/?fbclid=IwAR2F0uVvbghVXlYdtzPdNSFwJoUoWFoTh6T3iQXA96YV7bVNBiqN-I-ALHM#imagenes
* https://pypi.org/project/pip/#description
* https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
* http://www.sqlitetutorial.net/sqlite-create-table/
* https://docs.google.com/presentation/d/1Zx81UxMtDwOXr35cwMMZQ_6uQkALDfzSgbxxLwBtl40/edit#slide=id.g25eb4e6dae_0_12
