¿Qué lenguaje de programación utiliza el equipo de Netflix?
Java Web

¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Si la base caía, todo el sistema también

¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
La pérdida de tiempo al querer hacer cambios, solucionar problemas, encontrar los errores y la necesidad de un hardware más grande para escalar.

¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Flower

¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
La separación de procesos, la escalabilidad y la virtualización

¿Qué analogía se utiliza para comparar los microservicios con la vida real?
El cuerpo humano y su la funcionabilidad de sus órganos

Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
Zul: como capa dinámica
NCCP: para dispositivos modernos
API: que permite la comunicación entre los servicios

¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
La dependencia, escalabilidad y la varianza

¿Qué es el falló en cascada?
Es cuando algún servicio tiene alguna falla y los que están conectados a éste empiezan a fallar en forma de cascada.

¿Qué es Hystrix?
Una estructura que usaba Netflix para los tiempos de espera para que el cliente pueda seguir usando el servicion sin que obtenga un error.

¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
La de un parasito en la librería ya que puede provocar fallas dentro de la aplicación y debilitar el servicio.

¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Con el Teorema CAP en donde se tiene que saber qué partición elegir entre consistencia y disponibilidad.

¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
La estrategia multiregional con tres AWS en las que sí una fallaba, aún podría funcionar.

¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
Stateles services, stateful services y hybrid services.

¿De qué manera se describe un "stateless service" en el video?
Como una base de datos que no almacena información, donde si se pierde un nodo no es un evento.

¿Qué es Chaos Monkey?
Si un noso muere, todo sigue funcionando

¿Qué es un microservicio híbrido?
Una combinación entre stateles services y stateful services.

¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
Particionando la carga de trabajo, el almacenamiento en caché a nivel de solicitud y con el respaldo de token seguro.

¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
Node.js, python, Docker y Ruby

¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
Herramientas de productividad,capacidades de insight y triage, fragancia de la imagen base, gestión de nodos, curva de aprendizaje, experiencia en producción.

¿Qué es Spinnaker?
Una plataforma de entrega automatizada administrada en la nube.

¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
Con diagnosticos encontraron las fallas, respaldando su servicio y mejorando su arquitectura.

¿Qué es "chaos engineering" o "ingeniería del caos"?
Cuando se realizan pruebas en un sistema para ver la capacidad de la disponibilidad, seguridad y el rendimiento para tener un sistema estable.