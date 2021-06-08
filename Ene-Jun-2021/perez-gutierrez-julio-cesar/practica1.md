#Practica 1,  2do Parcial
¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
Es mas rapido el desarrolo monolitica, pero presenta problemas si quieres migrarlo a otra plataforma es mejor para sistemas pequeños. 

¿En qué consiste el patrón de arquitectura monolítica?
consiste en tener todos sus servicios dentro de uno solo modulo.

¿Cuáles son las principales desventajas de una arquitectura monolítica?
Se trata de sistemas rígidos y difícilmente adaptables ante nuevas necesidades.
Su crecimiento es vertical, es decir, el aumento de su capacidad de proceso pasa por cambiar el servidor actual por uno mayor.

¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
si modificas algo  esto afecta a todo, o puedes dañar otra parte. 

¿Qué sucede si falla una aplicación monolítica?
si algo falla todo el sistema falla.

¿En qué consiste el patrón de arquitectura basada en microservicios?
Dividir los servicios que pueden depender por uno mismo o por otro, es decir
tener una aplicacion grande subdividida en pequeñas partes.

¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
se escala ese servicio y este no interrumpe a los demas. 

¿Qué es un ambiente basado en contenedores?
Es donde cada servicio tiene un contenedor para ejecutarse independiente y tener un mayor control sobre cada contenedor. 

Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
No dependen de un lenguaje especifico, las partes se pueden reutilizar, y bueno si pueden depender de la red y de la seguridad. 

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
Se comunican a traves de los protocolos de internet.

¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si, porque pueden ejecutarse en diferentes servidores

¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
Realizar los test de cada servicio ya que cada uno puede utilizar difentes tecnologias y debes asegurarte que cada parte funcione. 
Necesitas mas herraminetas y recursos para monitoriar las difentes partes.
El codigo se vuelve mas complejo para comunicar servidores.

¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
Se tiene otra copia en el servidor.