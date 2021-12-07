# Parte 2
- ¿Qué lenguaje de programación utiliza el equipo de Netflix?
<br> Python.

- ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
<br> Cada ves trataban de encontrar hardware mas grande para poder escalar verticalmente.

- ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
<br> Que no se podían detectar fallos fácilmente, eran difíciles de detectar, aunque extrajeran partes del código era muy difícil detectar estos fallos ya que se revisaban individualmente.

- ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
<br> Martin Fowler.

- ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
    - Separación de módulos.
    - Escalabilidad.
    - Virtualización y elasticidad.

- ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
<br> Un sistema de órganos, cada órgano tiene un propósito y cuando estos se unen forman un organismos.

- Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
    - NCCP: Admitía sus servidores anteriores y la capacidad de reproducción fundamental.

    - Zul: Hace el enrutamiento dinámico.

    - API de Netflix: Llama a los demás servicios a cumplir la solicitud de un cliente.

- ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
<br> Se proponen utilizar en aplicaciones en donde se ve un crecimiento muy rápido, donde de tener una arquitectura monolítica no de abasto para este crecimiento, y así poder escalar fácilmente la aplicación.

- ¿Qué es el falló en cascada?
<br> Es cuando un servicio falla, puede ser un fallo en cascada, y tirar todos los servicios, y si es que desplegaste este mal cambio en múltiples regiones si tiene una estrategia regional porque ahora realmente no tendrías lugar para recuperarlo, solo queda arreglarlo.

- ¿Qué es Hystrix?
<br> Esta es una biblioteca proporcionada por Netflix diseñada para aislar puntos de acceso a sistemas servicios y bibliotecas de terceros prevenir fallas en cascada y  mejorar la resiliencia en sistemas distribuidos complejos  donde la posibilidad de fallas es inevitable.

- ¿Qué analogía utiliza el ponente para comparar las librerías de cliente con la vida real?
<br> Una infección parasitaria ya que al igual que un parasito puede debilitarte pasa lo mismo en las librerías, provocan fallas dentro de la aplicación y debilitar tu servicio.

- ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
<br> Empezando a pensar sobre las construcciones correctas y con el CAP Theorem, básicamente establece que es posible optimizar para cualquier 2 de consistencia, disponibilidad y tolerancia de partición de red, pero no los tres.

- ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
<br> Aislar regiones, para que las interrupciones en los EE.UU. O Europa no se afecten entre sí.

- ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
    - Stateless services
    - Stateful services
    - Hybrid services
- ¿De qué manera se describe un "stateless service" en el video?
<br> Sin afinidad de instancias, los grupos de auto escalado no son fundamentales para los microservicios, no es una base de datos.

- ¿Qué es Chaos Monkey?
<br> Es una herramienta que detiene instancias y contenedores que están ejecutándose en producción de forma aleatoria.

- ¿Qué es un microservicio híbrido?
<br> La combinación de EVCache Writes y EVCache Reads.

- ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
<br> Usando tecnologías como  edie cash y easy cash. Además de partición de carga de trabajo, almacenamiento en caché a nivel de solicitud y con el respaldo de token seguro.

- ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
    - Docker
    - Python
    - Node.js
    - Rubi
- ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
<br> Intentar de replicar con contenedores de node.js y docker y la administración de nodos.

- ¿Qué es Spinnaker?
<br> Es una plataforma automatizada que está diseñada para integrar mejor las aplicaciones. 

- ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
<br> Eliminando las unidades centrales de la arquitectura, para así que estos nodos estén en el mismo nivel con los mismos beneficios y obligaciones

- ¿Qué es "chaos engineering" o "ingeniería del caos"?
<br> Es la disciplina de experimentar en un sistema, cuyo objetivo es generar confianza en la capacidad del sistema para resistir las caóticas condiciones de producción.