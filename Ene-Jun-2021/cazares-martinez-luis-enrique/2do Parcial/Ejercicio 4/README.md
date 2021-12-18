Ejercicio 4

FLASK

(La aplicacion de git docker-flask-example no corrio en mi equipo, asi que supuse que tendriamos que hacer
un Diragrama sobre como Funciona FLASK)


La aplicacion en general sirve como ejemplo o guia para "Dockerizar" alguna aplicacion "Flask" existente.
Flask es un “micro” framework escrito en Python y concebido para facilitar el desarrollo de 
aplicaciones Web bajo el patrón MVC.

Podemos definir framework como un esquema
para el desarrollo o la implementación de una aplicación. En general los framework están asociado a lenguajes de programación 
(Ruby on Rails (Ruby), Symphony (PHP),…).

Las ventajas tiene utilizar un ‘framework’ pueden ser:

	► Facilita la colaboración. Cualquiera que haya tenido que “pelearse” con el código fuente de otro 
	programador sabrá lo difícil que es entenderlo y modificarlo; por tanto, todo lo que sea definir y estandarizar va 
	a ahorrar tiempo y trabajo a los desarrollos colaborativos.

	► Es más fácil encontrar herramientas (utilidades, librerías) adaptadas al framework concreto para facilitar el desarrollo.

El diagrama funciona de la siguiente manera:

Hello : Implementa todo, Como punta de Iceberg carpeta Raiz.

Page: Colocar Vistas, Templates y se Guarda HTML, JavaScript y Assets.
DB: Conexiones a Data Base.
Debug_ToolBar: Monitorear errores, Por ejemplo llamada a algun servidor y se excedio el tiempo.
Flask_static: Metodos estaticos para produccio, quiere decir que cuando se sube a algun servidor y mnificar los archivos.

Flask: Se encarga del Manejo de las Rutas.

Celery: Majeo de Llamadas, Tareas y peticiones asincronas y sincronas, se encarga de (vista - servidor - Base de datos)
DebugApp: Debugear la aplicacion.
Proxy: Realiza peticiones seguras que acepte protocoles de HTTPS.
