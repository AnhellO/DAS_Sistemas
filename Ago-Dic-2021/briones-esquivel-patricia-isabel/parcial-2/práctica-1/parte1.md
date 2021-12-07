# Parte 1
- ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
<br> Los microservicios son más fáciles de usar porque son más ágiles y flexibles.

- ¿En qué consiste el patrón de arquitectura monolítica?
<br> Incluye la creación de una aplicación autosuficiente que contiene todas las funciones necesarias requeridas para realizar sus tareas de diseño sin dependencias externas para complementar su funcionalidad.

- ¿Cuáles son las principales desventajas de una arquitectura monolítica?
<br> La funcionalidad y complejidad estructural del código, si los desarrolladores no comprenden completamente el código, caerán en serios problemas.

- ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
<br> Se tiene que agregar la nueva funcionalidad a todas las réplicas de la aplicación.

- ¿Qué sucede si falla una aplicación monolítica?
<br> Es probable que todo el sistema se bloquee.

- ¿En qué consiste el patrón de arquitectura basada en microservicios?
<br> En separar una aplicación en grupos pequeños, cada servicio se ejecuta en su propio proceso.

- ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
<br> Se van agregando mas componentes.

- ¿Qué es un ambiente basado en contenedores?
<br> Son los servicios implementados en contenedores, estos se comunican entre sí a través de API.

- Si utilizáramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
<br> No. Al ser aplicaciones grandes se utilizan varias tecnologías que se tratan como componentes o servicios individuales, para así, ser unidas después, lo que nos ofrece o permite trabajar con muchas tecnologías.

- ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
    - Por medio de los protocolos de la web HTTP/REST, AMQP y TCP.
    - Por medio de mensajes asíncronos.

- ¿Los microservicios pueden ser distribuidos? ¿Por qué?
<br> Sí, porque se organizan por diferentes servicios.

- ¿Cuáles son los principales desafíos de una arquitectura basada en microservicios?
<br> Contar con los suficientes recursos para poder trabajar de esta manera. Son complejos de probar, complejos de implementar y gestionar, complejos de comprender en su conjunto. 

- ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
<br> Esto depende de la gestión de nuestra red, también puedes escribir código, pero es muy difícil.