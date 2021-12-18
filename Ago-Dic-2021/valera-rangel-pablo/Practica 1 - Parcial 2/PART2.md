# Parte 2
**¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?**
- Se volvia lenta al minimo cambio, cada que se introducia un cambio venia con ello un problema lento y dificil de depurar

**¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?**
- Tenian que comprar mas hardware para soportar las solicitudes

**¿A qué autor cita el ponente cuando da el concepto de un microservicio?**
- Menciona a Martin Folwer

**¿Qué lenguaje de programación utiliza el equipo de Netflix?**
- Python asi como numpy, boto3 para analisis numericos, cambios en AWS

**¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?**
- Separación de preocupaciones Modularidad, encapsulación.
- Escalabilidad Escala horizontal Partición de la carga de trabajo. 
- Virtualización y elasticidad Operaciones automatizadas Aprovisionamiento bajo demanda.

**¿Qué analogía se utiliza para comparar los microservicios con la vida real?**
- Se hace la comparacion con los organos humanos, cada uno tiene su funcion que estos a su vez forman un sistema y estos a su vez forman el organismo

**Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces**
- Zuul: Hace enrutamiento dinamico
- NCCP: Admitía los dispositivos anteriores
- Api: Puerta de enlace

**¿Qué es el falló en cascada?**
- Cuando un servicio falla, cae todo el sistema

**¿Qué es Hystrix?**
- Se trata de una libreria de Netflix que aisla puntos de acceso a sistemas remotos, detiene fallos en cascada y permite mejorar la resilencia en sistemas complejos donde es inevitable la probabilidad de fallo

**¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?**
- La compara con una infeccion de parasitos

**¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?**
- Netflix eligió la disponibilidad a través de Cassandra, los sistemas finalmente son consistentes.

**¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?**
- Si un servidor AWS fallaba se enviaba el trafico a otro servidor

**¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?**
- Stateless services
- Stateful services
- Hybrid services

**¿De qué manera se describe un "stateless service" en el video?**
- Sin afinidad de instancias, los grupos de autoescalado no son fundamentales para los microservicios, no es una base de datos

**¿Qué es Chaos Monkey?**
- Es una herramienta que detiene instncuas y contenedores que estan ejecutandose en produccion de forma aleatoria

**¿Qué es un microservicio híbrido?**
- Un microservicio híbrido es un módulo único que realiza una tarea completa.

**¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?**
- Cuando se cayo todavia era reserva para el servicio y la base de datos.

**¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?**
- Docker
- Python
- NodeJS
- Rubi

**¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?**
- Herramientas de productividad 
- Capacidades de análisis y clasificación Fragmentación de imágenes base 
- Gestión de nodos 
- Duplicación de bibliotecas / plataformas 
- Curva de aprendizaje: experiencia en producción

**¿Qué es Spinnaker?**
- Es una plataforma que sirve para librera cambios de software con una alta velocidad y una gran confianza.

**¿Cómo manejo Netflix el problema de las arquitecturas híbridas?**
- Ley Conway

**¿Qué es "chaos engineering" o "ingeniería del caos"?**
- Es la disciplina de experimentar en un Sistema, con la finalidad de generar confianza en la capacidad del Sistema para soportar condiciones turbulentas en producción.