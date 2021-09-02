
¿Qué lenguaje de programación utiliza el equipo de Netflix?
R: Java

¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
R: Les afecto el fallo principal de la arquitectura monolitica:
   Al hacer un cambio en la base de datos, esta fallo completamente.

¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
R: La desventaja principal fueron los cambios constantes en el sistema.

¿A qué autor cita el ponente cuando da el concepto de un microservicio?
R: Martin Fowler.

¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
R: Separación de preocupaciones, escalabilidad y
   Virtualización y elasticidad.

¿Qué analogía se utiliza para comparar los microservicios con la vida real?
R: Se habla de que los organos del cuerpo humano
   Representan a los microservicios, y que estos se unen
   Para formar organismos en general.

Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
R:  Java, Oracle con JDBC y un Linux host con Apache y     Tomcat.
¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
R: Dependencia, escala, varianza y como introduces los
   Cambios.

¿Qué es el falló en cascada?
R: Es cuando se presenta una falla en un sistema conectado
   Entre si, y ésta falla hace que falle otra o varias
   Partes del sistema, desencadenando una serie de fallas.

¿Qué es Hystrix?
R: Es una libreria que nos permite gestionar las interacciones
   Entre servicios en sistemas distribuidos, añadiendo lógica
   Y tolerancia de fallos.

¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
R: Compara las librerias con un parásito, que pueden infectar
   Al sistema, como cuando se tienen dependencias transitivas,
   Y que estas llevan mas bibliotecas y asi hacen que falle.

¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
R: Se plantearon que, en la presencia de una partición de
   De red, debian elegir entre consistencia y disponibilidad.

¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
R: La solución fue dividir los servicios de netflix en diferentes regiones (con AWS), para evitar una falla total.

¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
R: Stateless services, stateful services y Hybrid services.

¿De qué manera se describe un "stateless service" en el video?
R: Se describe diciendo que no es una base de datos que no 
   Almacena datos masivamente, existe acceso frecuente a 
   Metadatos almacenados en cache, y el mas importante es
   Que la pérdida de un nodo, no es esencialmente un evento.

¿Qué es Chaos Monkey?
R: Es un sistema para probar fallos, desarrollado por netflix
   Al migrar a la nube, y que confirma que cuando un nodo
   Muere, todo sigue funcionando. 

¿Qué es un microservicio híbrido?
R: Es una combinación entre "Stateful services" y
   "Stateless services".

¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
R: 1. Particionar carga de trabajo.
   2. Caching a nivel de solicitudes.
   3. Tokens seguros.
   4. Caos bajo carga.

¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
R:  Python, Ruby, Node js y Docker.

¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
R: 1. Herramientas de productividad.
   2. Capacidades de conocimiento y triaje.
   3. Fragmentación de la imagen base.
   4. Manejo de nodos.
   5. Duplicación de libreria/plataforma.
   6. Curva de aprendizaje - experiencia en producción.

¿Qué es Spinnaker?
R: Es una plataforma de entrega continua de multiples nubes 
   De código abierto, para lanzar cambios de software 
   Con alta velocidad y confianza.

¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
R: Implementaron una arquitectura nueva, donde se 
   Fragmentaron algunos microservicios y se acoplaron
   Mejor al sistema.

¿Qué es "chaos engineering" o "ingeniería del caos"?
R: Es un metodo de experimentación que se aplica a 
   Un sistema distribuido, con el fin de que muestre Evidencias de que es capaz de soportar condiciones
   De datos en masa en producción.

