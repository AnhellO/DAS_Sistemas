# Parte 1
___
- ¿Qué lenguaje de programación utiliza el equipo de Netflix?
    Al principio mencionó Java Web.
- ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
    Estaba interconectada con otra base de datos usando DB links. Cuando tenian un peak, tenian que escalar verticalmente
- ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
    El código base, todos contribuian hacia él y cuando se introducia un cambio que causara algún problema, era dificil de diagnosticar.
    En general la arquitectura, todo estaba profundamente interconectado.
- ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
    Martin Fowler
- ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
    - Separación de preocupaciones.
    - Escalabilidad.
    - Virtualización y elasticidad.
- ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
    Los sistemas dentro de nuestra anatomía.
- Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
    - Zul : hacía enrutamiento dinámico.
    - NCCP : ayudaba con la capacidad de reproducción.
    - API : sigue siendo parte de la arquitectura moderna, llama a otros microservicios.
- ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
    - Dependencia.
    - Escala.
    - Varianza
    - Cambio.
- ¿Qué es el falló en cascada?
    - Cuando la falla de un servicio lleva a tener fallas a otros.
- ¿Qué es Hystrix?
    - Es un tipo de arquitectura que ayuda a manejar los imprevistos que pueden surguir al momento de que se ejecute alguna aplicación.
- ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
    - La infestación parasitaria.
- ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
    - Eligió la disponibilidad a través de cassandra.
- ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
    - Desarrollo una estrategia multi-region, con tres regions AWS.
- ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
    - Servivios:
        -   Stateless
        -   Stateful
        -   Hybrid
- ¿De qué manera se describe un "_stateless service_" en el video?
    - No es una caché o una base de datos.
    - Metadata de acceso frecuente.
    - Sin afinidad de instancia.
    - La pérdida de un nodo  es un non-event.
- ¿Qué es Chaos Monkey?
    - Hace que aleatoriamente un nodo se "caiga".
- ¿Qué es un microservicio híbrido?
    - Sucede de la combinación de dos tipos de approaches (en el video mencioni EV Writes & EV Reads).
- ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
    - Particionamiento de carga de trabajo.
    - Almacenamiento en caché a nivel de solicitud.
    - Respaldo de token seguro
    - Caos bajo carga.
- ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
    - Stash
    - Nebula/Gradle
    - BaseAMI/Ubuntu
    - Jenkins
    - Spinnaker
    - Runtime platform
- ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
    - Herramientas de productividad 
    - Capacidades de información y clasificación
    - Gestión de nodos
- ¿Qué es Spinnaker?
    - Plataforma de delivery que fue creada para reemplazar a asgaard. Es una gestión global de la nube.
- ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
    - Utilizando la Ley Conway.
- ¿Qué es "_chaos engineering_" o "_ingeniería del caos_"?
    - Es un tipo de disciplina en el cual se experimenta a traves de un sistema para checar que tan confiable es en caso de que surjan problemas en durante su funcionamiento