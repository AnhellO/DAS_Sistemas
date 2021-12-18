PARTE 1

1.	¿Qué lenguaje de programación utiliza el equipo de Netflix?
El lenguaje de programación utilizado es Java Web.

2.	¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Una pieza del hardware estaba corriendo en una gran base de datos de Oracle, una vez que esta falló, de igual manera lo hicieron las demás.

3.	¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
Los periodos para la realización de pruebas eran extensos, por el hecho de que era complicado extraer cierta información necesaria para su posterior corrección y si esta era favorable, el volver a integrarla resultaba igual de complicado.

4.	¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler

5.	¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
-Escalabilidad.
- La separación y encapsulamiento de los procesos.
-Virtualización.

6.	¿Qué analogía se utiliza para comparar los microservicios con la vida real?
Son comparados con los órganos, pues estos trabajando en conjunto, sostienen a un solo organismo, dependiendo de sus diferentes funcionalidades.

7.	Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
-API: permite la comunicación entre los servicios y la ejecución de los procesos. 
-Zuul: Una capa que crea rutas de red de forma dinámica.
-NCCP: Permite la admisión de nuevos dispositivos.

8.	¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
-Cambios
-Dependencia, 
-Escalabilidad
-Varianza

9.	¿Qué es el falló en cascada?
Cuando existen entre una conexión entre dos o más servicios, de los cuales no estén debidamente protegidos, en caso de que uno falle, como el mismo nombre lo dice, el fallo pasara a los demás servicios.

10.	¿Qué es Hystrix?
Hystrix es una biblioteca de tolerancia a fallos y latencia diseñada para aislar puntos de acceso a sistemas remotos.

11.	¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
Con un parásito, haciendo alusión de que uno solo, provoca un daño imperceptible, a comparación de que existen varios de ellos.

12.	¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Empleando el teorema de CAP: A la presencia de una partición de red, se debe escoger entre consistencia y disponibilidad.

13.	¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
La estrategia multiregional.

14.	¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
- servicios stateless
- servicios estatales
- servicios híbridos

15.	¿De qué manera se describe un "stateless service" en el video?
Lo describe como una base de datos la cual no esta almacenando información, utiliza metadata que se frecuenta, además, si uno de los nodos se pierde, no se considera como evento.

16.	¿Qué es Chaos Monkey?
Este indica cuando uno de los nodos falla completamente, sin que el sistema deje de funcionar.

17.	¿Qué es un microservicio híbrido?
Combinación entre los microservicios stateful y stateless.

18.	¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
- partición de carga de trabajo
- caching a nivel de solicitudes
- Token de seguridad

19.	¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
Implementación de Docker, Python y Ruby.

20.	¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
- herramientas de productividad
- Fragmentación de la imagen base
- manejo de Node

21.	¿Qué es Spinnaker?
Una plataforma de entrega la cual es administrada en la nube.

22.	¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
En lugar de pensar en las soluciones

23.	¿Qué es "chaos engineering" o "ingeniería del caos"?
Cuando a un sistema se le son aplicados pruebas para comprobar la confianza de un sistema, y poder saber si este puede soportar condiciones caóticas.
