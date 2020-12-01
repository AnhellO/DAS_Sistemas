## Comentarios

Estuvo divertida la practica.
Ya habia usado mongo, pymongo y requests un poco antes. Lo que si nunca habia usado antes de la clase era docker. No conocia sobre contenedores, menos sobre docker-compose. Siento que como hice la practica puede que no haya sido de la mejor manera, y no pude hacer que el contenedor de flask se inicializara *despues* de que terminara el contenedor de python.

Intente varias cosas, lo mas cerca que estuve fue haciendo un script de bash desde el contenedor de flask para que pingeara al contenedor de pyhon en un while y hasta que no tuviera respuesta se acabara el ciclo. Pero no funcionaba bien, y no supe bien donde ponerlo; Osea la idea era ponerlo en el CMD, que segun lo que lei es el comando que se ejecuta por default en un contenedor, pero luego no sabia donde poner el comando de python que iniciaba la app de flask. Lo trate poniendo como un RUN en el dockerfile, pero esos se corren al momento de buildear la imagen entonces uhhh, no se bien que paso esa vez.

Lo que termine haciendo fue hacer un html que fuera renderizado cuando no pudiera renderizar el index, por que aun no habia datos.

Tambien un error que me tomo mucho tiempo en darme cuenta, fue de que no sabia que docker-compose solo te corria los contenedores si la imagen ya existia, entonces no sabia por que los cambios que estaba haciendo no se reflejaban (luego vi lo del parametro --build). Pero bueno, siento que docker y la contenerizacion en general tiene muchismos usos utiles. Aun no lo se usar bien, y aun asi puedo ver que tan util puede llegar a ser.