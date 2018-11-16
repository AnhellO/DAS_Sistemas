# Práctica 1

## Objetivos

* Manejo básico de librerias en python
* Peticiones HTTP y respuestas de un sitio
* SQLite con Python
* Manejo archivos normales y de tipo JSON

## Especificaciones

Complementar el script de [que-sera.py](que-sera.py) para que cumpla con los siguientes puntos:
* Obtener todas las cervezas existentes en la API de `https://punkapi.com/`
* Guardar todas las cervezas obtenidas de la API en una base de datos creada con SQLite
  * La tabla de cervezas requiere contar con las siguientes 5 columnas obligatorias: `name`, `description`, `image_url`, `abv` y `food_pairing`
  * Aparte de las columnas solicitadas en el punto anterior, la tabla requiere tener otros 5 campos más a tu elección :wink:
* Agregar un check y/o forma de comprobar que todas las cervezas de la API se guardaron correctamente en la base de datos. La forma de comprobar esto es a libre elección.

## Referencias

#### Requests

* [http://docs.python-requests.org/en/master/](http://docs.python-requests.org/en/master/)
* [https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html](https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html)

#### SQLite

* [https://www.pythoncentral.io/introduction-to-sqlite-in-python/](https://www.pythoncentral.io/introduction-to-sqlite-in-python/)
* [https://www.tutorialspoint.com/sqlite/sqlite_python.htm](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

#### Archivos

* [https://www.pythonforbeginners.com/cheatsheet/python-file-handling](https://www.pythonforbeginners.com/cheatsheet/python-file-handling)
* [https://www.w3schools.com/python/python_file_handling.asp](https://www.w3schools.com/python/python_file_handling.asp)

#### JSON

* [https://www.json.org/](https://www.json.org/)
* [https://www.w3schools.com/js/js_json_intro.asp](https://www.w3schools.com/js/js_json_intro.asp)
* [https://jsoneditoronline.org/](https://jsoneditoronline.org/)