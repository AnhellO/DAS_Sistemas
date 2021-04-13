# Practica 1 - Parte 2

¿Qué lenguaje de programación utiliza el equipo de Netflix?
Java Web.

¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
El código base para Java Web era monolítico, el problema con eso fue cuando se introdujo un cambio que era difícil de diagnosticar.

¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
Era difícil de diagnosticar para encontrar posibles fallas, tomaba demasiado tiempo solucionar problemas, encontrar hardware adecuado. 
¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler.

¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
Separación de intereses, entorno virtualizado, escalabilidad a escala horizontal y particionamiento de la carga de trabajo dividiéndolo en componentes más pequeños que lo hacen más manejable.

¿Qué analogía se utiliza para comparar los microservicios con la vida real?
El cuerpo humano y su sistema de órganos, ya que cada órgano cumple su función y juntos forman un organismo.

Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
Zul: hacia enrutamiento dinámico, NCCP: admitía los dispositivos mas recientes y su capacidad de reproducción, API: era la puerta de enlace para cumplir con las solicitudes de clientes y que los servicios se comunicaran entre si.

¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
Dependencia, escalabilidad y varianza

¿Qué es el falló en cascada?
Es cuando algún servicio falla y este conectado a otros servicios comienzan a fallar uno tras otro en forma de cascada.

¿Qué es Hystrix?
Es la estructura para el manejo de tiempos de espera que permite que el cliente continúe usando el servicio en lugar de simplemente obtener un error.

¿Qué analogía utiliza el ponente para comparar las librerías de cliente con la vida real?
Una infección parasitaria ya que al igual que un parasito puede debilitarte pasa lo mismo en las librerías, provocan fallas dentro de la aplicación y debilitar tu servicio.

¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Con el teorema CAP en donde hay que saber que partición elegir entra consistencia y disponibilidad.

¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
Una estrategia multirregional con tres AWS regiones tales que si alguna de ellas fallaba por completo, todavía se podía mover todo el trafico hasta una de las otras regiones.

¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
Stateless services, Stateful services, Hybrid services.

¿De qué manera se describe un "stateless service" en el video?
Base de datos que no está almacenando masivamente cantidades de datos, seran metadados en memoria caché, capaz de remplazar un nodo defectuoso con relativa facilidad.

¿Qué es Chaos Monkey?
Es una herramienta para probar tu servicio y asegurarse de que pueda volver a funcionar rápidamente.

¿Qué es un microservicio híbrido?
La combinación de EVCache Writes y EVCache Reads

¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
partición de carga de trabajo, almacenamiento en caché a nivel de solicitud y con el respaldo de token seguro.

¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
node.js, python, docker y Ruby.

¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
Herramientas de productividad, capacidades insight & triage, fragmentacion de la imagen base, gestión de nodos.

¿Qué es Spinnaker?
Es una plataforma automatizada que esta diseñada para integrar mejor las aplicaciones.

¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
diagnosticando para encontrar fallas, respaldando su servicio y resolver las necesidades.

¿Qué es "chaos engineering" o "ingeniería del caos"?
Son pruebas definidas por Netflix para testear su sistema y testear la estabilidad, fragilidad, etc. de su sistema.
