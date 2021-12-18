PARTE 1
Arquitectura Monolitica y Microservicios


¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
- Los microservicios son mucho más fáciles de trabajar que las aplicaciones monolíticas ya que se tarta
  de una programacion distribuida y por lo tanto hay mas agilidad al momento de llevar una aplicacion en desarrollo hasta su producción.

¿En qué consiste el patrón de arquitectura monolítica? 
- El estilo arquitectónico monolítico consiste en crear una aplicación autosuficiente que contenga absolutamente toda la funcionalidad 
  necesaria para realizar la tarea para la cual fue diseñada sin contar con dependencias externas que complementen su funcionalidad.

¿Cuáles son las principales desventajas de una arquitectura monolítica?
- 	• Si hacemos una actualizacion en nuestra aplicación se tendra que hacer en todo el codigo que ya esta implementado en la App.
	• No se puede imcremetar el hardware o recursos a nuestra aplicación.
	• Uno de los mas contundentes es que toda la Aplicaccion tiene que estar desarollada en un solo lenguaje de programación.
	• Si algo falla toda nuestra App toda esta falla.


¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
- Si se desea hacer un cambio o agregar una nueva funcionalidad se tiene que desplegar toda la aplicacion para que se haga un cambio en todo.

¿Qué sucede si falla una aplicación monolítica?
- Si algo falla por mas pequeño que sea, toda esta falla.

¿En qué consiste el patrón de arquitectura basada en microservicios?
- Una arquitectura de microservicios consta de una colección de servicios autónomos y pequeños. 
  Los servicios son independientes entre sí y cada uno debe implementar una funcionalidad de negocio individual.

¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
- Libre de cambios no pasa nada si se añade o modifica algun servicio Debido a que cada uno está separado de los otros, 
  se mejora el aislamiento de fallas.

¿Qué es un ambiente basado en contenedores?
- Los contenedores ofrecen un mecanismo de empaquetado lógico en el que las aplicaciones se pueden abstraer del entorno en el que se ejecutan.

Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
- No, ya que podemos trabajar independientemente de cualquier lenguaje ya que cada servicio depende de ciertas tecnologias y lenguajes,
  podriamos usar muchos lenguajes y tecnologias en una misma app que utilice Microservicios.

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
- La comunicación entre estos servicios se realiza mediante protocolos como HTTP, AMQP y TCP. 
  Con una API de REST para servicios web.

¿Los microservicios pueden ser distribuidos? ¿Por qué?
- Si, los servicios se comunican entre sí mediante API bien definidas. 
  Los detalles de la implementación interna de cada servicio se ocultan frente a otros servicios. 

¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
-	• Definición clara de los límites de microservicios: 
	  Cada microservicio debe formar parte de la aplicación y a la vez ser autónomo con todas las ventajas y los desafíos que eso conlleva.
 	
	• Diseñar comunicación entre los límites de microservicios: 
	  Comunicarse a través de los límites de los microservicios supone un verdadero reto. 
	  
	• Coherencia entre microservicios: 
	  Según hemos definido, los datos que pertenecen a cada microservicio son exclusivos de cada microservicio y solo se pueden acceder a ellos mediante la api del microservicios.


¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
-  El estado trata de cuando el microservicio informa sobre su estado actual para que se tomen las medidas oportunas. 
   Un buen ejemplo es trabajar con los mecanismos de actualización e implementación para mantener la disponibilidad.

