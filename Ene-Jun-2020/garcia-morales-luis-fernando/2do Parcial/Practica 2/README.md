AGE OF EMPIRES INFO
-----------------------------------------------------------------------------
Aplicacion que recolecta informacion desde la API https://age-of-empires-2-api.herokuapp.com
y la almacena en una base de datos local usado libreria sqlite3 para creacion de bases de datos 
y tablas.
Se utiliza tecnica ORM usuando la libreria peewee para insertar y mostrar los datos.
-----------------------------------------------------------------------------
INSTRUCCIONES:
Usar comando => docker run -it -p 5000:5000 fernandogm/age_of_empires_db:1.0 para inicializar contenedor remoto de dockerhub.
Usar comando => python3 app.py para correr el programa Local con python

La aplicacion genera informacion de CIVILIZACIONES, UNIDADES, ESTRUCTURAS y TECNOLOGIAS de manera
aleatoria al recargar la pagina deacuerdo al parametro dado en la url.
  Ejemplo:
  0.0.0.0:5000 => Muestra un pequeño menu que redirecciona a las paginas de informacion.
  0.0.0.0:5000/civiliations => Genera la informacion de una Civilizacion al azar. Al recargar Genera una civilizacion aleatoria y muestra su info.
  0.0.0.0:5000/units => Genera la informacion de una Unidad al azar. Al recargar Genera una Unidad aleatoria y muestra su info.
  0.0.0.0:5000/technologies => Genera la informacion de una Tecnologia al azar. Al recargar Genera una Tecnologia aleatoria y muestra su info.
  0.0.0.0:5000/structures => Genera la informacion de una Estructura al azar. Al recargar Genera una Estructura aleatoria y muestra su info.
