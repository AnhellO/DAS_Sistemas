### How to build and test your Docker images in the cloud


En esta sesión nos volvemos a encontrar con desarrollador de la primer sesión a la que entré que es Peter Mckee
pero en esta ocasión nos comienza a explicar qué es exactamente la integración continua, dice que es donde
los desarrolladores fusionan sus cambios en un repositorio de código común cada vez que se completa una
característica o se realiza un cambio, una vez que se fusionan estos cambios, el sistema CI (Continuous Integration) 
puede ejecutar compilaciones y pruebas automatizadas para verificar los cambios, y nos dice que esto se hace
a menudo varias veces durante el día.
Entonces los desarrolladores que trabajan localmente en su máquina crean una rama de características para 
agregar una característica o arreglar un defecto y luego una vez que hayan terminado y también de ejecutar sus 
pruebas locales, realizan un push up hacia una rama remota, por lo general corta un PR y luego una vez que ese 
PR se haya cerrado,se fusiona en una rama maestra, después de esto Docker Hub está escuchando a las fusiones 
en la rama maestra y se lanza un Webhook y se envía a Hub, entonces Hub escucha ese Webhook para luego de
verificar esa rama encontrar nuestro Dockerfile, luego ejecutará la construcción de la imagen y una vez que esto se
apruebe, se ejecutarán nuestras pruebas si las tenemos configuradas. Una vez que todas las pruebas hayan pasado 
se hará un push de nuestra imagen al repositorio, y este es el flujo que nos presentó Peter en esta sesión.

Pero bueno igual por si se encuentran personas que no estén para nada familiarizadas con Docker Hub, de inmediato
recomienda que realicen su registro en la página para que puedan tener un usuario, ya que es indispensable.
Ahora si después de esto lo primero que hace es buscar cómo configurar GitHub... por lo que pide ira Docker Hub 
e inicia sesión, luego va al menú e ingresa a la configuración de la cuenta, abre el apartado de cuentas vinculadas
y en la parte inferior aparece que los repositorios de código fuente se pueden conectar a GitHub y BitBucket,
entonces da click en conectar con GitHub, le pide de nuevo que inicie sesión y con el código de autenticación
que recibe logra conectarlo, entonces ahora cuando está en proceso de hacer un nuevo repositorio en Docker Hub, 
solo selecciona si quiere conectarse a GitHub y listo.
Lo siguiente en hacer es construir una imagen, por lo que va a revisar su pequeña aplicación de NodeJS y su 
Dockerfile, luego de esto lo que hace es un push de esta imagen hacía el Hub, teclea los siguientes comandos:

	- docker login ---> luego ---> - docker push pmckee/hello-world

Esperamos un momento y listo, verifica en Docker Hub y aparece el push que acaba de realizar, ahora lo que
hace Peter es ir a su app y realiza un pequeño cambio, hace un commit y un push, va a Docker Hub y podemos
ver que tiene una compilación ejecutándose, luego se muestra que la construcción ha terminado, checa unos
registros y listo... todo en solo 15 minutos, ya no tuvo que hacer un build de la imagen localmente después de 
realizar el pequeño cambio en el código ya que solo tuvo que hacer un push y Docker lo recogió para construir
la imagen.


Lo aprendido en esta sesión fue:
	
	- En esta sesión obtuvimos información acerca de lo que es en realidad la integración continua, aprendimos
	  a crear rápidamente un repositorio en DockerHub (y claro principalmente una cuenta), también a cómo poder
	  conectar ese repositorio a GitHub y también vimos cómo evitar el hacer un build de imagenes localmente
	  después de haber realizado pequeños o grandes cambios en el código de nuestras aplicaciones, solo 
	  hacemos un push y listo, Docker se encarga y construye la imagen :) .

