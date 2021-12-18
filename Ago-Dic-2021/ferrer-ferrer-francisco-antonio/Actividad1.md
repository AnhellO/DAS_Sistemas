##### Actividad 1

# ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
La monolìtica, un patron molotico se usa para aplicacion mas pequeñas y que estan iniciando por lo que es mas facil  desarrollar. 

# ¿En qué consiste el patrón de arquitectura monolítica?
Los componentes de una aplicacion del lado del servidor estan funcionando conjuntamente como una sola unidad.

# ¿Cuáles son las principales desventajas de una arquitectura monolítica?
Sera mas complicado administrar el contenido, debe ser desarrollada en un solo lenguaje de programacion, el momento de las actualizaciones .

# ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
Toda la aplicacion debe ser desplegada para que vuelva a funcionar, no se puede hacer un cambio en especifico.

# ¿Qué sucede si falla una aplicación monolítica?
Si un componente falla, todo fallara ya que esta unido.

# ¿En qué consiste el patrón de arquitectura basada en microservicios?
Es una manera de dividir una aplicacion del back-end en multiples partes que se comunican por separados, cada servicio puede comunicarse y cada una tiene una funcionalidad especifica, cada una puede evolucionar sin depender de los otros.

# ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
La plataforma creara mas contenedores para ayudar con la carga, y cuando la carga disminuye, esos contenedores desapareceran para que funcione con naturalidad.

# ¿Qué es un ambiente basado en contenedores?
Cada contenedor tiene su propio proposito, o su propia actividad y se comunican cuando sea necesario por APis

# Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
No se es dependiente de un lenguaje, ya que no se caracterisa por la tecnologia, si no por el servicio que brindan, los servicios pueden usar cualquier tecnologia.

# ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
Atravez de la internet.

# ¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si, se pueden deplegar y versionar independientemente, pero es dificil.

# ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
El saber dividir los servicios de la aplicacion, para que cada una de los servicios haga una funcionalidad especifica y el poder administrarla ya que es compleja.

# ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
Atraves de la replica de los multiples servicios.
