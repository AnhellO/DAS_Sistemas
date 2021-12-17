# Parte 2
### ¿Qué lenguaje de programación utiliza el equipo de Netflix?
JAVA.

### ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Cada ves trataban de encontrar hardware mas grande para poder escalar verticalmente.

### ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
La falta de agilidad porque todo estaba profundamente interconectado.

### ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler.

### ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
* Separacion de modulos.
* Escalabilidad.
* Virtualizacion y elasticidad.

### ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
Puede verse como los organos en el cuerpo humano.

### Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
* NCCP:Admitia sus servidores anteriores y la capacidad de reproduccion fundamental.

* Zul:Hace el enrutamiento dinamico.

* API de Netflix:Es la puerta de enlace API que llama a los demas servicios a cumplir la solicitud de un cliente.

### ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
Dependencia
Escala
Varianza
Cambio

### ¿Qué es el falló en cascada?
Cuando fallan las defensas de un servicio y cae y derriba todo el servicio para los miembros.

### ¿Qué es Hystrix?
Es una estructura que tiene algunas propiedades como manejar los tiempos de espera y grupos de subprocesos aisaldos.

### ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
con la inoculacion, un virus es inyectado en el cuerpo humano para que desarolle anticuerpos y pueda defenderse.

### ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Comenzando a pensar en las construcciones correctas y en el teorema del limite.

### ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
Desarrollo una estrategia multiregional con tres regiones de AWS de modo que si alguna caia aun podian enviar el trafico a las otras regiones

### ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
* Stateless services
* Stateful services
* Hybrid services

### ¿De qué manera se describe un "stateless service" en el video?
Con la mitosis

### ¿Qué es Chaos Monkey?
Fue la primera herramienta de caos, si algun nodo muere los demas siguen funcionando

### ¿Qué es un microservicio híbrido?
Es una combinacion de EVCache client y Service Client

### ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
Cuando se cayo todavia era reserva para el servicio y la base de datos.

### ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
* Dejar de trabajar en el mismo conjunto de sistemas.
* Almacenamiento en cache a nivel de solicitud por lotes.
* incrustar un token cifrado dentro de los dispositivos.

### ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
tratar de replicar con contenedores de nodejs y docker.
administracion de nodos.

### ¿Qué es Spinnaker?
Es una plataforma de gestion de la nube global y tambien un sistema de entrega automatizada.

### ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
Con la ley de conway

### ¿Qué es "chaos engineering" o "ingeniería del caos"?
Experimentar en un sistema