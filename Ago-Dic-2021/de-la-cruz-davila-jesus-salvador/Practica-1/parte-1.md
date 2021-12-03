<h1>Parte 1</h1>
<h3>¿Que patron es mas facil de desarrollar (Monolitica vs. Microservicios), y por qué? </h3>
<p>R = Las arquitectura monolitica es mas facil de implementar o de desarrollar ya que es con la que mas estamos familiarizados y con esta arquitectura es con la que trabajamos sin darnos cuenta, el unico problema viene cuando una aplicación empieza a crecer, es mas dificil y complejo de administrar.</p>
<br>

<h3>¿En qué consiste el patrón de arquitectura monolítica?</h3>
<p>R = Consiste en que todas las partes o componentes, trabajan en unidad, esto del lado del servidor, es la que esta ejecutando los algoritmos y todo. En esta arquitectura todas las funciones se acoplan y estan sujetas a un mismo programa.</p>
<br>

<h3>¿Cuáles son las principales desventajas de una arquitectura monolítica? </h3>
<p>R = Una de las principales desventajas es que es mas dificil trabajar con ella cuando una aplicacion comienza a crecer, ya que es complicado manejar todos los componentes cuando son en masa o muy grandes estando en un servidor y eso requiere mas recursos.</p>
<br>

<h3>¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad? </h3>
<p>R = El problema es que cuando queremos agregar una funcionalidad o actualizacion, tambien tenemos que agregarsela a las replicas de este.
Tambien que todo tiene que estar desarrollada en el mismo lenguaje de programación.</p>
<br>

<h3>¿Qué sucede si falla una aplicación monolítica? </h3>
<p>R = Si un componente falla, toda la aplicacion o el programa falla, por que este trabaja conjuntamente y es muy dificil testear lo que esta pasando.</p>
<br>

<h3>¿En qué consiste el patrón de arquitectura basada en microservicios? </h3>
<p>R = Consiste en que las aplicaciones del lado del backend esta dividida en distintos componentes y esto es a lo que llamamos microservicios y cada uno de estos microservicios tiene una funcionalidad independiente </p>
<br>

<h3>¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios? </h3>
<p>R = Se ocupan mas recursos y hay que buscar la manera de aumentar los recursos con los que se cuentan.</p>
<br>

<h3>¿Qué es un ambiente basado en contenedores? </h3>
<p>R = Puede ser una forma fiable e independiente de un sistema operativo on de una estructura o infraestructura en donde cada proceso se lleva por separado</p>
<br>

<h3>Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué? </h3>
<p>R = No, no serias dependientes a una tecnología o a un lenguaje, ya que, al estar en componentes, podemos utilizar diferentes lenguajes de programación ya que estos componentes no dependenen el uno del otro, trabajan por separado.</p>
<br>

<h3>¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios? </h3>
<p>R = Se pueden conectar por medio de API'S y tambien se puede comunicar por medio de cocntenedores, ya que estos son faciles de conectar entre si. Otra de las maneras es por medio de los protocolos web HTTP.</p>
<br>

<h3>¿Los microservicios pueden ser distribuidos? ¿Por qué? </h3>
<p>R = Si, pueden ser distribuidos, esta es su principal funcion, no depender los unos de los otros para asi poderlos distribuir de manera simple y que puedan funcionar con otras estructuras de manera facil y sencilla</p>
<br>

<h3>¿Cuáles son los principales desafios de una arquitectura basada en microservicios? </h3>
<p>R = Uno de los principales desafios es contar con los suficientes recursos para poder trabajar de esta manera.
Otro de los desafios es, el hecho de que este desarrollado en componentes, hay que testear cada uno de ellos por separado y eso nos consume tiempo. Una de las cosas que yo considero, esto a nivel personal, que es un desafio es el aprender distintos lenguajes de programación, por que estos estan en componentes y pueden estar desarrollados en distintos lenguajes de programación.</p>
<br>

<h3>¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios? </h3>
<p>R = Podria ser evitando que falle algun componente mediante la redundancia y asi reducir la probabilidad de que ocurran multiples fallas en lo que se esta trabajando.</p>
<br>