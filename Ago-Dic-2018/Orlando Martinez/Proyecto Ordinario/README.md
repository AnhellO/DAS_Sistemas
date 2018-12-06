#Proyecto final#
###class Tacos####
Se encuentra en el archivo tacos.py. Lo que hace esta clase es obtener la informacion de los tacos a traves de la api de la pagina [http://taco-randomizer.herokuapp.com/](http://taco-randomizer.herokuapp.com/). Esta informacion se tuvo que scrappear mediante la ayuda de BeautifulSoup. En esta clase se implemento un ciclo for para que obtuviera la informacion de 50 tacos y esta informacion es:
- Nombre taco
- Subrecetas
- Contribuidores

Despues de que se obtiene esta informacion se almacenaba en una base de datos.

###Class Cliente
Se encuentra en el archivo clientes.py. Esta clase obtiene la informacion de los clientes a traves de la api [https://randomuser.me/](https://randomuser.me/). Se utilizo un ciclo for para obtener la informacion de 50 clientes usando requests. La informacion que se obtuvo de los clientes es:
- Nombre
- genero
- direccion
- celular

Despues de obtener la informacion se guarda en una base de datos.

###Class SQlite
Se encuentra en el archivo base_de_datos.py. En esta clase se crean las funciones necesarias para manejar la informacion de la base de datos por ejemplo: ver el menu, ver los pedidos realizados, ver los clientes que han realizado un pedido.

###class main
En esta clase se simula la app de la taqueria. En esta clase se muestra un menú de opciones donde el usuario podra seleccionar la de su interes, estas opciones son:
- Ver menú (muestra todos los tacos disponibles)
- Ordenar (El cliente podra ordenar un taco insertando el id del taco y su id de cliente)
- Ver ordenes (Se mostraran todas las ordenes recibidas)
- Ver clientes (se mostrara la informacion de un cliente y el id de su pedido)
- Ver subrecetas (Se mostraran las subrecetas del taco elegido mediante su id)

###class db_init
En esta clase solo se crea la base de datos con sus respectivas tablas.

![Diagrama de clases](file:///C:/Users/Orlando/Pictures/Diagrama%20de%20clases.jpg)
![Diagrama entidad-relacion](file:///C:/Users/Orlando/Pictures/entidad-relacion.jpg)

##Herramientas utilizadas
- BeautifulSoup
- request
- SQlite
- Atom

##Referencias
- [https://jarroba.com/scraping-python-beautifulsoup-ejemplos/](https://jarroba.com/scraping-python-beautifulsoup-ejemplos/)

