# Practica 1 - Parte 1

¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
A simple vista parecería que la arquitectura monolítica es más fácil de trabajar ya que utiliza una sola base de código para manejar todos sus servicios y funciones, pero esto al final se volvería una desventaja si más desarrolladores trabajan en conjunto o si el proyecto llegara a crecer. En mi punto de vista es más fácil el de microservicios, ya que se separan sus funciones y componentes, para funcionar como aplicaciones independientes conectadas entre sí.  

¿En qué consiste el patrón de arquitectura monolítica?
Módulos o servicios integrados corriendo de tal forma que toda su comunicación pasa a memoria entre llamadas a métodos funcionando como una sola unidad.

¿Cuáles son las principales desventajas de una arquitectura monolítica?
Es difícil o casi imposible trabajar en varios ambientes al mismo tiempo, toda la aplicación debe ser desarrollada en un mismo lenguaje de programación, no es la mejor opción en el caso de que el proyecto llegara a crecer y mas usuarios o desarrolladores trabajaran en ella, si se desea realizar algún cambio este tendrá que realizarse a todo el proyecto.

¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
Si hacemos una actualización de código o agregamos una nueva funcionalidad, tendremos que hacerlas también en las réplicas de la aplicación ya que todas están funcionando conjuntamente, además si haces un pequeño cambio en la aplicación toda la aplicación deberá ser desplegada para que vuelva a funcionar, no puedes hacer un cambio especifico, si haces un cambio hay que cambiarlo todo.

¿Qué sucede si falla una aplicación monolítica?
Ya que todo funciona conjuntamente si un componente falla, toda la aplicación fallara ya que todo está funcionando como una unidad.

¿En qué consiste el patrón de arquitectura basada en microservicios?
Consiste en aislar los distintos componentes de una aplicación, con el fin de que cada uno sea una aplicación o bien un servicio por si mismo. La arquitectura basada en microservicios es realmente programación distribuida.

¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
Como cada servicio se comunica por separado y cada uno tiene una funcionalidad especifica, cada uno puede ir evolucionando independientemente de los otros sin interrumpirse entre servicios.

¿Qué es un ambiente basado en contenedores?
Son los servicios implementados en contenedores, estos contenedores se comunican entre ellos a través de API.

Si utilizáramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
No, por ejemplo, una aplicación grande puede ser administrada en partes (microservicios), estos servicios podemos desarrollarlos en diferentes lenguajes de programación y cada servicio puede estar conformado por una base de datos distinta, ya que al final cada uno de estos servicios se caracterizan por su entrada y salida de información y no por su tecnología. 

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
Se comunican a través de protocolos de internet y también pueden comunicarse entre ellos a través de API.

¿Los microservicios pueden ser distribuidos? ¿Por qué?
si, los microservicios son componentes distribuidos en nuestro sistema donde cada componente va a exponer una funcionalidad al resto del sistema, entonces de esta forma modularizamos nuestro sistema a través de estos servicios independientes.

¿Cuáles son los principales desafíos de una arquitectura basada en microservicios?
Cuando tenemos múltiples aplicaciones distribuidas y son pocos desarrolladores o si no se tiene mucha experiencia en sistemas distribuidos esto hará que el desarrollo sea más lento, en los microservicios se testea cada parte por separado y esto consume mucho tiempo, la comunicación de cada servicio depende de la red y la seguridad, escribir código para comunicar servidores puede ser una tarea difícil y además convertir datos también requiere mucho más procesado por parte del servidor ya que va a tener que obtener datos y compartirlos.

¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
A través de la réplica de múltiples de sus servicios y testearla para ver si todo está funcionando correctamente.