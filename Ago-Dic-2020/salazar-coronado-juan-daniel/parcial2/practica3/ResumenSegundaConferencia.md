# Best Practices for Compose-managed Python Apps

### Daniel Salazar - 17289193

La segunda conferencia que trata sobre mejores practicas para el desarrollo de
aplicaciones de python haciendo uso de docker compose me ha ayudado mucho a entender
el uso de docker compose con un docker file, un archivo de python como tal y requeri-
mientos exernos como flask, con esta conferencia he podido darme una idea de como se
debe hacer la practica dos y como podemos mejorar nuestro desarrollo sin la necesi-
dad de estar instalando todo en nuestra computadora pues docker nos ayuda en este
tipo de situaciones, para empezar la conferencia comienza explicando una aplicacion
sencilla en python que hace uso de flask, después crea un dockerfile simple para
levantar una imagen que corra está aplicación, despupes nos muestra la creación de un
docker compose para poder levantar nuestra imagen junto con un servidor de bases de
datos. Al finalizar esto se nos muestran mejores practicas para el manejo de este 
tipo de aplicaciones, como el levantar volumes para que los datos de nuestra base
de datos no se pierdan en el momento de dar de baja el contenedor o algo por el 
estilo. 

En la segunda parte de la conferencia se realiza un "demo" por decirlo así, pues la
conferencista realiza su aplicación de python, una que da un mensaje como hola mundo
y además se conecta a una api para traer nombres de blogs, crea su archivo de 
requirements, el docker file necesario para crear esta imagen y también explica como
es que funciona y el motivo de cada uno de los comandos que contiene y para terminar
crea el archivo de docker compose para levantar los otros servicios de los que va a
hacer uso, después se nos muestra como levanta los servicios con el docker compose
build y el docker compose run, hace la prueba de la aplicación haciendo uso de la 
interfaz grafica que brinda el docker desktop y nos muestra como hace las consultas
de la bd y como es que si da los mensajes que especificaba en la aplicación de 
python. algo que me sorprendio mucho es que luego de realizar esto estuvo editando el
archivo como tal y se mostro que el docker compose actualizaba automaticamente sus
servicios para obtener los cambios que tenia el archivo de python y así poder mostrar
un mensaje diferente como "hola desde docker". y después siguio editando el archivo y
se nos mostro como es que es una buena practica parar el servicio de docker compose 
para que no esté generando errores innecesarios y solamente actualizarlo cuando se 
tenga toda la aplicación lsita por completo.

Este tipo de ejemplos se me hacen muy utiles por que muestra desde el inicio cada
detalle que se necesita para poder entender como se realiza una aplicación de python
y luego se dockeriza poco a poco sin necesidad de utilizar comandos externos. Creo
que esto por ejemplo nos puede dar a entender lo util que puede ser docker para la
arquitectura de microservicios, como podrían levantarse distintos servicios desde un
docker compose desde distintos lugares sin necesidad de hacer uso de servidores o
cosas por el estilo, solamente contenedores, creo que si esta herramienta se sigue
haciendo más conocida y se empieza a difundir información en todos los idiomas y no
solo ingles será muy util para todas las personas que empiecen a desarrollar o estén
en el proceso de estudio como yo. 