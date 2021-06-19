¿Qué lenguaje de programación utiliza el equipo de Netflix?
-Java.

¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
-Que si se cae, se cae todo.

¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
-Que si un problema sucedia, era dificil saber que era, por culpa de ser monolítica.

¿A qué autor cita el ponente cuando da el concepto de un microservicio?
-Martin Fowler.

¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
-Separacion de preocupaciones.
Escalabilidad.
Virtualizacion y elasticidad.

¿Qué analogía se utiliza para comparar los microservicios con la vida real?
-Nuestros organos como un conjunto de microservicios.

Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
-Subscriber: Encontrar la informacion del usuario.
Recommendation:Da la informacion necesaria para hacer una lista de series y peliculas que le gustarian al usuario.
Routing: para que los microservicios se encuentren entre ellos mismos.

¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
-Dependencia, escala,varianza y cambio.

¿Qué es el falló en cascada?
-Nos dice que cuando algo falla puede hacer que todo el sistema caiga 

¿Qué es Hystrix?
-Es una libreria que usa Netflix, para que el problema de cascada no suceda,ayuda a que el cliente pueda seguir usando el servicio y no de errores

¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
-Una infeccion de parasitos.

¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
-Usaron un sistema llamado cassandra que podia manejar diversos nodos con facilidad.

¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
-Crear un sistema multiregion, para que si uno fallara completamente, pudiera seguir el servicio sin problemas, mientras se resolvia el problema

¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
-Stateless services
Staleful services
Hybrid services

¿De qué manera se describe un "stateless service" en el video?
-Con la mitosis

¿Qué es Chaos Monkey?
-Confirma que si un nodo muere el sistema sigue funcionando, osea que pone al sistema en una situacion dificil para testear que siga en funcionamiento

¿Qué es un microservicio híbrido?
-Es la combinacion de un staless services y un Staleful services

¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
-Con Workload partitioning, Request-level caching, secure token fallback y chaos underload

¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
-Node, docker, ruby, python,etc.

¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
-Productivity tooling, base image fragmentation, done management.

¿Qué es Spinnaker?
-Es una plataforma de entrega, que maneja la nube y obviamente tiene un sistema de entrega y entrega automatica.

¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
-Con conway's law

¿Qué es "chaos engineering" o "ingeniería del caos"?
-Es poner al sistema en pruebas especificas de disponibilidad, rendimiento y seguridad, para que asi obtener un seguridad
de la capacidad y confianza del sistema en recuperarse, es decir, construir estructuras que soporten condiciones extremas.