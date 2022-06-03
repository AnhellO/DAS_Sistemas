# Parte 2
- ¿Qué lenguaje de programación utiliza el equipo de Netflix?
Python.

- ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Buscaban mejor hardware para escalar verticalmente.

- ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
Los fallos eran difíciles de detectar ya que había que revisar individualmente.

- ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler.

- ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
-- Separación de módulos.
-- Escalabilidad.
-- Virtualización y elasticidad.

- ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
Un sistema de órganos.

- Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
-- NCCP: Admitía sus servidores anteriores y la capacidad de reproducción fundamental.
-- Zul: Hace el enrutamiento dinámico.
-- API de Netflix: Llama a los demás servicios a cumplir la solicitud de un cliente.

- ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
Se proponen utilizar en aplicaciones con un crecimiento muy rápido y así facilitar el escalamiento de la aplicación.

- ¿Qué es el falló en cascada?
Es cuando un servicio falla y el fallo afecta otros servicios.

- ¿Qué es Hystrix?
Biblioteca proporcionada por Netflix cuya función es aislar puntos de acceso a sistemas servicios y bibliotecas de terceros para prevenir fallas en cascada y mejorar la resiliencia en sistemas distribuidos complejos donde los fallos son inevitables.

- ¿Qué analogía utiliza el ponente para comparar las librerías de cliente con la vida real?
Una infección parasitaria ya que puede debilitar las librerías, provocando fallas dentro de la aplicación y debilitando el servicio.

- ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Pensando sobre las construcciones correctas y el CAP Theorem, el cual nos dice que es posible optimizar 2 necesidades (consistencia, disponibilidad y tolerancia de partición de red), pero no las tres.

- ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
Aislar regiones, para que las interrupciones en distintos países no se afecten entre sí.

- ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
-- Stateless services
-- Stateful services
-- Hybrid services

- ¿De qué manera se describe un "stateless service" en el video?
Sin afinidad de instancias, los grupos de auto escalado no son fundamentales para los microservicios, no es una base de datos.

- ¿Qué es Chaos Monkey?
Herramienta que detiene instancias y contenedores que están ejecutándose en producción de forma aleatoria.

- ¿Qué es un microservicio híbrido?
La combinación de EVCache Writes y EVCache Reads.

- ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
Usando tecnologías como edie cash e easy cash. Además de partición de carga de trabajo, almacenamiento en caché a nivel de solicitud y con el respaldo de token seguro.

- ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
-- Docker
-- Python
-- Node.js
-- Rubi

- ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
La replicación con contenedores de node.js y docker y la administración de nodos.

- ¿Qué es Spinnaker?
Una plataforma automatizada diseñada para integrar mejor las aplicaciones.

- ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
Eliminando las unidades centrales de la arquitectura, para que estos nodos estén en el mismo nivel con los mismos beneficios y obligaciones

- ¿Qué es "chaos engineering" o "ingeniería del caos"?
Es la disciplina de experimentar en un sistema con el objetivo de generar confianza en la capacidad del sistema para resistir las caóticas condiciones de producción.