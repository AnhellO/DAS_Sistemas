<center> **"RESEÑA DE CONFERENCIA JUSTIA"** </center>
========================================================
<p style="text-align: justify;">

La **Ing. Metztli Vergara Lopez** quien es parte de la empresa **JUSTIA**, fue quien nos hizo el favor de darnos una conferencia que en resumen fue acerca de ***"Web Content Optimization for Voice Search"*** .

COmo una pequeña introducción nos dijo:
¿Qué es Justia? Justia es una empresa fundada en 2003 con sede en el Silicon Valley de California, y se centra en hacer de la información jurídica, recursos y servicios fáciles de encontrar a través de sitios de Internet.

La compañía proporciona a los usuarios de Internet códigos, reglamentos, artículos jurídicos y las bases de datos en blogs legales. 

Justia está enfocada a llevar la información legal de los usuarios en línea, además, también proporciona un sitio web, blogs y otras soluciones de marketing en línea para ayudar a los abogados y bufetes de abogados de Estados Unidos tomando la información de los juicios, de las cortes, de las leyes, en si todo lo relacionado con los abogados de Estados Unidos, y estos datos la empresa lo que hace es unificarlo en un portal que es gratuito. Las leyes en Estados Unidos funcionan de una manera muy diferente a lo que estamos acostumbrados en México, digamos que en el país no funcionan como deben de ser.

Las leyes de Estados Unidos tienen una estructura muy diferente la cual es que funciona por ciudad, por congreso y toda la información es pública, entonces cualquier persona se ve involucrada en cualquier inscidente o un abogado necesita acerca de un juicio, el tiene que ir a las cortes especificas a agarrar esa información y lo que la empresa hace con esa información ellos lo meten a un portal y todas las personas que necesiten algo de esa información lo pueden hacer de manera gratuita al postear ".com".

El equipo Justia está compuesto por programadores, desarrolladores, abogados, bibliotecarios y profesionales de marketing con experiencia legal en línea y el desarrollo de la ingeniería.

¿Cómo se hace viral un **Portal gratuito**?
La forma de ganar dinero es que la empresa hace sitios Web obviamente para los mismos abogados de Estados Unidos; ellos generan un sitio con base de estandares, de frameworks ya que son los mas actuales.

Para entrar de lleno en el tema que fue "Voice Search". Este es un tema que abre como un debate acerca de como en la actualidad nos estamos volviendo realmente unos flojos y como cada vez estamos mas cerca en tipo fucionarnos a nuestro celular sin ser una máquina.

Pero primero ¿Qué es el **Voice Search**?  
En una definición sencilla es la posibilidad de utilizar un dispositivo capaz de registrar la voz humana (la tuya, en lugar de escribir), interpretar órdenes de búsqueda a través de software (entender qué le estás pidiendo) y devolver resultados presentes en un motor de búsqueda (darte soluciones prácticas).

Algunos ejemplos mas conocidos de Voice Search son:  
+ Google Assistant
+ Siri
+ Cortana
+ Alexa

Este concepto a avanzado demasiado ya que neustros ancestros utilizaban libros para encontrar respuestas de equis cosa, nuestros ancestros mas modernos utilizaban la computadora y ahora lo mas actual es que utilizamos la Voice Search de nuestros celulares.

Todo esto es mas que nada porque el tiempo vuela, los jovenes somos mas imperactivos y realmente ya no hay tiempo para textear o utilizar los dedos en el celular sino algo mas rapido y practico que es la voz.

¿Todo esto como cambia al Internet?
Más que nada es que hay que empezar a pensar que nuestros sitios tienen que ser optimizados de una manera mecánica o robotica, el lenguaje de programación por ejemplo no le dice nada a la máquina, nosotros somos quienes tenemos que proveer la semantica.

La busqueda por voz se enfoca en hacer más fácil la vida de las personas de tal manera que hace que la optimización tiene que ser de manera natural; es decir, al momento que buscamos algo en Google no ponemos toda la frase que deseamos buscar, solamente ponemos ciertas palabras y eso es suficiente para que se nos de respuesta.

Otro punto tocado en la conferencia fue los **datos estructurados**, los cuales consisten en una serie de etiquetados que describen el contenido que se encuentra en una página web, ayudando a los buscadores a entender y clasificar la información de forma más acertada.

