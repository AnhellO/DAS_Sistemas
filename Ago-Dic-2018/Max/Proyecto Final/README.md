# Diseño y Aquitectura de Software.

## Proyecto Final Taquitos!!!

Autor y programador - "Maximiliano García De Santiago"

## Descripción:

Este programa llevara a cabo la simulación de un puesto de taquitos.

Se encargará de extraer las recetas y sub recetas de cada taquito de una web
proporcionada por nuestro maestro. Link(http://taco-randomizer.herokuapp.com/)

También extraerá información especifica de usuarios participes en la web para su
uso practico. Link(https://randomuser.me/)

## Funcionamiento

Las funciones y clases principales a usar en este programa, fueron separadas
en distintos archivos para poder tener un mejor orden y control sobre estas.
Poder tener un control ordenado siempre es mejor para no perderse en las
diferentes clases o funciones.
La diferente forma de separamiento de trabajo son :
- Builders o constructores, clases abstractas.
- Método de extracción de los datos por request de una API.
- Método de extracción de los datos navegando por una estructura HTML.
- Creación de tablas almacenadas en la DB.
- Guardado de los datos extraídos en sus respectivas tablas.
- Extracción de datos de las tablas para creaciones de Pedidos.
- Main principal, que nos permite el uso de un Menú, donde conforme
  todas las funciones anteriores para un fácil manejo de estos.



## Acciones que permite realizar

Guardara la información extraída de las diferentes web en una DB creada
por el alumno, cada dato en su respectiva tabla de la DB.
Posteriormente, permitirá el acceso a información guardada en las distintas
tablas de la DB para poder crear el Pedido de un Cliente y el Taco que desea.

Otras de las distintas funciones que le permitira en el Menu principal sera la posibilidad
de poder llegar a hacer consultas de Pedidos realizados anteriormente, las distintas
Recetas guardadas y los distintos Clientes que se encuentren en la DB
(Todo esto proporcionando una Id de acceso).

Permitirá la posibilidad de Borrar datos de sus respectivas tablas:
- Recetas
- Clientes
- Pedidos

Consultar una lista completa de los Clientes en la DB también será algo posible.
Así, esta misma acción se podrá para los Pedidos o las Recetas .

## Referencias

https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://docs.python-guide.org/scenarios/scrape/
https://www.sqlite.org/docs.html
https://guides.github.com/features/mastering-markdown/
https://www.youtube.com/watch?v=XQgXKtPSzUI&t=950s
