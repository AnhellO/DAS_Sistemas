*¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
R= Monolitica, porque todo se hace dentro de la misma maquina virtual, toda comunicación pasa a memoria a traves de metodos, por el contrario en los microservicios partes los dominios y los aislas para comunicarse mediante la red. 

*¿En qué consiste el patrón de arquitectura monolítica?
R= En que la estructura del software mantiene todos sus aspectos funcionales acoplados y sujetos a un mismo programa.

*¿Cuáles son las principales desventajas de una arquitectura monolítica?
R= Considero que la limitada escalabilidad a la hora de manejar grandes cantidades de datos y el hecho de que para poder manipular el programa se debe entender por completo su funcionamiento ya que todo opera en el mismo sistema.

*¿*Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
R= Que tienes que modificar absolutamente todo el proyecto para que funcione. 

*¿Qué sucede si falla una aplicación monolítica?
R= Perderemos todas las funcionalidades del sistema ya que todo esta dentro del mismo proyecto.

*¿En qué consiste el patrón de arquitectura basada en microservicios?
R= En particionar o dividir el programa en pequeñas responsabilidades que se comunican por separado a traves de la red.

*¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
R= No resulta complicado para el proyecto ya que la arquitectura funciona de mejor manera, ademas de que se le agregan mejores servicios a manera que se va escalando.

*¿Qué es un ambiente basado en contenedores?
R= Es una forma consistente y fiable, independiente del sistema operaivo o del ambiente de infrastructura, esto se logra agupando todo lo que se necesita para que se ejecute un servicio.

*Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
R= Podemos elegir libremente que lenguaje usar, incluso s epodria usar un lenguje distinto para cada microservicio y el sistema funcionaría perfectamente ya que la principal caracteristica de los microservicios no es su tecnologia si no la entrada y salida de informacion.

*¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
R= Por medio de los protocolos de la web HTTP(REST) y por medio de la API.

*¿Los microservicios pueden ser distribuidos? ¿Por qué?
R= Si, de hecho esa es su principal funcion ser divididos en responsabilidades para lograr que el codigo sea mas facil de refactorizar y añadir nuevas funcionalidades.

*¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
    - El delegar y dividir el sistema.
    - La seguridad web.
    - No poder hacer pruebas de integracion ya que se deben hacer mocks de los microservicios.
    - La comunicacion de los microservicios depende de la calidad de la red.

*¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
R= Mediante la redundancia, agregando mas puntos y colocandolos en diferentes ubicaciones fisicas para asi reducir la probabilidad de multiples puntos de falla. 