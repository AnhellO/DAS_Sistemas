# Práctica 1

## Objetivo

Aprender y mejorar en el manejo de bases de datos en `SQLite` y en el consumo de APIs

## Especificaciones

La práctica deberá de enviarse a través de un pull request con su carpeta de alumno creada por ustedes. Anexar la base de datos que generen con `SQLite`

## Requerimientos

* Consumir la siguiente API [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/) de tal manera que obtengamos múltiples usuarios de el endpoint de `users`
* Crear una base de datos en `SQLite` a través de Python, y guardar los usuarios obtenidos en el punto anterior en una nueva tabla dentro de la base de datos creada
* Agregar rutinas de `SQL` por medio de `Python` para poder llevar a cabo las operaciones CRUD a los usuarios insertados en la base de datos, es decir:
  * Consultar uno o más usuarios
  * Insertar un nuevo usuario
  * Eliminar un usuario existente
  * Etcétera...

### Referencias

[https://stackabuse.com/a-sqlite-tutorial-with-python/](https://stackabuse.com/a-sqlite-tutorial-with-python/)
[https://realpython.com/python-requests/](https://realpython.com/python-requests/)
[https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/)