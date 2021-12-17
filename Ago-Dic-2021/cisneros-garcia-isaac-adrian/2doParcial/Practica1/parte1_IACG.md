#Parte1 IsaacElCrack

**_¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?_**
- A mi punto de vista, yo creo que la de microservicios, ya que es posible lograr una mejor modernización de aplicaciones al implementar arquitecturas que te permitan ser adaptable frente a un entorno cambiante, como lo son las de microservicios. Por ejemplo, Amazon Lambda, que es parte de Amazon Web Services, es un servicio en la nube que te permite ejecutar códigos y arquitecturas de microservicios sin la necesidad de administrar servidores on premises. 

**_¿En qué consiste el patrón de arquitectura monolítica?_**
 El estilo arquitectónico monolítico consiste en crear una aplicación autosuficiente que contenga absolutamente toda la funcionalidad necesaria para realizar la tarea para la cual fue diseñada, sin contar con dependencias externas que complementen su funcionalidad.

**_¿Cuáles son las principales desventajas de una arquitectura monolítica?_**
Los problemas de este tipo de arquitectura, como la escalabilidad o la dificultad para los desarrolladores, ya que necesitan entender todo el código de la aplicación; Han hecho que este tipo de desarrollo de software deje de ser utilizado en muchos proyectos, aunque su sencillez y bajo coste hace que siga siendo interesante para ciertos proyectos con bajos requerimientos.

**_¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?_**
La funcionalidad del Codigo, y la complejidad de su estructura, ya que si el desarrollador no conoce por complrto el codigo, se metera en graves problemas.

**_¿Qué sucede si falla una aplicación monolítica?_**
Llega un punto en que parece que lo único que podemos hacer es escalar en hardware más maquinas hasta llegar al colapso.
La mejor opción es cambiar a microservicios:)

**_¿En qué consiste el patrón de arquitectura basada en microservicios?_**
Construir una aplicación de manera distributiva es el principal objetivo de una arquitectura basada en microservicios. Cada componente de la aplicación debe ser independiente de los otros, permitiendo que sean desplegados por sí mismos.
La comunicación o conexión entre los distintos módulos de la aplicación se realizan a través de API, lo que facilita que cada uno de estos módulos pueda contar con su propio grupo de desarrolladores, eliminando la necesidad de que cada desarrollador tenga que comprender todo el código de la aplicación o de otros módulos de la misma.
Cada uno de los servicios que componen una arquitectura basada en microservicios se puede desarrollar, implementar y escalar sin que afecte el funcionamiento del resto de servicios. Esta autonomía es una de las características principales de este tipo de arquitectura

**_¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?_**
Cuenta con la "Escalabilidad por módulos", lo que permite incrementar las capacidades de cómputo del módulo que mayor carga soporte o mayor demanda tenga (al poderse instalar en distintos servidores los módulos de la aplicación).

**_¿Qué es un ambiente basado en contenedores?_**
Los contenedores contienen un microservicio o una aplicación y todo lo que necesita para ejecutarse. Lo que está dentro de un contenedor se conserva en lo que llamamos imagen: un archivo basado en un código que incluye todas las bibliotecas y las dependencias.

**_Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?_**
No, ya que al trabajar por módulos, permite desarrollar utilizando múltiples lenguajes de programación, lo que aporta ventajas como velocidad, rendimiento, reducción de costes, elección de distintas herramientas de desarrollo, etc.

**_¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?_**
En una arquitectura de microservicios, los servicios se ejecutan en varios servidores. La comunicación entre estos servicios se produce a través de protocolos como HTTP, AMQP y TCP. Los protocolos más utilizados son HTTP/REST y los mensajes asíncronos.

**_¿Los microservicios pueden ser distribuidos? ¿Por qué?_**
Si, y a través del desarrollo distribuido, los microservicios potencian a los equipos y las rutinas. También puede desarrollar múltiples microservicios de forma simultánea. Gracias a ello, más desarrolladores pueden trabajar en la misma aplicación simultáneamente para reducir el tiempo invertido en el desarrollo.

**_¿Cuáles son los principales desafios de una arquitectura basada en microservicios?_**
- Administrar microservicios:
Administrar microservicios puede ser un desafío importante, especialmente a medida que aumenta el número de éstos. Si acaba de comenzar con los microservicios y solo tiene un puñado de ellos, esto aún no es un problema en su organización.
- Cambio Cultural y Organizacional:
La implementación de microservicios no ocurre de la noche a la mañana. No puede decidir introducir microservicios y esperar que todas sus formas antiguas de hacer las cosas se adapten por sí mismas. Un cambio a microservicios requiere un cambio cultural, de procesos y organizacional, porque es un cambio de mentalidad y de la forma en que las personas trabajan.
- Diagnóstico y monitoreo de microservicios
Cuando se introduce un enfoque de microservicios, pueden ser necesarias nuevas formas de supervisión y solución de problemas para rastrear y resolver problemas imprevistos, tanto en la producción o durante el proceso de desarrollo.
- Tiempo de implementación y recursos para microservicios
El tiempo de implementación y la búsqueda de los recursos adecuados para el desarrollo de microservicios es el último de los cuatro desafíos principales identificados por los participantes en la encuesta de Red Hat. Este desafío probablemente tiene más que ver con las personas que implementan microservicios que con la tecnología misma.

**_¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?_**
Los microservicios permiten que cada servicio se escale de forma independiente para satisfacer la demanda de la característica de la aplicación que respalda. Esto permite a los equipos adecuarse a las necesidades de la infraestructura, medir con precisión el costo de una característica y mantener la disponibilidad si un servicio experimenta un aumento en la demanda.