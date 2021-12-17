
# Parte-1

### ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
    La arquitectura monolitica porque a veces sin darnos cuenta la implementamos, porque solo
    es tenerlo todo en un contexto en contraste con los microservicios que tienes que dividir las tareas aparte de delegar equipos de programadores a estos microservicios siendo asi el costo de desarrollo mas bajo para la arquitectura monolitica

### ¿En qué consiste el patrón de arquitectura monolítica?
    su principal caracteristica es tener todo en el mismo contexto, donde  tiene toda la funcionalidad necesaria de la app en un solo lugar compartiendo los mismos recursos y memoria

### ¿Cuáles son las principales desventajas de una arquitectura monolítica?
    - No permite un agil desarrolo
    - Escabililidad (debes escalar el harware, meterle mas galleta a los musculos)
    - Mas recursos
    - Toda la app solo debe usar un lenguaje de programacion
    - Los componentes, no pueden ser reutilizados en otras aplicaciones
    - Dificil de testear

### ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
    Toda la aplicacion tiene que ser otra vez desplegada, no se puede hacer solo un
    cambio especifico si haces un pequeño cambio tendras que cambiar todo el programa nuevamente porque es dependiente

### ¿Qué sucede si falla una aplicación monolítica?
    si falla un compontente, perderemos todas las funcionalidades del sistema ya que todo esta unido y es dependiente.

### ¿En qué consiste el patrón de arquitectura basada en microservicios?
    son componentes distribuidos donde cada componente expone una funcionalidad dentro del sistema para que el cliente consuma esto, es muy comun que cada microservicio tenga su propia base de datos
    En particionar o dividir el programa en pequeñas responsabilidades que se comunican por separado

### ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
    lo que pasa es que la arquitectura funciona de mejor manera, ademas de que se le agregan mejores servicios a manera de se va escalando

### ¿Qué es un ambiente basado en contenedores?
    es una forma consistente y fiable, independiente del sistema operaivo o del ambiente de infrastructura, esto se logra agupando todo lo que se necesita para que se ejecute un servicio

### Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
    seriamos totalmente independientes de que elegir incluso en cada microservicio se podria usar otro lenguaje, tanto
    como cambiar de base de datos relacional como no relacional ya que la principal caracteristica de los microservicios no
    es su tecnologia si no la entrada y salida de informacion

### ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
    - Por medio de los protocolos de la web HTTP(REST)
    - Por medio de la API

### ¿Los microservicios pueden ser distribuidos? ¿Por qué?
    si, de hecho esa es su principal funcion ser divididos en responsabilidades para lograr que el codigo sea mas facil de refactorizar y añadir nuevas funcionalidades

### ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
    - El delegar y dividir el sistema
    - La seguridad web
    - La comunicacion de los microservicios depende de la calidad de la red
    - el testing se dificula en cuestion para hacer test no se pueden hacer pruebas de integracion ya   que debe se deben hacer mocks de los microservicios

### ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
    mediante la redundancia , evitando que falle de un solo punto, en otras palabras agregando mas puntos, colocandolos en diferentes ubicaciones fisicas para asi reducir la probabilidad de multiples puntos de falla


### Created by
- @EdsonAmaya7

