Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
R: La monolítica es mas facil desarrollar, debido a su corta longitud
   La hace mas facil, tambien porque reside en un solo sistema.


¿En qué consiste el patrón de arquitectura monolítica?
R: Consiste en que el software tenga una estructura en la que todas
   Las funcionalidades quedan sujetos y acoplados a un mismo programa.

¿Cuáles son las principales desventajas de una arquitectura monolítica?
R: -Una de las principales desventajas de esta arquitectura, es que al momento
   De realizar un lanzamiento de este software, se tiene que relanzar todo el
   Sistema completo de nuevo.
   -Al escalar una aplicacion con esta arquitectura, implica escalar toda la 
     Aplicación completamente, y muchas veces solo se necesita escalar una 
     Parte específica de la aplicación.
   -Otra desventaja es que, al crecer esta aplicacion, se hace muy dificil
   Desarrollarla entre varios desarrolladores, ya que una caracteristica 
   Principal de esta arquitectura es que reside en un sistema solamente.
   
¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
R:  Agregar una nueva funcionalidad implica que, aunque sea la mas minima,
    Se tenga que compilar toda la aplicación de nuevo, gastando mas recursos 
    Y tiempo.

¿Qué sucede si falla una aplicación monolítica?
R: Si alguna vez falla, esto hara que la aplicación completa falle, y el
   Sistema quede inservible por ese momento.

¿En qué consiste el patrón de arquitectura basada en microservicios?
R: Consiste en aislar los diferentes componentes de una aplicación, con
   La tarea de que cada modulo sea una app independiente.

¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
R: Esta arquitectura esta hecha para que cada funcionalidad trabaje por separado,
   Esto quiere decir que se puede escalar mucho mas, y por lo tanto, 
   si cargamos mas datos o funciones a un microservicio, no representara alguna 	dificultad    o   amenza para la aplicación.

¿Qué es un ambiente basado en contenedores?
R: Es cuando guardamos o desarrollamos una aplicación o software, dentro de   un ambiente en donde se encuentran las librerias, archivos o variables que necesita
   Para funcionar.

Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
R: No seriamos dependientes, ya que, como las funcionalidades de la aplicación
   Estan divididas, y a pesar de que se comunican entre si, cada una es
   Independiente de la otra.

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
R: Principalmente existen dos criterios. 
   -Por número de receptores: unico receptor o varios.
   	°Receptor unico: En este, cada solicitud ha de ser procesada por un 
   	 Receptor o un servicio.
   	 °Varios receptores: El ejemplo mas sencillo de este, es el de 
   	  Los microservicios.
   -Por clase de protocolo: sincrónico o asincrónico.
   	°Sincrónico: Su caracteristica principal es la de aislar lo mas que se 
   	 Pueda cada microservicio. 

¿Los microservicios pueden ser distribuidos? ¿Por qué?
R: Si pueden ser distribuidos porque esa es la idea principal de la arquitectura
   de microservicios, que se distribuyan en varias partes para que varios
   Desarrolladores puedan trabajar en la misma aplicación al mismo tiempo y asi
   Reducir el tiempo de trabajo.

¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
R: El desafío mas grande de esta arquitectura, reside en la dificultad
   De enlazar o comunicar los multiples servicios entre si, es una tarea 
   extensa y dificil.

¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
R: Se puede garantizar gracias a que cada servicio funciona independiente, es
   Decir, que es mas facil de auditar cada servicio por separado, y 
   Gracias a que el personal encargado de cada servicio lleva a cabo el 
   Mantenimiento y la auditoria, es mas facil garantizar la disponibilidad de
   Ese servicio. 
