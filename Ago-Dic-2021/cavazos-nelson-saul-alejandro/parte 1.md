###### ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
**R** dependiendo es mas dificil Microservicios cuando tienes pocoas pesonas para desarollarlo y mas si tiene experiencia nula en este patron pero facilita mas ala larga como agragar modulos, en cambio un monolito no tiene esta ventaja a largo plasa ya que para agregar un modulo se tendria que actulizar todo el sistema.

###### ¿En qué consiste el patrón de arquitectura monolítica?
**R** es unaptro en dode los modulos estan en una misma maquina virtual y secomnunican atrevez de esta 

###### ¿Cuáles son las principales desventajas de una arquitectura monolítica?
**R** que depende de una sola maquina virtual y que es mas dificil agreagar nuevos modulos 

###### ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
**R** que se tendria que actulizar y restructur todo el sistema

###### ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
**R** que falla todo el sietemas

###### ¿En qué consiste el patrón de arquitectura basada en microservicios?
**R** es un patron dode cada sistema esta separado y se comunica con los demas atraves de la red 

###### ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
**R** a lo que tengo entendido solo colapsaria ese servicio pero los de mas seguiran funcionando al 100

###### ¿Qué es un ambiente basado en contenedores?
**R** es una ambiente donde las apliciones se ejecuten de forma independiente del sistema operativo

###### Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
**R** no seria dependeiente de un lenguaje ya que la comunicacion sera atravez de la red asi que cualquier modulo podria ser escrito en un lenguaje diferente a los demas

###### Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
**R** ptincipal atraves de la red

###### ¿Los microservicios pueden ser distribuidos? ¿Por qué?
**R** si los microservicio significa que el módulo se divide en una unidad de servicio independiente para realizar la interacción de datos a través de interfaces.

###### ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
**R** la complejidad ya que cada modulo es independiente y se tiene que comunicar entre ellos atraves de la red

###### ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
**R** gracias a la orquetacion de contenedores le permiten iniciar, parar y agrupar contenedores en clusters