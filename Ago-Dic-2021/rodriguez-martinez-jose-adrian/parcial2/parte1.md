##Parte 1##

**¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?**
_Las arquitectura monolitica es mas facil de implementar y de desarrollar porque es la mas comun, pero tiene un problema de dinamismo lo que la hace dificil de actualizar conforme se hacen cambios._

**¿En qué consiste el patrón de arquitectura monolítica?**
_La arquitectura monolítica consiste en que todos trabajan en unidad. En esta arquitectura todas las funciones se acoplan y estan sujetas a un mismo programa._

**¿Cuáles son las principales desventajas de una arquitectura monolítica?**
_La desventaja es cuando comienza a crecer el proyecto ya que se hace muy comolejo el poder actualizar el mismo._

**¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?**
_Todo tiene que estar desarrollado en el mismo lenguaje y cuando hay una actualización o cambio se deben hacer a todas las replicas._

**¿Qué sucede si falla una aplicación monolítica?**
_Todo falla, ya que es un conjunto y es complicado hacer pruebas individuales._

**¿En qué consiste el patrón de arquitectura basada en microservicios?**
_Consiste en que las aplicaciones del lado del backend esta dividida en distintos componentes y esto es a lo que llamamos microservicios y cada uno de estos microservicios tiene una funcionalidad independiente._

**¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?**
_Se ocupan mas recursos y hay que buscar la manera de aumentar los recursos con los que se cuentan._

**¿Qué es un ambiente basado en contenedores?**
_Puede ser una forma fiable e independiente de un sistema operativo on de una estructura o infraestructura en donde cada proceso se lleva por separado._

**Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?**
_No, no serias dependientes a una tecnología o a un lenguaje, ya que, al estar en componentes, podemos utilizar diferentes lenguajes de programación ya que estos componentes no dependenen el uno del otro, trabajan por separado._

**¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?**
_Podrían conectarse por API'S y tambien se puede comunicar por medio de cocntenedores, ya que estos son faciles de conectar entre si._

**¿Los microservicios pueden ser distribuidos? ¿Por qué?**
_La principal funcion de los microservicios es se distribuidos para no depender los unos de los otros para asi poderlos distribuir de manera simple y que puedan funcionar con otras estructuras de manera facil y sencilla._

**¿Cuáles son los principales desafios de una arquitectura basada en microservicios?**
_Un gran desafío es contar con los suficientes recursos. Además como está por componentes hay que testearlo individualmente._

**¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?**
_Mediante la redundancia podría reducirse los incidentes de fallo._

