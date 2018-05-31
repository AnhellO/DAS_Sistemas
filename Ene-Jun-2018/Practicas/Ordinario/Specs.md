# Proyecto Ordinario

## Especificaciones y Requerimientos

### Objetivo

- Crear un pequeña aplicación que corra en servidor local (si se monta y funciona en un servidor remoto, que mejor). La aplicación se comunicará a una base de datos (DBMS a elección del equipo) por medio de un ORM. Los datos que se utilicen para la DB son de libre elección (datos generados, datos parseados de algún sitio, etc). Al final, crear una página web que funcione desde el servidor, la cual despliegue los datos de las tablas de la DB en tabla(s) HTML (no es obligatorio el uso de CSS ni JS). No es obligatorio implementar múltiples páginas (una es suficiente), pero la aplicación deberá de soportar el uso de parámetros en las urls (`www.ejemplo.de?parametro&otroparametro=convalor`) de tal manera que estos parámetros filtren datos en la(s) tabla(s). Ejemplo:

`url-aplicacion?id=6` responde con una tabla como la siguiente (datos de mero ejemplo):

<table>
	<thead>
		<tr>
			<th>Id</th>
			<th>Nombre</th>
			<th>Edad</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>6</td>
			<td>Nepomuseno Casimiro de la Buenavista</td>
			<td>66</td>
		</tr>
	</tbody>
</table>


### Requerimientos

- Base de Datos
  - Uso de algún DBMS (recomendado SQLite)
  - Mínimo 3 tablas en la DB
  - Mínimo 100 registros en cada tabla
- ORM
  - Uso o implementación propia de un ORM (recomendados Peewee o SQLAlchemy)
  - Mapear cada tabla de la DB a un modelo propio
  - Uso de todas las operaciones CRUD via los Modelos (no importa en que parte de la app se usen)
- Página(s) Web
  - Uso de HTML para el rendereo de los datos en la(s) página(s) web (recomendado Jinja)
  - Mínimo una página que despliegue la(s) tabla(s) HTML
- Documentación
  - Agregar diagramas para:
    - Modelos (diagramas de clase)
    - Aplicación (diagrama de componentes)
    - DB (diagrama entidad-relación)
  - Descripción y especificaciones del funcionamiento de la app en un `README.md` (todo en formato MarkDown), así como las herramientas utilizadas y las referencias que hayan consultado durante el desarrollo del proyecto. Pueden incluir los diagramas aquí.

## Puntos Extra (Calificación Final)

* Menos W.E.T. y más D.R.Y.
* Un solid principle implementado
* Un patrón de diseño implementado
* Uso de un servidor remoto, CSS y/o JSS

## Referencias

### Pip
* https://pypi.org/project/pip/#description
* https://www.makeuseof.com/tag/install-pip-for-python/
* http://www.pythonforbeginners.com/pip/

### Virtualenv
* http://docs.python-guide.org/en/latest/dev/virtualenvs/
* https://realpython.com/python-virtual-environments-a-primer/

### SQLite
* https://www.tutorialspoint.com/sqlite/index.htm
* http://www.sqlitetutorial.net/sqlite-create-table/

### ORMs
* https://www.fullstackpython.com/object-relational-mappers-orms.html

### Template Engines
* https://www.fullstackpython.com/template-engines.html

### Python Local Server
* https://docs.python.org/2/library/simplehttpserver.html
* https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server
* http://www.pythonforbeginners.com/modules-in-python/how-to-use-simplehttpserver/

### Routing
* https://wiki.python.org/moin/Routing
* https://pypi.org/project/Routes/
* https://pythonspot.com/tag/full-stack-python/
