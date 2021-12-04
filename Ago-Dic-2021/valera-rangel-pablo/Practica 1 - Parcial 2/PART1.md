**¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?**

- A mi parecer yo opino que seria mejor la monolitica esto debido a que todos los modulos estan dentro de la maquina virtual, a comparacion de que se tengan que estar comunicando por red.

**¿En qué consiste el patrón de arquitectura monolítica?**

- Es aquella en la que todos las funciones del software se quedan acopladas dentro de un mismo programa.

**¿Cuáles son las principales desventajas de una arquitectura monolítica?**

- Se crean entornos rigidos que no pueden ser facilmente actualizables
- Agrega dificultad a los desarrolladores, dado que estos deben conocer todo el codigo de la aplicacion
- Altamente dependiente
- Lenguaje: Todo debe ser escrito en un solo lenguaje

**¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?**

- Que el desarrollador encargado antes debe conocer la estructura en la que esta formada la aplicacion y por ende tardara mas en implementarse

**¿Qué sucede si falla una aplicación monolítica?**

- Al momento en el que una funcion de una aplicacion monolitica falla, todo el monolito puede fallar

**¿En qué consiste el patrón de arquitectura basada en microservicios?**

- A diferencia de los monolitos esta se construye por partes, lo cual no son altamente dependientes de todas las funciones, cada funcion hace su propio servicio, tiene su propio contenedor y se comunican por separado, cada uno tiene una funcionalidad especifica

**¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?**

- Cuenta con la "Escalabilidad por módulos", lo que permite incrementar las capacidades de cómputo del módulo que mayor carga soporte o mayor demanda tenga

**¿Qué es un ambiente basado en contenedores?**

- Cada microservicio es un contenedor, esto es para evitar fallos masivos en toda la aplicacion, por ejemplo si falla el sistema de pagos, solo fallaria eso, y no toda la aplicacion en general

**Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?**

- No, esto debido a que cada microservicio puede ser utilizado con cualquier lenguaje que el equipo encargado desee.

**¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?**

- Podemos utilizar HTTP, AMQP o TCP, API REST.

**¿Los microservicios pueden ser distribuidos? ¿Por qué?**

- Si, esto es mas para aprovechar el tiempo entre los microservicios

**¿Cuáles son los principales desafios de una arquitectura basada en microservicios?**

- Desarrollar, testear, cada parte por separado
- La eficiencia depende de la administracion de redes
- Escribir codigo para comunicar servicores puede ser dificil
- Necesitas mas herramientas para monitorear todos los servicios.

**¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?**

- A traves de la replica de multiples de sus servicios.