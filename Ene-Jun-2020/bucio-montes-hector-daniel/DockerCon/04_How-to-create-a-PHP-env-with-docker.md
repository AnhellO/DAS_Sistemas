### How to create a PHP Development Environments with Docker Compose



En esta charla Erika Heidi nos habla sobre los entornos de desarrollo de PHP, cómo es que han cambiado
con el tiempo al igual que una visión general de Docker Compose. Al inicio ella comienza a contar sus
experiencias, muestra como hacían los entornos de desarrollo en PHP alrededor de los años 2000 - 2004,
tenían instalado el servidor Wamp o Xampp en Windows y luego usaban FTP para enviar los archivos...
Alrededor del año 2010 comenzó a utilizar Linux solo para su máquina local, y luego comenzó a usar
el entorno local de Linux y de igual manera comenzó a utilizar Git ya que todo esto le parecía mucho más 
profesional. Para el año 2014 cuenta que Docker se hizo muy popular y mucha gente empezó a usarlo 
para entornos de desarrollo y nos dice que unas de sus ventajas son que es muy rápido y ligero y que
elimina la necesidad de una gran automatización ya que podemos reutilizar mucho más y es mucho 
más rapido... sin embargo dice que algunas desventajas es que no es tan intuitivo como las máquinas virtuales,
así que la gente tardó algo de tiempo en poder comprender cómo funcionaba y cuáles eran las diferencias
entre un contenedor y una máquina virtual y también otra cosa que era muy difícil, fue cómo definir
y administrar estos servicios de manera declarativa y no como tener que ejecutar un montón de comandos 
manualmente.

Entonces ahí dice que fue cuando Docker Compose vino al rescate pero, ¿Qué es Docker Compose?...
ella nos menciona que es una herramienta que nos facilita el crear entornos de aplicaciones y los crea en
un archivo YAML, luego nos muestra cómo construir un simple archivo Docker Compose  que creará un servicio
de servidor web basado en Nginx.
Después nos enseña algunos de los comandos más comunes y relevantes para usar Docker Compose 
de la siguiente manera:

	* Para controlar el entorno...
		- up | down | stop | start
	* Para monitoreo y solución de problemas...
		- ps | logs | top | kill
	* Y para ejecutar comandos en los contenedores
		- exec 'service_name' ' command'

Erika menciona que este último comando es muy importante ya que le servirá para su caso de uso con Laravel,
porque mientras se desarrolla siempre tendrá que usar comandos artesanos o comandos PHP Composer, por lo
que es importante el tener la capacidad de ejecutar comandos dentro del contenedor, con todo el contexto y la 
base de datos y todo lo que se pueda tener desde el interior del contenedor.
Al final da una demostración de una aplicación Laravel que utiliza una base de datos MySQL para almacenar lugares
que pueden ser marcados como visitados o que faltan ser visitados...
Pero entonces ¿Cuáles son las necesidades de nuestro entorno especifíco de PHP?
	- Se necesita un servidor web y utilizará Nginx
	- También necesitará  PHP-FPM que es requerido para analizar el contenido PHP y regresar 
	  los resultados a Nginx.
	- Y una base de datos MySQL para almacenar los lugares.

 
Lo aprendido en esta charla fue:

	- El seguir viendo cómo usar Docker Compose y también fue buena la explicación de Erika acerca de 
	  cada uno de los comandos anteriormente mencionados, como los que sirven para controlar el entorno
	  (down: sirve para derribar tu entorno, eliminará todos los contenedores, redes y volúmenes,
	  stop: que sirve para detener por un momento el entorno, no eliminará nada cómo el anterior,
	  start: sirve para traerlo de vuelta, después de haber utilizado el comando stop ), y también 
	  los que son usados para el monitoreo y solución de problemas, etc.