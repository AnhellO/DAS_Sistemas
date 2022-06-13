# Respuestas.
¿Qué lenguaje de programación utiliza el equipo de Netflix?
JAVA WEB

¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Si se caía todo el sistema caía.

¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
Tardaban mucho tiempo en agregar cambios, en encontrar errores y probar nuevamente que todo funcione bien. 

¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler.

¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
Separación de procesos.
Escalabilidad.
Virtualizació.

¿Qué analogía se utiliza para comparar los microservicios con la vida real?
Con los organos ya que cada organo tiene una funcion y este forma de un sistema que funciona en conjunto. 

Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
Zuul: capa dinamica.
NCCP: para dispositivos modernos.
API:  sirve para peticiones de los usuarios.

¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
Dependencia.
Varianza.
Cambios.
Escala.

¿Qué es el falló en cascada?
Es cuando un servicio falla y los servicios que están conectados entre si van fallando provocando un efecto cascada.

¿Qué es Hystrix?
Es un sistema que maneja los tiempos y los reintentos, haciendo que en lugar de que aparezca un error al cliente pueda seguir con el uso de la aplicación.

¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
Con un parásito porque va provocando pequeños fallos que no se pueden ver a prioridad solo cuando es mas grande el fallo. 

¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Con el Teorema de CAP.

¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
Una estrategia multiregión.

¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
Stateless services.
Stateful services.
Hybrid services.

¿De qué manera se describe un "stateless service" en el video?
No guardar en base de datos, no tener cache,
perder un nodo no es un evento.

¿Qué es Chaos Monkey?
Cuado un nodo muere, pero todo aun sigue funcionando.

¿Qué es un microservicio híbrido?
Que funciona con stateless y stateful.

¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
particionamiento del trabajo.
almacenamiento en caché a nivel de solicitud.
respaldo de token.

¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
Docker, node.js, python.

¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
Herramientas de productividad
Fragancia de la imagen base
Gestión de nodos
Curva de aprendizaje

¿Qué es Spinnaker?
una plataforma de entrega automatizada. 

¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
Pensando del lado del cliente para sus solucines y mejorar su arquitectura.

¿Qué es "chaos engineering" o "ingeniería del caos"?
Cuando hacen pruebas en un sistema para ver la capacidad en diferentes escenarios complicados.