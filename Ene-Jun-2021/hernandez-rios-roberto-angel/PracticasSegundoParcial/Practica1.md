Parte 1

¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
    -Los microservicios son más fáciles de trabajar que las aplicaciones monolíticas,
     porque permiten introducir nuevos marcos, fuentes de datos y demás recursos
     dificultades.

¿En que consiste el patrón de arquitectura monolítica?
    -Que los componentes de una aplicación por parte del servidor
     están funcionando conjuntamente como una sola unidad.

¿Cuáles son las principales desventajas de una arquitectura monolítica?
    -la dificultad para los desarrolladores ya que solamente está escrito en 
     un solo lenguaje 
    -Otra desventaja es al momento de realizar un nuevo despliegue, se necesita
     lanzar todo el sistema de nuevo para que las demás aplicaciones no se vean 
     afectadas
    -Solo se crean para una aplicación específica por lo que no se puede reutilizar.

¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
    -El problema surge cuando se quiere incrementar la funcionalidad y resulta más 
     díficil de administrar ya que se tiene que replicar el código en los demás 
     servidores y por lo tanto estariamos afectando a las demás aplicaciones.

¿Qué sucede si falla una aplicación monolítica?
    -Fallan las demás aplicaciones ya que están unidas

¿En qué consiste en patrón de arquitectura basada en microservicios?
    -Se caracteriza por las aplicaciones por parte del back end están divididas
     por múltiples partes o servicios donde cada uno es un proceso independiente
     con una funcionalidad en particular.

¿Qué sucede si aumenta la carga la carga en un servicio de la arquitectura basada en microservicios?
    -Se comineza a subdividir una aplicación y se requiere más complejidad y más administración por parte
     de los desarrolladores asi como más disponibilidad de recursos.

¿Qué es un ambiente basado en contenedores?
    -Es como una estructura en donde hay varias particiones y estas a su vez se concentan 
     a través de la internet y logra mantenter una mejor administración por parte de los 
     desarrolladores.

Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
    -No se necesitaría depender de un lenguaje o tecnología, porque como cada servicio o proceso se crea a partir del 
     criterio de cada desarrollador no se crea esa dependencia por el concepto de procesos separados.

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
    -Compartiendo una misma base de datos y con comunicación por base en los protocolos de internet.

¿Los microservicios pueden ser distribuidos? ¿Por qué?
    -Porque son muy faciles de reutilizar en distintas aplicaciones por lo mismo que están creadas por
     distintos lenguajes o tecnologías.

¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
    -Es la parte de mantenerlos ya que funcionan muy bien con una buena cantidad de desarrolladores
     a su vez crearlos es un poco más complicado porque es construir cada uno de los servicios.

¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
    -Respectivamente con la disponibilidad de desarrolladores con los que se cuenta, asumiendo las
     peticiones o el incremento de trabajo.



Parte 2


¿Qué lenguaje de programación utiliza el equipo de Netflix?
    -Java

¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
    -Se introdujo un cambio dónde el albúm fue difícil de diagnosticar y a través de distintas
     soluciones se requirío tiempo, se notó la complejidad en las llamadas directas en la 
     base de datos.

¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
    -Notar la dificulatd que se requería para poder generar cambios, que consumía mucho tiempo
     y que se necesitaron soluciones complejas.

¿A qué autor cita el ponente cuando da el concepto de un microservicio?
    -Martin Fowler

¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
    -Fomenta la modularidad, la capacidad de encapsular sus estructuras de datos, algo 
     para lo que no se tenga que lidiar con toda esa coordinación.
    -Escalabilidad particiona la carga de trabajo ya que es un sistema distribuido
    -Virtualización y Elasticidad se requiere para automatizar sus operaciones.

¿Qué analogía se utiliza para comparar los microservicios con la vida real?
    -Al cuerpo humano y la biología como órganos en un sistema de órganos.

Describe al menos 3 diferentes tipos de servicios que Netflix tenía en si arquitectura en aquel entonces
    -Capa de proxy que está detrás del ELB llamada Zul que hace el enrutamiento dinámico
    -El NCCP que admite los dispositivos más la capacidad de reproducción
    -API de Netflix que llama a los demás servicios para cumplir con las solicitudes.

¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
    -Dependencia
    -Escala
    -Variación
    -Cambio

¿Qué es el fallo en cascada?
    -Es un escenario en el que tienes un servicio que falla con defensas inadecuadas que 
     puede producir una cascada de errores y derribar todo su servicio para sus miembros.

¿Qué es Hystrix?
    -Es una historia con grupos de subprocesos aislados que tiene una forma estructurada para manejar 
     los tiempos de espera, un concepto de respaldo.

¿Qué analogía utiliza el ponente para comparar las librerías de cliente con la vida real?
    -A una infección parasitaria ya que lo muestra como una infestación al sistema.

¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
    -Pensando sobre las construcciones correctas y sobre el teorema del límite, se eligió 
     el concepto de consistencia eventual.

¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
    -Netflix desarrolló un estreptococo con una estrategia multiregional con tres regiones 
     de AWS de modo que si alguna de esas fallaba, todavía se podía llevar todo el tráfico a los
     otros sobrevivientes.

¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
    -Servicios apátridas
    -Servicios estatales
    -Servicios Híbridos

¿De qué manera se describe un "stateless service" en el video?
    -No es una base de datos que no está almacenando masivamente, datos a los que se ha
     accedido con frecuencia, existe una naturaleza no volátil de esa configuración.

¿Qué es Chaos Monkey?
    -Es una herramienta de caos que confirma que cuando un nodo muere, todo sigue funcionando.

¿Qué es un microservicio híbrido?
    -Este microservicio almacena cientos de miles de millones de objetos en decenas de miles
     de memcache y escala consistentemente en un lineal de manera que las solicitudes se 
     pueden devolver en cuestión de milisegundos.

¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
    -Se detuvo martillando en el mismo conjunto de sistemas para lotes y en tiempo real,
     se solicitó almacenamiento en caché de nivel para que no esté llamando 
     repetidamente al mismo servicio y hay una probabilidad de instalar un token
     seguro dentro de los dispositivos.

¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
     -La carretera pavimentada una especie de integración para que los desarrolladores puedan ser
      más agiles
     -NodeJS
     -python
     -Ruby
     -Docker

¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
    -Herramientas de productividad
    -Capacidades de conocimiento y triaje
    -fragmentación de la imagen base

¿Qué es Spinnaker?
    -Es una gestión global de la nube para una entrega automatizada 

¿Cómo manejó Netflix el problema de las arquitecturas híbridas?
    -Con la Ley de Conway era un sistema cuyos sistemas de disco 
     estaban obligados a producir diseños que son copias de las estructuras de comunicación

¿Qué es Ingeniería del caos?
    -Es la disciplina de experimentar en un Sistema, con la finalidad de generar
     confianza en la capacidad del sistema para soportar condiciones turbulentas en producción.