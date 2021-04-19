PARTE 1

1.- ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
    Sería cuestión de medir la estabilidad de nuestra aplicación además de las dimensiones que esta posee, pero sin duda, el padrón de microservicios sería más fácil de implementar, ya que, por su metodología de módulos, permite un acceso mucho más accesible al concentrar las diferentes funciones en sus correspondientes servicios. Cabe destacar la utilidad que este sería para los futuros fallos. 

2.- ¿En qué consiste el patrón de arquitectura monolítica?
	Consiste en una estructura de software concentrada en dentro de un mismo programa, de forma que la información recopilada esté operando en un único servidor. Un ejemplo se encuentra en el video, donde cada uno de los módulos implementados están a función de una sola máquina virtual.

3.- ¿Cuáles son las principales desventajas de una arquitectura monolítica?
	Para este punto, quisiera mencionar una venta que ofrece la arquitectura monolítica, pues esta es muy conocida gracias a su eficiencia, ya que el entorno en el que son desarrollados, trayendo consigo un número mínimo de fallos, sin embargo, crea entornos demasiado rígidos los cuales no pueden actualizarse fácilmente. Es aquí donde su principal ventaja se convierte en lo contrario, y es muy latente cuando el software tiende a crecer.

4.- ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
	Como se menciona anteriormente, la estructura en la cual esta construida hace que la actualización del código implementado sea muy difícil de modificar, pues al estar todo conectado, los fallos que esté presente afectasen toda la estructura, por lo que una de sus soluciones sería el pasar todo a otros servidores.

5.- ¿Qué sucede si falla una aplicación monolítica?
	Al estar todo concentrado en un mismo servidor, el fallo que tenga alguno de los módulos hará que todos los demás estén comprometidos, causando una difícil reparación.

6.- ¿En qué consiste el patrón de arquitectura basada en microservicios?
	Consiste en poder dividir una aplicación en diferentes partes, donde cada uno de estas opera de manera autónoma, además de estar comunicadas con las demás, permite una mayor escalabilidad en los diferentes servicios de los cuales este opera: Desarrollar sus funciones de diversos lenguajes de programación, así mismo en diferentes bases de datos.

7.- ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
	Cada uno de los servicios requiere de su propia complejidad, lo que podría ocurrir es que el servidor al que este designado llegue a saturarse.

8.- ¿Qué es un ambiente basado en contenedores?
	Consiste en una aplicación de los microservicios, donde cada uno implementa un contenedor propio en sus diversas funciones correspondiente a distintas bases de datos y lenguajes de programación, los cuales son comunicados mediante el uso de una API.

9.- Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en      específico o no?, ¿y por qué?
    No, ya que al estar cada uno de los servicios comunicados, la única relación que estos comparten es la información que constantemente fluye dentro de las aplicaciones, independiente de la tecnología implementada.

10.- ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
	La forma en la que estos pueden comunicarse es por la implementación de la API, así mismo de los mismos protocolos de red.
	
11.- ¿Los microservicios pueden ser distribuidos? ¿Por qué?
	Si, porque cada uno opera de diferente manera, solo se encuentran comunicados unos con los otros.

12.- ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
	El tiempo, pues al tener diferentes servicios con sus distintas funcionalidades, una dificultad grande a encontrar es el tiempo para su mantenimiento y ver si trabaja de manera correcta.

13.- ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
	Mediante sus pruebas.
