#Parte2 IsaacElCrack

**_¿Qué lenguaje de programación utiliza el equipo de Netflix?_**
 El servicio que lidia con ello también está basado en Python, y utiliza Numpy, Scipy, Boto3 o RQ** para ejecutar análisis numéricos, para hacer cambios en su infraestrucura AWS o para ejecutar cargas de trabajo asíncronas.

**_¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?_**
Era de arquitetura monolítica, lo que provoco que al mas minimo cambio, la base de datos se volviera lenta. Todos contribuían a una única base de código que se publicaba una vez a la semana, cuando el cambio introducía un problema que era difícil y lento de depurar.

**_¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?_**
Al ser monolítico, el equipo de netflix, necesitaba más y más hardware para seguir adelante cada verano.

**_¿A qué autor cita el ponente cuando da el concepto de un microservicio?**_
Martin Fowler.

**_¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?_**
- Separación de preocupaciones Modularidad, encapsulación.
- Escalabilidad Escala horizontal Partición de la carga de trabajo. 
- Virtualización y elasticidad Operaciones automatizadas Aprovisionamiento bajo demanda.

**_¿Qué analogía se utiliza para comparar los microservicios con la vida real?**_ 
Se puede pensar en los microservicios como órganos, cada órgano tiene su propósito, los organos forman sistemas, los sistemas forman un organismo.

**_Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces**_
- Zuul: Hace enrutamiento dinamico
- NCCP: Admitía los dispositivos anteriores
- Api: Puerta de enlace

**_¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?**_
Es posible que deba proporcionar alguna orquestación entre el cliente y el cliente almacenado en caché, por lo que es posible que deba proporcionar realmente una biblioteca cliente que irá a la caché primero, y si falla, irá al cliente que llegará a la capa de microservicio y persistencia. y luego rellenar el caché para la próxima llamada. Todo esto tendrá que estar incrustado dentro de la aplicación cliente que quiere utilizar el. Desde la aplicación consumidora, la biblioteca cliente, que incluye el caché del cliente del servicio, el cliente del servicio, el servicio y la base de datos es el microservicio. No es una simple cuestión de estado.

**_¿Qué es el falló en cascada?**_
Un servicio falla sin defensas, puede caer en cascada y derribar toda su red.

**_¿Qué es Hystrix?**_
Se trata de una librería ofrecida por Netflix diseñada para aislar puntos de acceso a sistemas remotos, servicios y librerías de terceros, deteniendo fallos en cascada y permitiendo mejorar la resiliencia en sistemas complejos distribuidos donde la probabilidad de fallo es inevitable.

**_¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?**_
Como una infección de parasitos, que chupan tu sangre e infestará tus intestinos.

**_¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?_** 
Con el teorema del límite
En presencia de una partición de red, debe elegir entre consistencia y disponibilidad. Netflix eligió la disponibilidad a través de Cassandra, los sistemas finalmente son consistentes.

**_¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?**_
Una estrategía multiregional de AWS, de modo que si alguna fallaba, se enviaba el tráfico a otro servidor.

**_¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?**_
- Stateless services
- Stateful services
- Hybrid services

**_¿De qué manera se describe un "stateless service" en el video?**_
- No es un caché o una base de datos
- Metadatos de acceso frecuente
- Sin afinidad de instancias
- La pérdida de un nodo no es un evento, puede reemplazar un nodo sin costo
- Los grupos de autoescalado son fundamentales para los microservicios, ventajas

**_¿Qué es Chaos Monkey?**_
Es una herramienta software que de forma aleatoria detiene instancias y contenedores que están ejecutándose en el entorno de producción. El objetivo es exponer a los sistemas a fallos para ayudar a los ingenieros a proveer servicios que sean capaces de reaccionar a caídas y otros problemas inesperados.

**_¿Qué es un microservicio híbrido?**_
Es fácil dar por sentado EVCache
- 30 millones de solicitudes / seg
- 2 billones de solicitudes por día en todo el mundo
- Cientos de miles de millones de objetos
- Decenas de miles de instancias Memcached
- Su consistencia escala de forma lineal, sin importar la carga. 
- Milisegundos de latencia por solicitudes

**_¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?**_
- Partición de la carga de trabajo 
- Almacenamiento en caché a nivel de solicitud
- Respaldo de token seguro 
- Caos bajo carga

**_¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?**_
- Docker
- Python
- node js
- Rubi

**_¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?**_
Herramientas de productividad 
Capacidades de análisis y clasificación Fragmentación de imágenes base 
Gestión de nodos 
Duplicación de bibliotecas / plataformas 
Curva de aprendizaje: experiencia en producción
**_¿Qué es Spinnaker?**_
es una plataforma de entrega continua de código abierto para liberar cambios de software con alta velocidad y confianza. A través de una poderosa capa de abstracción, Spinnaker proporciona herramientas nos permiten llevar el código de la aplicación desde el “commit” hasta producción.

**_¿Cómo manejo Netflix el problema de las arquitecturas híbridas?**_
Evoluciono, pasó de unas bases de datos anticuadas a unas más simples y con gran potencial. "Conway's Law"

**_¿Qué es "chaos engineering" o "ingeniería del caos"?**_
Es la disciplina de experimentar en un Sistema, con la finalidad de generar confianza en la capacidad del Sistema para soportar condiciones turbulentas en producción.