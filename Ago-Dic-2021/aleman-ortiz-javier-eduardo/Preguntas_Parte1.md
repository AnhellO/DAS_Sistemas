# Parte 1

### ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
El patron de microservicios ya que al particionar nuestro domino conseguimos mas agilidad y eficiencia a la hora de llevar nuestra aplicacion desde desarrollo hasta produccion, una aplicacion de microservicios tiende a ser mas flexible, adaptable y multifuncional ofreciendo autonomia a cada uno de los equipos desarrolladores.

### ¿En qué consiste el patrón de arquitectura monolítica?
Consisten en agrupar todas las funciones en un solo gran codigo

### ¿Cuáles son las principales desventajas de una arquitectura monolítica?
Son mas dificiles de actualizar, Consumen mas memoria.

### ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
No podremos incrementar los recursos de la app sin que aumentemos al resto de aplicaciones ya que todas estan funcionando en conjunto, toda la app tiene que estar desarrollada en un solo lenguaje.

### ¿Qué sucede si falla una aplicación monolítica?
si ocurre una falla en un modulo es probable que todo el sistema se bloquee.

### ¿En qué consiste el patrón de arquitectura basada en microservicios?
En separar una aplicacion en grupos pequeños, cada servicio se ejecuta en su propio proceso.

### ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
Se van agregando mas componentes.

### Qué es un ambiente basado en contenedores?
Agrupar varios conenedores haciendo que se pueda simplificar y acelerar funciones repetitivas.

### Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
No, puedes desarrollar en cualquier lenguaje ya que se comunican atgraves de los protcolos de internet

### ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
El tipo más común es la comunicación de un único receptor con un protocolo sincrónico como HTTP/HTTPS al invocar a un servicio normal HTTP Web API.

### ¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si, ya que son partes separadas que se estan comunicando atraves de internet.

### ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
Es dificil organizar una gran cantidad de microservicios,tambien comprender, administrar y testearlas seria un reto.

### ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
Dependera de la administracion de nuestras redes, tambien se puede llegar a escribir codigo pero es muy dificil.