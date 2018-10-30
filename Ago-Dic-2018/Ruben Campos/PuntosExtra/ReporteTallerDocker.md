
# Reporte de Taller de Docker

En este taller nos introdujeron a la herramienta **Docker**. 

Se nos explicó que docker utiliza contenedores, y estos contenedores tienen la capacidad de empaquetar el software, haciendo versiones ligeras que puedan ser ejecutadas en cualquier computadora en la que tengas docker instalado, independientemente del sistema operativo que tengas.

Como cada contenedor contiene el programa y todas las cosas que necesita para funcionar como código, librerías y configuraciones, puedo ejecutar el programa sin tener preocupación de que en la máquina tenga la versión necesaria de algo, si es compatible o cumple requerimientos.

## Ventajas
Esto tiene ventajas tanto como para desarrolladores como para demás gente implicada en la producción de software, ya que si por ejemplo se desarrolla una aplicación en versiones diferentes de algún lenguaje de programación, al compartir la imagen de docker a otra persona evitas posibles incompatibilidades o el tener que forzar a otro desarrollador a cambiar su entorno de trabajo y versión para seguir con el trabajo. 

## Comandos vistos:

- docker images: Muestra en una lista las imágenes disponibles.
- docker pull _nombre de imagen:[versión]_: Descarga la imagen especificada desde el [Registry de Docker](https://hub.docker.com/explore/) 
- docker rmi _Id de la imagen_: Elimina la imagen solicitada.
- docker run _nombre de imagen:[versión]_: Ejecuta el contenedor solicitado.
- docker stop _nombre de imagen:[versión]_: Detiene la ejecución del contenedor solicitado.
- docker rm _nombre de imagen:[versión]_: Elimina el contenedor solicitado.
- docker ps -a: Muestra un listado de los contenedores en ejecución y los ya ejecutados también junto con su status.

### Diferencia con Máquina Virtual
El uso de docker es parecido a las máquinas virtuales, pero la gran diferencia está en que a diferencia de una máquina virtual que se le tiene que instalar un sistema operativo (y todo el espacio que implica) para que funcione, los contenedores que se ejecutan comparten el kernel del sistema operativo de la computadora, estos los hace mas ligeros y prácticos.

### Lo hecho en el taller:
- Usamos contenedores para compilar código de Java, C y Go.
- Usamos contenedores de Nginx para crear un servidor web y phpMyAdmin para gestionar una base de datos.
- Creamos un blog con un contenedor de Wordpress a su vez usando los contenedores del punto pasado.
- Usamos contenedores para linkearlos a otros y que puedan trabajar en conjunto.
- Montamos volúmenes para enlazar nuestra computadora con el contenedor.