Sitios populares optimizados para la busqueda por voz mas populares son: Netflix, Amazon, Google, sitios de noticias, entre otros.

Al último nos dijo que los de Sistemas somos el futuro, ya que siempre a cada momento estamos muy actualizados, por lo tanto somos los encargados en cambiar el mundo a nuestro gusto, ya que el chiste de aqui es la creatividad y el ingenio, que es lo que le hace falta a México.
</p>


<center> **"RESEÑA DE TALLER DOCKER"** </center>
========================================================
<p style="text-align: justify;">

En la semana de Ingenieria tome el taller"Docker" el cual duró 6 horas en tres dias. Impartida por el **Ing. Claudio Montoya**.

Para el taller solamente tome ciertas notas que me parecieron importantes.

__Requerimientos__:  
- Install and configure operating systems
- TCP/IP
- CLI semi expert
- CLI editors (nano, vim, ...)
- Virtual machines environments
- Application/Software

__Architecture__:
Traditional servers (bare metal):  
Es una computadora mas potente, que contiene mas memoria, y que puede procesar informacion mas concurrente.

*Pros*  
- Utilization of resources
- Isolation

*Cons*
- Very slow deployment time
- Expensive
- Wasted resources
- Difficult to scale
- Difficult to migrate
- Complex configuration

__Virtual machines__
Sistemas operativos que corren dentro de un servidor con base Linux

- Primera capa: Servidor fisico
- Segunda capa: Sistema Operatvo real
- Tercera capa: Hiporvisor-controla los recursos de las maquinas virtuales-Virtual Box
- Cuarta capa: Maquina Virtual con el Sistema Operativo invitado
- Quinta capa: La aplicacion

*Pros*
- Good use of resources
- Easy to scale
- Easy to backup and migrate
- Cost efficiency
- Flexibility

*Cons*
- Resource allocation
- Vendor lockin
- Complex configuration

__Containers__
Los contenedores son independientes de la arquitectura, o sea puede ser en Linux, MAC, Windows donde quieras. Solo si realizas un contenedor
en Windows no corre en Linux pero si de viseversa, aunque si realizas una aplicacion en Windows si corre en Linux sin problema

- Primera capa: Container runtime
- Segunda capa: Os Kernel
- Tercera capa: Host operating system
- Cuarta capa: Physcal server or virtual machine

*Pros*
- Isolation
- Lightweight
- Resource effective
- Easy to migrate
- Security
- Low overhead
- Mirror environments

*Cons*
- Architecture
- Resource heavy apps

¿Que es **contenedor**?
Es un paquete de software que viene en un archivo y que puede correr en cualquier arquitectura
Es una unidad de software que viene empaquetado

Ejemplos de __imagenes docker__:

- docker pull mongo
- docker pull golang:1.11.1-alpine
- docker pull wordpress:4.9.8-php7.2-apache
- docker pull nginx:stable-alpine
- docker pull gcc
- docker pull mysql:5.6
- docker pull phpmyadmin/phpmyadmin
- docker pull php:7.2.2-fpm-alpine
- docker pull java:7

Los descargas de esa manera, y si quieres descargar alguno especificamente, solo pones despues de los dos puntos la version que deseas.

Si quieres eliminar algun contenedor solo es cuestion de poner __docker rm__ y el nombre del contenedor

Si quieres eliminar alguna imagen solo es cuestion de poner __docker rmi__ y el nombre de la imagen

Si quieres saber cuantos contenedores tienes disponibles, pones __docker ps -a__

Para correr algun contenedor solo es cuestion de poner __docker run__ y el nombre del contenedor o imagen y para detenerlo es docker stop y en seguida el nombre del contenedor o imagen

</p>

<center> **"RESEÑA DE CONFERENCIA DOCKER"** </center>
========================================================
<p style="text-align: justify;">

La conferencia fue impartida por el **Ing. Hector Ochoa** quien nos dio una introducción del Docker.

__Docker__ es relativamente nuevo y un proyecto que ha crecido de forma rápida dado a que permite crear “Maquinas Virtuales” muy ligeras, (bueno, Docker no crea maquinas virtuales en si, sino que son como entornos virtuales enjaulados).

