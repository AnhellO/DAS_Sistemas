# Práctica 2

## Objetivos

* Expandir el conocimiento teórico sobre el tema de arquitectura de software
* Conocer casos de uso reales de las arquitecturas de software más utilizadas
* Revisar múltiples recursos para aprender sobre el uso de los diferentes patrones de arquitectura de software

## Especificaciones

### Parte 1

* Revisa el siguiente video [Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM) y contesta a las siguientes preguntas en otro nuevo archivo `.md` ([Markdown](https://www.markdowntutorial.com/)) por separado:
  * ¿Qué lenguaje de programación utiliza el equipo de Netflix?
    - Netflix utilizaba Java como lenguaje de programación, Linux como Host donde corría una configuración estándar de Apache y Tomcat, esta era una aplicación que el equipo de Netflix llamaban JavaWeb, esto estaba conectado directamente con una base de datos de Oracle utilizando JDBC que luego se interconectaba con otras bases de datos de Oracle usando enlaces de Bases de Datos.

  * ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
    - El código base para JavaWeb era monolítico en el sentido de que todos contribuían a un código base que se implementaba semanal o quincenalmente. El problema con es fue cuando se introdujo un cambio que causó un problema que era difícil de diagnosticar. La base de datos también era monolítica, incluso en un sentido más severo, era una pieza de Hardware que ejecutaba una gran base de datos y cuando está base de datos se caía, todo se caía.

  * ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
    - Desde una perspectiva de la ingeniería una de las principales desventajas que el equipo de Netflix tuvo que afrontar debido a esta arquitectura monolítca fue la falta de agilidad ya que todo estaba profundamente interconectado es decir tenían una arquitectura fuertemente acoplada.

  * ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
    - Martin Fowler

  * ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
    - Separation of concerns
      - Modularity, encapsulation
    - Scalability
      - Horizontally scaling
      - Workload partitioning
    - Virtualization & elasticity
      - Automated operations
      - On demand provisioning

  * ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
    - Utiliza como analogía el Sistema de Organos del cuerpo humano
      - Cada organo tiene un propósito
      - Los organos forman sistemas
      - Los sistemas forman un organismo

  * Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
    - La arquitectura de Netflix tiene una capa de proxy que está detrás del ELB llamado Zul que hace el enrutamiento dinámico.
    - Hay un nivel que era heredado llamado NCCP que admitía los dispositivos anteriores de Netflix más la capacidad de reproducción fundamental.
    - Netflix API, era la puerta de enlace de Netflix que hoy es la parte central de la arquitectura moderna de Netflix, llamando a todos los demás servicios para cumplir con las solicitudes de los clientes.

  * ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
    - Dependency
      - Intra-service requests      
      - Client libraries
      - Data Persistene
      - Infrastructure
    - Scale
      - Stateless services
      - Stateful services 
      - Hybrid services
    - Variance
    - Change

  * ¿Qué es el falló en cascada?
    - Cuando un servicio falla y con defensas inadecuadas contra ese servicio que falla ese error puede caer en cascada y eliminar todo nuestro servicio para nuestros miembros.

  * ¿Qué es Hystrix?
    - Para lidiar con el problema de un fallo en cascada Netflix creó Hystrix que tiene unas propiedades realmente agradables: tiene una forma estructurada para manejar los tiempos de espera, tiene este concepto de respaldo, por lo que si no se puede llamar al servicio B se puede devolver alguna respuesta estática o algo que le permita al cliente continuar usando el producto en lugar de simplemente obtener un error y el otro gran beneficio de Hystrix son los grupos de subprocesos aislados.

  * ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
    - Utiliza una analogía con un tema de Biología llamado Inoculación. La inoculación lo que hace es tomar una versión débil de un virus e inyectarlo en una persona para desarrollar los anticuerpos para defenderse contra la versión más mortal del virus, de la misma manera la inyección de fallas en producción logra lo mismo, y se creó para ajustarse al marco de prueba de inyección de fallas.

  * ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
    - Netflix manejo el problema de la persistencia al comenzar a pensar en las construcciones correctas y en el Teorema de CAP.
      - CAP Theorem
        - In the presence of a network partitioning, you must choose between consistency and availability
      - Netflix adoptó este concepto de consistencia eventual utilizando Cassandra.

  * ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
    - Netflix desarrolló una estrategía extra multirregional con tres regiones de AWS, de modo que si alguna de ellas falla por completo, aún pueden envíar todo el tráfico a las otras regiones supervivientes.

  * ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
    - Stateless services
    - Stateful services
    - Hybrid services

  * ¿De qué manera se describe un "_stateless service_" en el video?
    - What is a stateless service?
      - Not a cache or a database
      - Frequently accessed metadata
      - No instance affinity
      - Loss a node is a non-event

  * ¿Qué es Chaos Monkey?
    - Chaos Monkey es la disciplina de experimentar en un sistema distribuido (microservicio) para generar confianza en la capacidad del sistema para soportar condiciones turbulentas e inesperadas en la producción.

  * ¿Qué es un microservicio híbrido?
    - EVCache Writes: Es esencialmente un envoltorio alrededor de la memcache, que es similar a las SuitCaches, pero EVCache escribe datos múltiples veces en múltiples nodos.
    - EVCache Reads: Cuando leemos las lecturas son locales por que se desea esa eficiencia local pero la aplicación puede recurrir a la lectua a través de las zonas de disponibilidad que necesita para llegar a esos nodos.
    - El equipo de Netflix utiliza una combinación de ambos, un microservicio híbrido de EVCache Writes y EVCache Reads.

  * ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
    - Workload partitioning: La primera solución fue dejar de utilizar constantemente el mismo conjunto de sistemas.
    - Request-level caching: Utilizar el almacenamiento en caché de nivel de solicitud por lotes y en tiempo real para que no esté llamando repetidamente al mismo servicio una y otra vez como si fuera gratis.

  * ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
    - Python
    - Ruby on Rails
    - Node JS

  * ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
    - Productivity tooling
    - Insight & triage capabilities
    - Base image fragmentation
    - Node management
    - Library/platform duplication
    - Learning Curve - production expertise

  * ¿Qué es Spinnaker?
    - Es una plataforma global de administración de la nube, pero también un sistema de entrega automatizada

  * ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
    - Con el uso de la Ley de Conway
      - Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.
      - Any piece of software reflects the organizational structure that produced it.

  * ¿Qué es "_chaos engineering_" o "_ingeniería del caos_"?
    - La ingeniería del caos es el proceso de probar un sistema informático distribuido para garantizar que pueda soportar interrupciones inesperadas.

### Parte 2

* Ve alguno o todos los videos listados a continuación y contesta a las siguientes preguntas en otro nuevo archivo `.md` ([Markdown](https://www.markdowntutorial.com/)) por separado::
  * [_Robert C Martin - Clean Architecture and Design_](https://www.youtube.com/watch?v=Nsjsiz2A9mg)
  * [_Clean Architecture: La mejor forma de escalar y mantener tu código_](https://www.youtube.com/watch?v=y3MWfPDmVqo)
  * [_Arquitectura limpia!! o en inglés Clean Architecture!! En 5 minutos!! Fácil de entender 🚀💻🚀👨‍💻_](https://www.youtube.com/watch?v=hjBVBi18tUo)\
* Preguntas
  * ¿Qué busca solucionar esta arquitectura?
    - Las Arquitecturas Limpias también conocidas como las Arquitecturas por Capas nos ayudan a desacoplar la lógica de nuestro negocio de la infraestructura de la persistencia.
  * ¿Qué es la "_regla de dependencia_" o "_dependency rule_"?
    - La Clave de **Clean Architecture** es la **regla de dependencia**. Todas las dependencias tienen apuntar hacia dentro y no puede haber ningun círculo interior que apunte a uno exterior. Lo más importante es que todas las dependencias tienen que ir hacia el dominio y el dominio no debe apuntar a nada del exterior.
  * ¿Qué abarca la capa de _Entidades_ o _Entities_?
    - La lógica y datos de negocio empresarial se representa utilizando las **entidades**. Las entidades contienen los datos de negocio así como las reglas de negocio empresarial. Las entidades de una aplicación podrían ser compartidas entre diferentes aplicaciones dentro de una compañia.
  * ¿Qué abarca la capa de _Casos de Uso_ o _Use Cases_?
    - Los casos de uso representan la lógica de aplicación, que existe principalmente debido a la automatización de procesos mediante la aplicación y es inherente a cada aplicación.
  * ¿Qué abarca la capa de _Adaptadores_ o _Interface Adapters_?
    - Los adaptadores se van a encargar de transformar la información como se entiende y es representada en los detalles de implementación o frameworks, drivers a como la entiende el dominio.
  * ¿Qué abarca la capa de _Frameworks_ o _Frameworks and Drivers_?
    - En esta capa van todos los detalles, tanto para mostrar datos en la UI como para obtener los datos requeridos.
  * ¿Puede haber más de 4 capas? Complementa tu respuesta explicando tu razonamiento
    - Es posible modularizar aún más nuestro proyecto agregando más capas (como la capa de presentación, de datos, etc...), pero esto siempre dependerá del tipo de proyecto al que nos estemos enfrentando, aún si agregasemos más capas, todas las capas deberán de implementar la regla de dependencia.
  * ¿Qué son los "_boundaries_"?
    - Es una separación que definimos en nuestra arquitectura para definir dependencias y dividir componentes.

## Deadline

* `Viernes 3 de Junio a las 11:59pm`
