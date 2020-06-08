# [DAS_FINAL_PROJECT](https://github.com/EmilioBG1997/DAS_FINAL_PROJECT)
Repositorio para el proyecto final de la materia Diseño y Arqitectura de Software.

## MATERIA
Diseño y Arquitectura de Software.

## Profesor
Ing. Angel Santiago Jaime Zavala.

## Equipo
- Angela Gabriela Sanchez Niño.
- Emilio Barrera Gonzalez.
- Juan de Dios Almaguer Constante.
- Luis Fernando Garcia Morales.

## Prerequisitos
- Docker.

## Tecnologias
- Python (flask, peewee).
- Docker, Docker-Compose.
- Redis.
- PostgreSQL.
- Pgadmin.
- Materialize.
- Microsoft Teams

## Introducción
Con este proyecto se busca demostrar que los conocimientos del profesor han sido transferidos correctamente hacia el alumno.
Se utilizarán las tecnologías que se manejaron a lo largo del ciclo escolar.

## Descripción
Utilizando las tecnlogías mencionadas anteriormente, hay que construir una serie de contenedores de **Docker** conectados entre si para servir una aplicación implementada con **Python** que mostrara una lista de heroes de DC Comics & , utilizando *flask* como framework web, estilizada con **Materialize** y *peewee* como ORM. la app es alimentada con una base de datos de **PostgreSQL** que puede ser administrada con la imagen de **pgAdmin** incluida en el *docker-compose*. Adicionalmente, se implementa un contenedor con una imagen de **Redis** para encargarse del cache generado por la base de datos para agilizar las consultas a la misma.  
 

### Estructura
En el archivo *docker-compose* se implementan 5 contenedores
- ***Contenedor A***: Contiene una imagen funcional de **PostreSQL**  
Lleva el nombre de *"dc_db"*
- ***Contenedor B***: Contiene una imagen funcional de **PgAdmin4**  
Lleva el nombre de *"dc_pgadmin"*
- ***Contenedor C***: Contiene un scrapper que se encarga de traer los datos de [superheroapi](https://superheroapi.com/) e ingresarlos a la base de datos.  
LLeva el nombre de *dc_script*
- ***Contenedor D***: Contiene una implementacion de **Flask** que se encarga de mostrar todos los datos obtenidos de [superheroapi](https://superheroapi.com/) y tambien del cache generado por el contenedor E.  
Lleva el nombre de *dc_app*
- ***Contenedor E***: Contiene una imagen funcional de **Redis**, se encarga de administrar el cache de nuestra aplicacion.  
Lleva el nombre de *dc_redis*



## Instrucciones
1. Clonar o descargar el repositorio.<br>
En caso de que lo hayas descargado, tambien hay que extraerlo.
2. Entrar a la carpeta del reposositorio y abrir una terminal en ella.
3. Detener los contenedores.  

<code>$ docker kill [container id]</code>

4. Eliminar las Imagenes.<br>
Para prevenir problemas, si sabes lo que estas haciendo puedes saltar este paso.

<code>$ docker system prune -a</code>

5. Correr los contenedores.

<code>$ docker-compose up --build</code>

>Nota: Una vez que este corriendo podremos ver en consola lo que esta ocurriendo,tomará bastante tiempo, pero hay que esperar a que aparezca en pantalla el mensaje "dc_script exited with a code 0".

6. Acceder a http://0.0.0.0:5000 para ver la app, o http://0.0.0.0:5050 para acceder al pgadmin.

<code>correo: pgadmin4@pgadmin.org</code>  
<code>contraseña: admin</code>

7. Para detener la Ejecución hay que presionar <kbd>CTRL</kbd> + <kbd>C</kbd> y esperar a que los contenedores se detengan

>Nota: Puede forzarce la detención de los contenedores si durante el proceso de detención "graciosa" se vuelve a presionar <kbd>CTRL</kbd> + <kbd>C</kbd>

8. Adicionalmente podemos verificar e interactuar con nuestros contenedores si corremos el docker-compose en modo "detached"  
<code>$ sudo docker-compose -d</code>  

### *Instrucciones Especificas* ***PgAdmin***
Para poder visualizar la base de datos se deben de realizar los siguientes pasos:
1. Ingresar a http://0.0.0.0:5050.
2. Ingresar los datos de inicio de sesion mencionados anteriormente.
3. Se un panel del lado izquierdo. Dar clic derecho en *servers* y en seguida en la opcion *create >> server*, se abrira una ventana <code>GENERAL</code> donde se ingresara DAS en el apartado *name*.
4. A continuacion hacer click en <code>Connection</code> e ingresar:

<code>name: dc_db</code>

<code>user: postgres</code>

<code>password:postgres</code>

Por ultimo se le dara en la opcion guardar.

5. En seguida les mostrara <code>DATABASES</code> en el panel del lado izquierdo, se le dara clic y les aparece la base <code>dc_heroes</code>.

## Diagramas de Arquitectura
Para poder generar nuestro diagrama de arquitectura utilizamos la herramienta de [mingrammer](https://diagrams.mingrammer.com/)
Para correr el script es necesario instalar diagrams para python y graphviz:  
<code>$ sudo apt install graphviz</code>  
<code>$ pip3 install diagrams</code>  
El script llamado horizontal.py se encarga de generar el esquema de arquitectura:  
<code>$ python3  horizontal.py</code>  
Mientras que para generar nuestro diagrama de base de datos usamos una herramienta online
Estos archivos los podras encontrar en la carpeta llamada  <code>DIAGRAMS</code>

## Tiempo
- Requests directo a la API de superheroes: 15 segundos (100 requests)
- Request a la información de la DB en PostgreSQL: 6.28x10^-5 segundos
- Request al nodo de caché en Redis: 0.02055 segundos  
Estos resultados se pueden encontrar en la carpeta <code>Evidencias</code>

## Agradecimientos
- Al Profesor Angel Santiago Jaime Zavala por brindarnos atención dentro y fuera de la clase aún dentro de estos tiempos tan complicados y por enseñarnos y orillarnos a aprender tecnologías de punta de lanza utilizadas en la vida real.
- Al equipo por la dedicación al proyecto.
- A nuestras familias por su comprensión y apoyo a lo largo del proyecto.