¿Qué son los __contenedores__?  
Los contenedores son la vía que nos coloca Docker para tener el mismo uso que con las maquinas virtuales creadas de la forma tradicional.

Características de un Contenedor

    Tiempo de ejecución: cada contenedor se ejecuta en un solo proceso.

    Permisos de escritura: sólo tendrá permiso a sus propios archivos y a los volúmenes asociados.

    Capas: es en una imagen en base a un sistema operativo.


Algo muy chido de Docker es que nos ayuda a no malgastar nuestro tiempo configurando el entorno, y las dependencias del sistema, porque lo vamos a poder desplegar fácilmente, además esto es muy útil para tanto empresas grandes como Google como para pequeñas startups que empiezan a desarrollar su aplicación.

Ejemplos de empresas mas conocidas que utilizan Docker:
+ Spotify
+ ING Direct
+ Uber
+ eBay
+ PayPal

¿Qué son las __imagenes en Docker__?  
Una imagen es una especie de plantilla, una captura del estado de un contenedor.

Las imágenes se utilizan para crear contenedores, y nunca cambian.

*Características de una Imagen*

    Portátil: pueden ser versionadas en los repositorios de Docker Hub, o guardarse como un archivo tar.

    Estática: el contenido no se puede cambiar, a menos que hagas una nueva imagen.

¿Qué son los __volumenes en Docker__?  
Los volúmenes son para mantener los datos más allá de la vida útil de su contenedor. 
Son espacios dentro del contenedor que almacenan datos fuera de ella, lo que le permite destruir, reconstruir y cambiar  las veces que queramos nuestro contenedor y se mantendrán intactos sus datos.

¿Es **seguro utilizar Docker**?  
Al usar secciones de kernel de host, un ataque puede realizarse para
ganar acceso al kernel principal.
Para eso debes asegurarte que los procesos corran en ambientes sin
privilegios de root, para que en caso de un ataque solo se tenga acceso
a una seccion del contenedor y no a todo.

</p>

<center> **"RESEÑA DE CONFERENCIA DevOps"** </center>
========================================================
<p style="text-align: justify;">

Y por ultimo el __Ing. Enrique Vargas__ nos dio una reseña acerca de que es DevOps.

¿Qué es __DevOps__?  
No es un rol, no es una cultura, es una metodologia, esta ayudada por una serie de herramientas y procedimientos para el desarrollo de aplicaciones de Software. 

En México hay muchas oportunidades dentro del área de DevOps.

DevOps es una metodologia de trabajo utilizada por empresas grandes como Google, Amazon, entre otras.

No se usa el ciclo casual (cascada), sino que uno en espiral que es mas veloz.

DevOps utiliza dos partes:  
- __Aplication Development__
- __Aplication Testing QA__

La finalidad de DevOps es crear las condiciones adecuadas para la colaboración entre los departamentos de desarrollo y de operaciones. 

¿Qué tecnología es necesaria para aplicar DevOps?  
Hay un pilar tecnológico indiscutible en DevOps que es la automatización.

DevOps establece una “intersección” entre Desarrollo, Operaciones y Calidad, pero no se rige por un marco estándar de prácticas, sino que permite una interpretación mucho más flexible en la medida en que cada organización quiera llevarlo a la práctica, según su estructura y circunstancias.

Algo muy claro que nos dijo el ingeniero fue:  
**"El objetivo final de DevOps es minimizar el riesgo de los cambios que se producen en las entregas y dar así un mayor valor tanto a los clientes como al propio negocio"**

Algunos objetivos que tiene DevOps fue:
- Desarrollo mas rapido
- Mayor calidad
- Mayor estabilidad
- Reduccion de costos

Planear de manera correcta tus actividades así como tus procesos es una parte fundamental de la adopción de una metodología DevOps. 

En cuanto a la __codificación en DevOps__ para que éste sea correcto se debe contar con elementos necesarios para desarrollar la codificación del proyecto y con el apoyo de herramientas capaces de ayudarnos a manejar el desarrollo. 

Al ultimo nos dijo que DevOps es importante por la eficiencia, rapidez y la calidad al reducir el downtinme y riesgo de produccion. Los clientes estan mas satisfechos con la reduccion de costos y la mejor calidad entregada.

</p>