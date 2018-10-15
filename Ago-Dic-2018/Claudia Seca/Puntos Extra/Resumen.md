09/10/2018

*meztli.vergara@justia.com*

*www.skema.word.com*


# Voice Search - Justia
### By Meztli Vergara

### Es una función que permite a los usuarios buscar cosas por medio de voz en lugar de texto, lo cual hace que la automatización sea de manera natural.


## Asistente Virtual

-	Google (Android)
-	Siri (Iphone)
-	Emy (Huawei)
-	Alexa (amazon)
-	Bixby (Samsung)
-	Cortana (Windows)


## Como cambia el internet

-	Semántica
-	Términos
-	Conversacionales
-	Datos Estructurados


## Datos Estructurados

Ayudan a los navegadores a entender la información (*Microdata, RDfa, JSon, LD*)


## Tarjetas de Información

-	Resultado (Geolocalizaciones y/o gráficas)
-	Gráfica de conocimiento
-	Preguntas Relacionadas (Términos conversacionales)

*Machine Learning by Google: https://www.youtube.com/watch?v=Hgav0LQAN6A*


## Herramientas para pruebas de datos estructurados

-	Legal Service


## Optimizar Contenido

Formato de preguntas y respuestas 
Google cuenta con el servicio “Mi Negocio” el cual provee una plataforma gratuita a negocios para próximas búsquedas de los usuarios y cuenta con actualización de este e incluye datos estructurados.
El futuro es: *Google Duplex, Voice Shooping, Smart home*


## Domótica: 

-	Utiliza aparatos muy tecnológicos para mejorar las tareas 
-	Ingeniería Social






11/10/2018

*hecdan8@hotmail.com*

# Introducción a Docker – Click It
### By Héctor Aguirre


## Docker es una tecnología de virtualización con una amplia variedad de lenguajes donde se puede tener de uno a muchos contenedores en ejecución.
Un contenedor es una forma de separar los procesos. Docker cuenta con imágenes que también se crean de una manera especial las cuales serán usadas al lanzar un container.
Una imagen de Docker es un conjunto de capas.


## Como Recursos de Virtualización:

-	Host
-	Computador

*Se construye todo desde cero.*


## Como Recursos de Containers:

-	Archivos .dll
-	Computador

*Se hace uso de los recursos*


## Comandos más comunes

-	Mainteiner
-	From (de quien se hace mantenimiento)
-	Add (crea capas)
-	Env (define construcción)
-	Enty point (define entrada de inicio)
-	Cmd (añade parámetros al entry point)
-	expose (permite abrir y correr archivos dentro del container)


## ¿Por qué usar Docker?

Porque crea ambientes inmutables, además de ser muy portable, nos brinda seguridad al manejar un ambiente aislado. Para hacerlo seguro es necesario que los procesos NO tengan privilegios de root.







09/10/2018 – 11/10/2018

*cm@paybook.com*
*www.paybook.com*


# Aplicaciones y Servicios Basados en Arquitectura Docker – Pay Book
### By Claudio Montoya – Infrastructure Manager


# Docker

## Docker hace uso de código abierto el cual nos permite mostrar aplicaciones, ejecutar funciones y editarlas dentro de contenedores, siendo de gran ayuda para el desarrollo de software, para administrar sistemas de bases de datos, servidores, páginas web entre muchos otros.
Dentro de este taller aprendimos a usar contenedores, con imágenes, usamos comandos que son muy similares a los de Linux. También utilizamos la máquina virtual, para poder trabajar con Docker, ya que Docker solo es compatible con Windows enter Price o Windows Pro.
Primero instalamos Virtual box, luego añadimos el archivo Docker. Una vez lista la maquina iniciamos sesión para comenzar a trabajar.


## Comandos
	
-	-- link (va a enlazar el conteiner de una BD al local Host)

-	-d (se ejecuta back door para seguir trabajando)

-	docker exec (ejecuta comandos dentro de un conteiner

-	docker images (muestra las imágenes de docker)

-	docker pull (nombre de imagen: versión) – (descarga imágenes) 

-	docker rm (nombre de imagen: versión) – (elimina el contenedor)

-	docker rmi (id contenedor) - (elimina imágenes)

-	docker ps -a (muestra los conteiners en ejecución)

-	docker run (id contenedor: versión) – (lanza el conteiner)

-	docker stop (id contenedor: versión) – (detiene la ejecución del conteiner


## Conclusiones

Hicimos una conexión al local host con PHP My Admin, mostramos código y ejecutamos prints de java, C y GO, modificamos puertos y creamos un blog en wordpress.
En lo personal pude observar que con Docker es más sencillo desarrollar o dar mantenimiento a un sistema, ya que ahorramos tiempo al no tener que descargar intérpretes de lenguajes o cualquier otro software, ni instalar paquetes y las librerías que utilizan estos. 
Hoy en día se trabaja con Docker en importantes empresas como Pay Book y Click IT, por ello la importancia de aprender a manejar esta tecnología tan enfocada en el uso de la nube. 


