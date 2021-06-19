# justifiques de mi diagrama 

El método que utilice fue como le fui entendiendo que este programa funciona flask + Docke, me fui basando en las imágenes y archivos que venían en el git fui leyendo cada de ellas y básicamente lo que es flask permite crear aplicaciones web rápidamente y con un mínimo número de líneas de código, Todo está pagina de docker + flask se centra en el docker-compose que dé hay parte todo mi diagrama básicamente todo está conectado por medio del docker-compose.yml las diferentes librerías que utiliza, y todas las diferentes 'apps' que se encuentran en el docker compose, también lo hice fue meterme a todos los archivos que vienen en el git para ver que estaba conectado con que en los diferentes 'scripst' de todos lo que están y a sí fui relacionando el diagrama
El diagrama funciona de la siguiente manera:
docker-file: este archivo tiene toda la ecensia en si respecto a los programas que se ejecuta en toda la app
Page: Colocar Vistas, Templates y se Guarda HTML, JavaScript y Assets.
DB: Conexiones a Data Base.
Debug_ToolBar: Monitorear errores, Por ejemplo llamada a algun servidor y se excedio el tiempo.
Flask_static: Metodos estaticos para produccio, quiere decir que cuando se sube a algun servidor y mnificar los archivos.
Flask: Se encarga del Manejo de las Rutas.
Celery: Majeo de Llamadas, Tareas y peticiones asincronas y sincronas, se encarga de (vista - servidor - Base de datos)
DebugApp: Debugear la aplicacion.
Proxy: Realiza peticiones seguras que acepte protocoles de HTTPS.
