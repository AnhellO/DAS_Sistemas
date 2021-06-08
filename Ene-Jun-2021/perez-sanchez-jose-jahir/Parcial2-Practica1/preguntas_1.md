¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
-Yo opino que es más sencillo desarrollar un patron Monolítico, ya que todo esta en la misma unidad
y eso para mi entender es mucho mas facil de desarrollar que tener los diferentes servicios por separado.

¿En qué consiste el patrón de arquitectura monolítica?
-Los componentes de la aplicación del lado del servidor, funcionan como una sola unidad conjunta.

¿Cuáles son las principales desventajas de una arquitectura monolítica?
-Si algo falla, todo falla. 
Todo tiene que estar en el mismo lenguaje.
El uso de recursos aumenta bastante.
No se puede reutilizar.
Si cambias algo, tienes que cambiar todo.

¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
-Que al intentar agregar esta funcionalidad tendremos que cambiar todo para que pueda funcionar.

¿Qué sucede si falla una aplicación monolítica?
-Si falla cualquier cosa al estar todo unido, todo la estructura fallara.

¿En qué consiste el patrón de arquitectura basada en microservicios?
-Las aplicaciones por lado del backend estan dividas en multiples partes o servicios, que son procesos indepedientes.

¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
-Que exista un retraso en los otros servicios y pueda molestar esto al cliente.

¿Qué es un ambiente basado en contenedores?
-Es aplicación que se ejecuta de forma consistente y confiable, independientemente del sistema operativo o del ambiente de infraestructura, los contenedores agrupan todo lo que necesita el servicio para ejecutarse.

Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
-No seriamos dependientes de ningun lenguaje ni tecnología, ya que al estar separado cada proceso pueden usar cualquier leguaje o tecnología que necesiten, esto de hecho es una de las caracteristicas de los microservicios.

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
-Por clase de protocolo: sincrónico o asincrónico.
Por número de receptores: uno o varios.
Via APIs

¿Los microservicios pueden ser distribuidos? ¿Por qué?
-Pues en teoria ya estan distribuidos al tener a cada uno por separado o al menos eso entiendo

¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
-Diseño, pruebas, control de versiones, implementacion, registro, monitoreo, depuracion y conectividad.

¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
-Desplegar varias instancias de un mismo microservicio en distintos nodos/máquinas con el objetivo de que si una de ellas se cae o falla, poder seguir dando servicio con el resto de instancias. 