#####       PARTE 1      ######
##### ERICK DIAZ DELABRA ######

# ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
.- Yo creo que la de microservicios debido a la agilidad y que podemos programar por partes todo, y pues creo yo que es mas facil a la hora de organizarse para una apliacion, puede ser una desventaja ya que cada microservicio debe tener su propia base de datos pero yo creo que si alguien le sabe pues le sabe y no será problema.
SS
# ¿En qué consiste el patrón de arquitectura monolítica?
.- Consiste en que todas las partes de una aplicacion funcionen en conjunto y  para lo que fueron diseñadas. 

# ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
.- Que por cada funcionalidad nueva agregada tenemos que corregir y modificar la aplicacion para que quede bien coplado el codigo o la nueva funcionalidad, y en caso de que no funcione pues estariamos dañando toda la app.

# ¿Qué sucede si falla una aplicación monolítica?
Falla toda la aplicacion por completo y ya no serviria su ejecución. Igualmente buscar el error seria mas complicado.

# ¿En qué consiste el patrón de arquitectura basada en microservicios?
Que todas las partes de la aplicacion esten separadas y tengan sus propias bases de datos, al final todas las partes van a estar conectadas por red y asi funciona toda la aplicacion.

# ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
Nada, solo deberiamos de aumentar la capacidad dependiendo los requerimentos de la aplicacion. Usar micro servicios nos permite añadir los recursos necesarios solo a la parte en la que o necesitamos.

# ¿Qué es un ambiente basado en contenedores?
Un modelo de una aplicacion en la que cada parte trabaja por separado. Estos contienen los microservicios.

# Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
No, cada parte o cada microservicio puede trabajar con su propio lenguaje o con su propia tecnologia siempre y cuando pues nos sirva a nosotros para lo que estamos buscando. Por ejemplo podemos tener dos micro servicios y uno puede funcionar con MSQL y el otro con MySQL. Uno puede estar en Python y el otro en java, funcionan si es que asi lo requerimos :D.

# ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
Se pueden comunicar por red (Protocolos web HTTP, AMQP y TCP), contenedores y apis.

# ¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si pueden, ya que pues en eso se basan, en no depender de los demas para que sea mas ágil su programacion y puedan funcionar de manera distribuida y hasta con otras aplicaciones..

# ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
Los test son independientes por cada uno de os microservicios que tengamos.
Cada uno debe tener sus propios recursos.
La administracion, ya que mientras mas tengamos pues mas complicado se volverá.
Aprender a usar cada uno de ellos, debido a que como ya dije arriba pues pueden tener diferentes lenguajes o bases de datos.
Tiempo de implementacion, debido a que tenemos que saber muy bien que es exactamente lo que requiere cada microservicio.

# ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
Mmmmm, pues yo creo que simplemente dando el mantenimiento y actualizaciones correctas. 
Haciendo test continuamente o tests automaticos para ver que anda falle.
Dandole un poquito mas que los recursos necesarios a cada microservicio, mejeor que sobre a que falte je.

0