*¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
La monolitica, porque nos permite tener todo nuestro codigo y servicios sobre un mismo lugar por lo que el desarrollo se torna mas sencillo ya que se trata directamente a los diferentes servicios.

*¿En qué consiste el patrón de arquitectura monolítica?
Es la arquitectura en la que toda la funcionalidad esta dentro del mismo lugar, por ejemplo, podemos tener la interfaz de usuario junto a nuestros servicios que conectan con bases de datos, ademas de que la mayoria del codigo se programa bajo el mismo lenguaje y todo se concentra en un mismo servidor.

*¿Cuáles son las principales desventajas de una arquitectura monolítica?
El tener todo dentro de un mismo lugar, si se tiene un servicio de reportes, es necesario saber en donde se emplea este dentro del codigo de otros servicios ya que cualquier cambio puede ir a pegar a otros lados, a la vez que si se necesita un cambio en un solo servicio se requiere toda una iteracion para liberacion de este, otra desventaja es que un codigo a gran escala ya casi no es sostenible con esta arquitectura ya que implica muchos recursos al querer agrandar los servidores y mas capacidad de gente para darle mantenimiento.

*¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
Como lo habia mencionado antes, al querer agregar mas cosas a un servicio o monolito, se necesita saber en que otro lado podria afectar esto, ademas de que la carga sobre uno de estos puede implicar descuido de otras areas, ya que si se agrega funcionalidad por ejemplo a un servicio de pagos, es necesario hacer tambien cambios en otros lados, ya que dependen de este directamente.

*¿Qué sucede si falla una aplicación monolítica?
Gran parte de el sistema falla ya que todo esta conectado, por lo que si una parte de este falla, directamente nos falla en otros lados.

*¿En qué consiste el patrón de arquitectura basada en microservicios?
Es una arquitactura que busca la independencia de los diferentes servicios que ocupemos, conectandolos a traves de apis o otros medios, por lo que no es necesario tener el codigo en un solo lugar, y la implementacion de estos servicios incluso se puede manejar en diferentes lenguajes ya que se comunican de una forma diferente al no depender uno del otro, solo con mandar un llamado o subir un request que sera escuchado por otro servicio es suficiente para que nuestro sistema se conecte.

*¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
No sucede nada, solo se complementa mas el servicio, ya que operan de manera independiente, por loq ue solo creceria la funcionalidad de ese servicio sin afectar a otros o al sistema en si.

*¿Qué es un ambiente basado en contenedores?
Es un ambiente que nos permite crear todo un sitema preparado para desarrollar, esto gracias a la implementacion de sus imagenes por asi decirlo "prefabricadas" que nos permiten tener acceso rapido a programas que quizas sin contenedores nos tomaria mas tiempo implementar.

*Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
No necesariamente, ya que el ser servicios independientes estos no deben seguir un lenguaje especifico, podrian transmitir datos en base a formatos estandarizados, por ejemplo mandar un json desde un servicio usando js a uno con python, el servicio en python recibe el json y lo transforma en un objeto de python o directamente trabaja con el json, por lo que no es necesario usar un  solo lenguaje.

*¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
A traves de apis, de llamados y receptores en red que nos permiten saber cuando se necesita de un servicio.

*¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si, ya que cada servicio sirve para una cosa diferente, por lo que se pueden asignar de cualquier forma.

*¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
Saber cuando usarlos, ya que si se tiene un equipo pequeño y un sistema pequeño, seria mas complicado usar una arquitectura de microservicios ya que la administracion de estos se vuelve mayor,saber contener los diferentes errores que puedan llegar a surgir, sobre todo de red, ya que sin red no hay manera que nuestros servicios se comuniquen.

*¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
Con un buen balanceador, que nos permita mantener en orden la conexion entre nuestros servicios