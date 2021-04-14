#**PARTE 1**


####**¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?**

-  microservicios ,tiene como objetivo aislar los distintos componentes de una aplicación, con el fin de que cada uno sea una aplicación por sí misma

-  Seguridad: cualquier problema o fallo que suceda con un microservicio, solo afectará a éste

-  Flexibilidad: los microservicios son mucho más fáciles de trabajar que las aplicaciones monolíticas ya que si se quiere modificar de como estaba antes o acltualizar de alguna manera se  debería relanzar todo el sistema de nuevo.



####**¿En qué consiste el patrón de arquitectura monolítica? **
-   El estilo arquitectónico monolítico consiste en crear una aplicación autosuficiente que contenga absolutamente toda la funcionalidad necesaria para realizar la tarea para la cual fue diseñada, sin contar con dependencias externas que complementen su funcionalidad. En este sentido, sus componentes trabajan juntos, compartiendo los mismos recursos y memoria. En pocas palabras, una aplicación monolítica es una union y un conjunto de relacion de todo el código.

####**¿Cuáles son las principales desventajas de una arquitectura monolítica?**
-   Si hacemos una actualizacion en nuestra aplicaccion tambien se tendran que hacer en todo el demas codigo que ya esta implementado en la App.

-   No se puede imcremetar el hardware o recursos en si a nuestra aplicaccion sin que le aumentemos al resto de las aplicacciones ya que todas estan trabajando conjuntamente asi que si se le quiere poner o quitar algo a nuestra app se le tiene que quitar ao poner a todo nuestro conjunto de App.

-   Uno de los mas contundentes es que toda la Aplicaccion tiene que estar desarollada en un solo lenguaje de programacion

-   Si algo falla por mas pequeño que sea toda nuestra App toda esta falla 


####**¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?**
-   Si se desea hacer un cambi o agregar una nueva funcionalidad se tiene que desplegar toda la aplicacion para que se haga un cambio en toda

####**¿Qué sucede si falla una aplicación monolítica?**
-   Si algo falla por mas pequeño que sea toda nuestra App toda esta falla

####**¿En qué consiste el patrón de arquitectura basada en microservicios?**
-   El estilo de arquitectura de microservicios es un método para desarrollar una sola aplicación en un grupo de pequeños servicios. Cada servicio se ejecuta en su propio proceso. El mecanismo de comunicación liviano (generalmente API de recursos Http) se utiliza para la comunicación entre servicios. Los servicios se basan en las capacidades empresariales y se pueden implementar de forma independiente a través de un mecanismo de implementación totalmente automatizado. Estos servicios comparten una gestión centralizada mínima. Los servicios se pueden desarrollar en diferentes idiomas y utilizar diferentes tecnologías de almacenamiento de datos.

####**¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?**
-   Libre de cambios no pasa nada si se añade o modifica algun servicio Debido a que cada uno está separado de los otros, se mejora el aislamiento de fallas.

####**¿Qué es un ambiente basado en contenedores?**
-   Los contenedores ofrecen un mecanismo de empaquetado lógico en el que las aplicaciones se pueden abstraer del entorno en el que se ejecutan. Esta separación permite que las aplicaciones basadas en contenedores se implementen de manera fácil y uniforme, independientemente de si el entorno objetivo es un centro de datos privado, la nube pública o incluso la laptop personal del desarrollador. La creación de contenedores ofrece una separación clara de inquietudes, ya que los desarrolladores se enfocan en la lógica y las dependencias de su aplicación, mientras que los equipos de Operaciones de TI se pueden concentrar en la implementación y la administración sin preocuparse por los detalles de las aplicaciones, como las versiones específicas del software y las configuraciones específicas de la app.

####**Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?**
-   No, ya que podemos trabajar independientemente de cualquier lenguaje tecnologia etc ya que cada servicio depende de siertas tecnologias y lenguajes podriamos usar muchos lenguajes y tecnologias en una misma app que utilice Microservicios

####**¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?**
-    La comunicación entre estos servicios se realiza mediante protocolos como HTTP, AMQP y TCP. Los mensajes HTTP/REST y asíncronos son los protocolos más utilizados.

-   Una API de REST para servicios web comúnmente usa el protocolo HTTP. Con los métodos HTTP (como GET, POST, PUT y DELETE), los clientes pueden acceder y manipular los recursos de la aplicación mediante un localizador uniforme de recursos (URL).

####**¿Los microservicios pueden ser distribuidos? ¿Por qué?**
-   Si pero se dise que es muy complicado y tambien poder implementarlo, para esto existen una serie de patrones que nos ayudan con la solución a este problema:Patrón saga,Basado en coreografía,Basado en orquestación

####**¿Cuáles son los principales desafios de una arquitectura basada en microservicios?**
-   Definición clara de los límites de microservicios. Cada microservicio debe formar parte de la aplicación y a la vez ser autónomo con todas las ventajas y los desafíos que eso conlleva. 
-   Diseñar comunicación entre los límites de microservicios: Comunicarse a través de los límites de los microservicios supone un verdadero reto. En este contexto, la comunicación no hace referencia al protocolo que debe usar (HTTP y REST, AMQP, mensajería, etc.). 
-   Recuperar información de varios microservicios: El desafío se centra en recuperar información de varios microservicios sin generar un exceso de comunicación entre los microservicios. 
-   Coherencia entre microservicios. Según hemos definido, los datos que pertenecen a cada microservicio son exclusivos de cada microservicio y solo se pueden acceder a ellos mediante la api del microservicios.


####**¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?**
-   Con Comprobaciones de estado. El estado es diferente del diagnóstico. El estado trata de cuando el microservicio informa sobre su estado actual para que se tomen las medidas oportunas. Un buen ejemplo es trabajar con los mecanismos de actualización e implementación para mantener la disponibilidad. Aunque un servicio podría actualmente estar en mal estado debido a un bloqueo de proceso o un reinicio de la máquina, puede que el servicio siga siendo operativo. Lo último que debe hacer es realizar una actualización que empeore esta situación. El mejor método consiste en realizar una investigación en primer lugar o dar tiempo a que el microservicio se recupere. Los eventos de estado de un microservicio nos ayudan a tomar decisiones informadas y, en efecto, ayudan a crear servicios de reparación automática.

