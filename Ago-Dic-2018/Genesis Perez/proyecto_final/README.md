# Descripción y especificaciones

La app consta de 3 archivos:
1. crearTablas.py
2. webScrapping.py
3. mainProyectoFinal.py


En el archivo *crearTablas.py* hay una clase llamada **bd** con una función llamada **CrearTablas()** en donde se hace la conexión con la base de datos y despues se crean las 3 tablas: *tacos, clientes y ordenes*.
Al momento de crear la tabla imprime un mensaje en consola que expecifica si se creó con éxito o hubo un error.

En el archivo *webScrapping.py* primeramente se hace la conexión a la base de datos, después hay una clase llamada **scrappingTacos** que se encarga de extraer la información de la url que posteriormente se utiliza para obtener solo los datos que me interesan; jugué con la información cortandola para poder guardarla como quería en la tabla *tacos*.
Durante los ciclos for se va llenando la tabla.

Más adelante en el mismo archivo está la clase llamada **Clientes** con una funcion llamada **crearClientes()** que también extraer la información de la url, pero de forma distinta ya que se usa la api de la página de donde se crean los clientes.
Durante el ciclo se va llenando la tabla *clientes*.

Por último en el archivo *mainProyectoFinal.py* se juega con los clientes y los tacos para que simule que están consumiendolos.
Primero se hace la conexion a la base de datos, después hay diferentes funciones que se encargan de consultar la base de datos a las tablas correspondientes para mostrar la información que se pide, por ejemplo, mostrar todo el menu de tacos que exiten, todos los clientes, todas las ordenes, un cliente, un taco o una orden en particular.

Enseguida está la clase principal **Main** con una funcion llamada **menu()**
que en el que primero se especifícan las multiples opciones de un menu para el usuario que se imprimirán en la consola y despues está un ciclo while que maneja la impresion del menu y la entrada de teclado de la opcion que quiera el usuario y lo que corresponda a cada opcion.

# Referencias
[Scrapping en Python](https://jarroba.com/scraping-python-beautifulsoup-ejemplos/)

[Manipular cadenas de caracteres en Python](https://programminghistorian.org/es/lecciones/manipular-cadenas-de-caracteres-en-python#cortar)

[Utilizando diccionarios en python](https://librosweb.es/libro/algoritmos_python/capitulo_9/utilizando_diccionarios_en_python.html)

# Diagramas

### Diagrama de clase
![Diagrama de clase](/proyecto_final/Diagramadeclases.png)

### Diagrama entidad-relacion
![diagrama entidad-relacion](/proyecto_final/Diagramaentidad-relacion.png)
