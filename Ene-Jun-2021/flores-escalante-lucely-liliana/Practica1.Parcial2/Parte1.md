¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
Hablando sobre el desarrollo, la monolítica es más fácil porque solo necesita de una base de código para su manejo, pero tendría problemas al crecer el proyecto.
Por eso los microservicios son más efectivos si se trata de un proyecto grande, ya que trabaja con procesos independientes que realizan una actividad en particular y hace más fácil trabajar en ellos cuando se requuiera, ya que no afectará todo directamente si no a cada microservicio por separado.

¿En qué consiste el patrón de arquitectura monolítica?
Consiste en tener todos los servicios juntos dentro de un mismo módulo en donde su comunicación es através de la memoria.

¿Cuáles son las principales desventajas de una arquitectura monolítica?
La principal desventaja es que al estar todos los servicios juntos en más complicado trabajar con ellos ya que lo que hagas se verá afectado en todos los servicios.

¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
Las modificaciones que se realicen al código se tendrán que hacer también en las réplicas de la aplicación porque todas funcionan continuamente, si se hace un cambio por más pequeño que sea, este afecta a todo.

¿Qué sucede si falla una aplicación monolítica?
Con cualquier falla por más mínima toda la aplicación va a tener problemas.

¿En qué consiste el patrón de arquitectura basada en microservicios?
Consiste en tener dividir las tareas con la finalidad de tener varios microservicios con diferentes funcionalidades pero comunicados entre sí para que puedan actuar como uno solo, además que como trabajar por separado, es más fácil al momento de realizar cambios porque solo afectarán al que se esté trabajando.

¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
Se le agregan más funcionalidades para que no afecte a lo que ya está hecho.

¿Qué es un ambiente basado en contenedores?
Es en donde cada servicio tiene un contenedor para su ejecución independiente al resto pero con comunicación mediante una API

Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
No, cada servicio puede trabajar mediante su propio lenguaje porque son independientes entre sí.

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
Mediante los protocolos de internet, mediante un API que mantenga los servicios comunicados entre si.

¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si, porque cada servicio tiene su propia funcionalidad independiente a las demás.

¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
Cada parte se trabaja por separado, entonces se necesitará más tiempo, la comunicación entre los servicios y la seguridad van a depender de la red en la que se trabaje, llevar el control de cada servicio va a requerir más desarrolladores.

¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
Con los test suficientes para verificar su funcionalidad