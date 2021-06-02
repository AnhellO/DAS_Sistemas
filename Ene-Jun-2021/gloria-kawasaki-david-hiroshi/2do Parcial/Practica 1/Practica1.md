#PARTE 1

    ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
        El patrón de Microservicios ya que se seccionan y aíslan funcionalidades pudiendose concentrar en esos pequeños servicios. Además de si aparece un error o fallo, se puede
        encontrar y corregir más fácilmente
    ¿En qué consiste el patrón de arquitectura monolítica?
        Se contruyen los servicios de forma que se puedan comunicar entre sí.
    ¿Cuáles son las principales desventajas de una arquitectura monolítica?
        Cuando el software crece en código y funcionalidad se vuelve más complicado el
        mantenimiento y la corrección de errores, además de que necesitará más recursos.
    ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
        Puede que las funciones estén construídas de tal forma que la modificación del
        código puede causar fallos en la funcionalidad.
    ¿Qué sucede si falla una aplicación monolítica?
        Toda la aplicación falla
    ¿En qué consiste el patrón de arquitectura basada en microservicios?
        Dividir atómicamente los servicios y aislarlos entre sí
    ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
        El servicio en cuestión puede llegar a saturarse, para evitarse lo que se hace es agregar otro nodo del microservicio delante de un balanceador de carga.
    ¿Qué es un ambiente basado en contenedores?
        Es una aplicación del patrón de microservicios
    Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún 
    lenguaje/tecnología en específico o no?, ¿y por qué?
        No, ya que los microservicios se comunicarían entre sí mediante la red y no de forma directa por lo que los módulos podrían ser construídos en otros lenguajes
    ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
        mediante servidores o la red
    ¿Los microservicios pueden ser distribuidos? ¿Por qué?
        Si, ya que pueden ejecutarse en otros servidores
    ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
        La comunicación entre estos mismos microservicios ya que la velocidad y seguridad con que lo hacen dependerá completamente de la velocidad y seguridad de la conección. Además del tiempo que se toma a la hora testear y liberar cada microservicio.
    ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
        A través de la réplica de los microservicios.

#PARTE 2

    ¿Qué lenguaje de programación utiliza el equipo de Netflix?
        Java Web
    ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
        Era una única pieza de hardware que ejecutaba una única base de datos, si esta caía, todo lo demás caía.
    ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
        Tardaban mucho en probar y efectuar cambios ya que tomaba días el extraer un fragmento en específico de código, probarlo y volverlo a meter en caso de encontrar la falla.
    ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
        Martin Fowler
    ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
        - Separación y encapsulamiento de procesos
        - Escalabilidad
        - Virtualización y elasticidad
    ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
        Compara los microservicios con órganos ya que estos son sistemas que en conjunto llevan a la existencia de un organismo más grande.
    Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
        - Zuul: una capa proxy para el enrutamiento dinámico.
        - NCCP: soporta dispositivos más nuevos.
        - API: es el gateway sirve para completar los request de los usuarios.
    ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
        - Dependencia
        - Escala
        - Varianza
        - cambios
    ¿Qué es el falló en cascada?
        Es cuando un servicio falla y los demás servicios no están debidamente protegidos contra estos escenarios provocando que otros servicios fallen, tumbando todo el servicio hacia los usuarios
    ¿Qué es Hystrix?
        es una estructura para evitar los fallos en cascada
    ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
        Comparó las librerías de cliente con un parásito ya que comparten ciertas similitudes como lo es el hecho de que uno solo no hace nada, pero muchos pueden provocar sintomas severos.
    ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
        Con el teorema de CAP el cual se podría decir que dicta que en la presencia de una partición de red, se debe de escoger entre consistencia y disponibilidad
    ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
        una estrategia multiregión
    ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
        - stateless
        - stateful
        - hibrido
    ¿De qué manera se describe un "stateless service" en el video?
        No guarda en bases de datos o en cache, tiene metadata que se frecuenta, no tiene afinidad de instancias, y si un nodo se pierde no es un evento.
    ¿Qué es Chaos Monkey?
        Indica cuando un nodo muere sin que el sistema deje de funcionar
    ¿Qué es un microservicio híbrido?
        Una combinación entre un microservicio stateful y uno stateless. 
    ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
        - partición de carga de trabajo
        - caching a nivel de solicitudes
        - Token de seguridad
    ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
        docker
    ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
        - herramientas de productividad
        - Fragmentación de la imagen base
        - manejo de Node
    ¿Qué es Spinnaker?
        una plataforma de entrega para realizar cambios al software a altra velocidad
    ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
        Pasar de preocuparse por las soluciones y preocuparse sobre la organización
    ¿Qué es "chaos engineering" o "ingeniería del caos"?
        Disciplina que permite experimentar en un sistema con la finalidad de generar confianza en la capacidad para soportar condiciones caoticas del sistema.