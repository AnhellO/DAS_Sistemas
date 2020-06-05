### New Docker desktop filesharing features



El encargado de esta plática fue Dave Scott, él trabaja para Docker en Cambridge, en Reino Unido, comenzó
su plática mostrándonos cómo suele trabajar día con día, nos enseña los comandos básicos de docker, como lo
son docker run -v , docker-compose, etc., y ya vemos que su código en ese contenedor puede compilar, puede
ejecutar pruebas, puede exponer puertos, se puede conectar a su navegador y conectarse a los puertos para
probar su aplicación, checa si los cambios que ha realizado funcionan... y así nos dice que vendría siendo su "ciclo",
luego regresa al paso en el que se comparten los archivos con el contenedor, ya que de eso trata esta charla.
Menciona que él cree que el intercambio de archivos es la clave para este flujo de trabajo, y como realmente es una 
parte fundamental, debe ser confiable para empezar, porque si realiza algún cambio en su editor y no ve el cambio
en el contenedor entonces va a estar perdiendo tiempo buscando qué sucedio, además de tener errores todo el día.
Esto tiene que ser rápido ya que a nadie le gusta esperar las cosas, debe soportar inotify, que es un tipo de evento,
un evento más rápido en Linux, cuando el archivo cambia, y cada vez que el código es modificado y Linux lo sabe,
se hará de estos eventos.
Para que todo esto funcione de manera confiable y rápida con inotify, se requieren diferentes enfoques en Mac y
Windows, y requiere diferentes enfoques dependiendo de la versión de Windows que se esté utilizando.

Después comenzó a mostrarnos los problemas que tenían en Windows antes de la versión de escritorio 2.2.0.0
y estos eran esos problemas:

	- El inicio no era confiable: las redes Hyper-V chocaban con el software de seguridad.
	- La autenticación requerida: el almacenamiento de contraseñas, no había soporte de login para AzureAD o SmartCard.
	- El usuario gestionaba las direcciones IP: evitando enfrentamientos.
	- No había caché ni inotify.

Ya después de la versión 2.2.0.0 crearon las siguientes implementaciones:

	- Nueva implementación de intercambio de archivos basado en FUSE*.
	- Usaron sockets de hipervisor en lugar de la red Hyper-V.
	- Correr con privilegios de usuario.
	- Sin necesidad de autenticaciones o manejar contraseñas.
	- Sin necesidad de IP o de administrar direcciones
	- Se agregó un poco de almacenamiento en caché e implementaron inotify
	
	*(FUSE es el sistema de archivos de Linux y el espacio de usuario)

Luego presenta una demostración de cómo funciona ahora con estas implementaciones tanto en Windows como
en Mac, al hacer cambios y hacer un refresh en su aplicación, estos cambios ya fueron actualizados y ahora mucho 
más rápido gracias a la implementación del almacenamiento en caché.


Lo aprendido en esta plática fue:

	- Observar como es importante siempre estar actualizando aplicaciones como estas, siempre tratando de
	  hacer mejor las cosas, darnos cuenta de que se debe apreciar todo lo que realizan estas personas para
	  que los demás puedan obtener mejores resultados en sus proyectos, siempre haciendo las cosas cada 
	  vez más rápidas, más eficientes, por lo que hay que agradecer esta clase de implementaciones ya que
	  igual no es un trabajo fácil ya que no solo se realizan una vez, si no varias veces para que haya una buena
	 compatibilidad con los demás sistemas operativos existentes como Windows, Mac OS, etc.