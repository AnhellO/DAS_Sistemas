# Práctica 1

## Objetivo

- Aprender sobre los diferentes formatos de serialización y deserialización de archivos
- Uso del manejador de paquetes de `Python`: `pip`
- Uso de nuevos paquetes externos

## Especificaciones

### Ejercicio 1

Lee, investiga y aprende sobre el formato `XML`:

- <https://developer.mozilla.org/es/docs/Web/XML/XML_introduction>
- <https://support.microsoft.com/es-es/office/xml-para-no-iniciados-a87d234d-4c2e-4409-9cbc-45e4eb857d44>
- <https://openwebinars.net/blog/que-es-xml-y-para-que-se-usa/>

Analiza la librería de XML nativa de Python: <https://docs.python.org/3/library/xml.etree.elementtree.html> y a través de un script que se llame `my_xml.py` lleva a cabo las siguientes tareas:

- Leer el archivo [`sample.xml`](sample.xml)
- Imprimir una lista de todas las personas cuyo nodo de id sea un número par
- Imprimir una lista de todas las personas cuyo correo electrónico tenga el dominio `.edu` o `.gov`
- Manipular el contenido del archivo original de tal manera que todos los nodos de `ip_address` ahora sean iguales a la IP `127.0.0.1` y guardar el resultado en un nuevo archivo llamado `updated.xml`

### Ejercicio 2

Lee, investiga y aprende sobre el formato `JSON`:

- <https://www.oracle.com/mx/database/what-is-json/>
- <https://www.json.org/json-es.html>
- <https://developer.mozilla.org/es/docs/Learn/JavaScript/Objects/JSON>

Analiza la librería de JSON nativa de Python: <https://docs.python.org/3/library/json.html> y a través de un script que se llame `my_json.py` lleva a cabo las siguientes tareas:

- Leer el archivo [`sample.json`](sample.json)
- Imprimir una lista de todas las personas cuyo nodo de id sea un número impar
- Imprimir una lista de todas las personas cuyo nombre de la compañía tenga una longitud de entre `4` y `6` letras
- Manipular el contenido del archivo original de tal manera que todos los nodos de `phone_number` ahora sean iguales al string `XX-XX-XXX` y guardar el resultado en un nuevo archivo llamado `updated.json`

### Ejercicio 3

Lee, investiga y aprende sobre el formato `YAML`:

- <https://geekflare.com/es/yaml-introduction/>
- <https://yaml.org/>
- <https://learnxinyminutes.com/docs/es-es/yaml-es/>

Analiza la librería de YAML externa de Python: <https://pyyaml.org/wiki/PyYAMLDocumentation> y a través de un script que se llame `my_yaml.py` lleva a cabo las siguientes tareas:

- Leer el archivo [`sample.yml`](sample.yml)
- Imprimir una lista de todas las personas cuyo nodo de id sea un número múltiplo de 3
- Imprimir una lista de todas las personas cuyo nombre o apellido tenga una longitud exacta de `5` letras
- Manipular el contenido del archivo original de tal manera que todos los nodos de `email` ahora sean iguales al string `---` y guardar el resultado en un nuevo archivo llamado `updated.yml`

## Deadline

- `Viernes 3 de Junio a las 11:59pm`
