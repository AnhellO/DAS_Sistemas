# Proyecto Ordinario

## Especificaciones

* Crear un pequeña aplicación que simule el servicio de un puestito de tacos que puso su página web online :taco:. La información para llenar la base de datos de tacos se obtendrá desde [http://taco-randomizer.herokuapp.com/](http://taco-randomizer.herokuapp.com/). Dado que esta es una API tipo HTML, los datos deberás de "_scrappearlos_" con la ayuda de [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/). Para cada receta de tacos, deberás obtener toda la información posible y disponible en su página: sub-recetas (que también son recetas :wink:), contribuidores, tags, links, etcétera. Queda a tu criterio el como diseñes la base de datos y sus relaciones, pero mientras _más mejor_ lo hagas, más se te facilitará el proyecto :wink:. Al final, se deberá de crear una clase principal que juegue con los datos guardados en la DB. Para ello, deberás de crear objetos `Client` que consuman sus órdenes de taquitos :yum:. Los datos que se utilicen para crear este tipo de objetos deberán de ser obtenidos a través de la API [randomuser.me](https://randomuser.me/) (es opcional guardar los usuarios en la base de datos también, pero, puede ayudar :wink:)

## Requerimientos

* Clases
  * Mínimo 3 clases + la clase `main` en dónde se simulará la app de taquitos. Queda a libertad tuya decidir cuales clases implementar, ya sea porque son necesarias, o nada más por amor al arte :stuck_out_tongue:. Échale coco e imaginación :wink:.
* Base de Datos
  * Uso de SQLite
  * Mínimo 3 tablas en la DB
  * Mínimo 50 recetas de tacos scrappeadas y guardadas en la DB :stuck_out_tongue:
* Documentación
  * Agregar diagramas para:
    * Clases (diagramas de clase)
    * DB (diagrama entidad-relación)
  * Descripción y especificaciones del funcionamiento de la app en un `README.md` (todo en formato `MarkDown`), así como las herramientas utilizadas y las referencias que hayan consultado durante el desarrollo del proyecto. Pueden incluir los diagramas aquí en el archivo `.md`.

## Puntos Extra (Calificación Final)

* Menos W.E.T. y más D.R.Y.
* Un solid principle implementado
* Un patrón de diseño implementado
* Uso de algún ORM listado en los recursos de abajo :wink:

## Recursos

### Pip
* [https://pypi.org/project/pip/#description](https://pypi.org/project/pip/#description)
* [https://www.makeuseof.com/tag/install-pip-for-python/](https://www.makeuseof.com/tag/install-pip-for-python/)
* [http://www.pythonforbeginners.com/pip/](http://www.pythonforbeginners.com/pip/)

### Virtualenv
* [http://docs.python-guide.org/en/latest/dev/virtualenvs/](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [https://realpython.com/python-virtual-environments-a-primer/](https://realpython.com/python-virtual-environments-a-primer/)

### BeautifulSoup
* [https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe](https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe)
* [https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python](https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python)

### SQLite
* [https://www.tutorialspoint.com/sqlite/index.htm](https://www.tutorialspoint.com/sqlite/index.htm)
* [http://www.sqlitetutorial.net/sqlite-create-table/](http://www.sqlitetutorial.net/sqlite-create-table/)

### ORMs
* [https://www.fullstackpython.com/object-relational-mappers-orms.html](https://www.fullstackpython.com/object-relational-mappers-orms.html)
