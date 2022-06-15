¿Qué lenguaje de programación utiliza el equipo de Netflix?
    Python 

¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
    Netflix creó programas grandes para ordenadores grandes,
    lo que se conoce como monolito : un programa que lo hacía todo.
    El problema está cuando creces tan rápido como Netflix;
    es muy difícil hacer que un monolito sea fiable
    y no lo consiguieron.

¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
    Netflix quería tener computación en la nube para poder prescindir
    de la creación de programas monolitos poco fiables, así como convertirse
    en un servicio global sin tener que construir sus propios
    centros de datos. Ninguna de estas capacidades estaba disponible
    en sus antiguos centros de datos y nunca lo llegaría a estar.

¿A qué autor cita el ponente cuando da el concepto de un microservicio?
    En palabra de Martin Fowler  los microservicios son una
    arquitectura con “puntos finales inteligentes y tuberías tontas”.

¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
    La separación de procesos, la escalabilidad y la virtualización

¿Qué analogía se utiliza para comparar los microservicios con la vida real?
    Los raganos y que cada uno de los organos tiene su funcion
    y se forma de un sistema que funciona en conjunto

Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
    Las API, NCCP y zuul

¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
    Dependencia, varianza y escala

¿Qué es el falló en cascada?
    Sí un servicio falla todos los servicios que están conectados entre si van a fallar.

¿Qué es Hystrix?
    El sistema que se encarga de manejar los tiempos y los reintentos.

¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
    Una piedra que se va atravesando y va provocando fallos que no se pueden
    ver a simple vista hasta que es mas grande el fallo. 

¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
    Con el Teorema de CAP    

¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
    Optaron por una estrategia multiregión para no depender de un solo lugar.

¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
    Stateless, stateful y hybrid services

¿De qué manera se describe un "stateless service" en el video?
    Sin cache no poder almacenar en la base de datos

¿Qué es Chaos Monkey?
    Que un nodo muera pero todo el sistema sigua bien

¿Qué es un microservicio híbrido?
    Que funciona con stateless y stateful services

¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
    Con almacenamiento del caché a nivel de solicitud y respaldo de token

¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
    El uso de nodos javascript, docker y phtyon

¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
    Gestion de nodos, fragancia de la imagen base y comocimiento de la curva de aprendizaje

¿Qué es Spinnaker?
    Una plataforma de entrega automatizada

¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
    Pensar en el cliente para sus comprender sus soluciones y mejorar su arquitectura

¿Qué es "chaos engineering" o "ingeniería del caos"?
    Pruebas que realiza un sistema para medir su capacidad en diferentes escenarios