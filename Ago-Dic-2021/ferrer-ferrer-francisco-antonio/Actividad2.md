##### Actividad 2

# ¿Qué lenguaje de programación utiliza el equipo de Netflix?
java antes y ahora python
# ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Estaba conectada a otra base de datos. Tenian que hacer cambios semanales, lo que no era rentable y tenian que buscar hardware nuevo para poder escalar la aplicacion,.

# ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
Todo estaba tan interconectado que habia referencias a todos lados.

# ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler

# ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
·Separacion de intereses
·Escalabilidad
·virtualizacion y elasticidad

# ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
Un sistema de organos

# Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
tipo: Product
Suscriber: Se usa para crear el entorno de peliculas que se le recomendaran al usuario(cliente)

tipo: Platform
Routing: Enrutamiento

tipo: Persistence
Cache: Vive dentro del sistema

# ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
Las dependencias, escala, varianza y cambio. 

# ¿Qué es el falló en cascada?
Que una falla en un servicio se encadene a los servicios siguientes, llevando esta falla en cascada

# ¿Qué es Hystrix?
Un historial que ayuda a manejar los tiempos de espera y los reintentos, tiene mas herramientas para ayudar a controlar estos detalles.

# ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
Con los parasitos y un sistema.

# ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Con distintos servidores, tenerlos funcionando para apoyarse.

# ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
Desarrollo una estrategia multi-regional con 3 regiones, de modo que su alguna de ellas fallaba, aun podemos enviar todo el trafico a las otras 2.

# ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
Servicio sin estado, servicio con estado y despues el hibrido.

# ¿De qué manera se describe un "stateless service" en el video?
Se usa la mitosis(en biologia) para su explicacion.

# ¿Qué es Chaos Monkey?
Un software para hacer pruebas en casos peligrosos, para poner a prueba nuestra aplicacion.

# ¿Qué es un microservicio híbrido?
La combinacion del servicio con y sin estado.

# ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
Dejar de trabajar en el mismo conjunto de sistemas 

# ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
Python, ruby, node.js y docker.

# ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
Herramientas de productividad, gestion de nodos y en la curva de aprendisaje.

# ¿Qué es Spinnaker?
Es una plataforma de entrega continua de código abierto para liberar cambios de software con alta velocidad y confianza. 

# ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
Llamando al servicio repetidas veces en tiempo real.

# ¿Qué es "chaos engineering" o "ingeniería del caos"?
Es jugar o experimentar con nuestro sistema, haciendo situaciones peligrosas y ver la confiabilidad de nuestro sistema.