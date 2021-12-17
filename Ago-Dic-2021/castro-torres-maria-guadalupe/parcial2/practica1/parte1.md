############PARTE_1#######################


1¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
El patron de microservicios es mas facil de desarrollar ya que se pueden formar equipos multifuncionales sin demasiado esfuerzo al igual que al momento de eliminarlos, esto se debe a que dentro de este patron de arquitectura cada elemento es independiente, espor eso que es mas facil de desarrollar

2¿En qué consiste el patrón de arquitectura monolítica?
Consiste en crear una aplicación autosuficiente que contenga absolutamente toda la función necesaria para realizar la tarea para el cual fue diseñado, sin contar con dependencias externas que complementen su funcionalidad. En este sentido, sus componentes trabajan juntos, compartiendo los mismos recursos y memoria. 

3¿Cuáles son las principales desventajas de una arquitectura monolítica?
Uno de los mas contundentes es que toda la Aplicaccion tiene que estar desarollada en un solo lenguaje de programacion

Si algo falla por mas pequeño que sea toda la App falla

4¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
Si se desea hacer un cambio o agregar una nueva funcionalidad se tiene que desplegar toda la aplicacion para que se haga un cambio en toda

5¿Qué sucede si falla una aplicación monolítica?
Si algun proceso falla por mas pequeño que sea el detalle toda la App falla

6¿En qué consiste el patrón de arquitectura basada en microservicios?
Consiste en poder dividir una aplicación en diferentes partes, donde cada uno de estas opera de manera autónoma, además de estar comunicadas con las demás, permite una mayor escalabilidad en los diferentes servicios de los cuales este opera: Desarrollar sus funciones de diversos lenguajes de programación , así mismo en diferentes bases de datos.

7¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
No pasa nada si se añade o modifica algún servicio debido a que cada uno está separado de los otros, se mejora el aislamiento de fallas

8¿Qué es un ambiente basado en contenedores?
Consiste en una aplicación de los microservicios, donde cada uno implementa un contenedor propio en sus diversas funciones correspondientes a distintas bases de datos y lenguajes de programación, los cuales son comunicados mediante el uso de una API.

9.Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes de algún lenguaje / tecnología en específico o no ?, ¿y por qué?
No, porque cada servicio es independiente

10¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
La comunicación entre estos servicios se realiza mediante protocolos como HTTP, AMQP y TCP. Los mensajes HTTP / REST y asíncronos son los protocolos más utilizados.

Una API de REST para servicios web usa el protocolo HTTP. Con los métodos HTTP (como GET, POST, PUT y DELETE), los clientes pueden acceder y manipular los recursos de la aplicación mediante un localizador uniforme de recursos (URL)

11¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si, porque cada uno opera de diferente manera, solo se encuentran comunicados unos con los otros.

12¿Cuáles son los principales desafíos de una arquitectura basada en microservicios?
como hacer para sincronizar los datos o para interconectar los servicios

13¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios? 
Con comprobaciones de estado
