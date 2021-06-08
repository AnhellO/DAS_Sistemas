¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
En mi consideración creo que el patrón con el menor grado de dificultad a la hora de desarrollar es el de microservicio puesto que este actúa de una manera independiente con sus compontes haciendo que estos no sufran cambios al momento de ser modificadas por algún agente externo o bien por algún error que surja se puede corregir y esto no compromete a las demás funciones.

¿En qué consiste el patrón de arquitectura monolítica?
Este consiste en que todos los métodos o bien todo el contenido de ejecución del programa queda sujeto a uno solo, ósea es un programa que depende de uno solo para su funcionamiento y esto como ya se había dicho genera una serie de inconvenientes.

¿Cuáles son las principales desventajas de una arquitectura monolítica?
Como ya se puede intuir su principal desventaja es su dificultad para poder desarrollarse por las opciones de tiempo y dificultad se ha dejado de ver en muchos proyectos, también el problema es que no tiene buena escalabilidad.

¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
El problema que existe es que en el momento de nosotros crear una función que podría hacer que nuestro código se vea afectado por lo que se estaría comprometiendo a todo el programa y se tendrían que hacer modificaciones mayores.

¿Qué sucede si falla una aplicación monolítica?
Como todos los componentes dependen uno del otro podríamos decir que todo fallaría por la dependencia que existe.

¿En qué consiste el patrón de arquitectura basada en microservicios?
Lo que nos dice esta es que consiste en una aplicación de varios servicios por llamarlos así que son independientes unos con otros.

¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
Lo que puede ocurrir es que se llegue a saturar puesto que no estaría diseñado para soportar esa carga, en caso de fallo y posterior modificación no existe una dependencia que haría que se modificaran mas cosas del programa.

¿Qué es un ambiente basado en contenedores?
Es una forma de trabajo para los microservicios desarrollada para mejorar la agilidad de los procesos.

Si utilizáramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
Creo que no puesto que estos se basan a servicios independientes asi como con conexión a api’s dando una mayor versatilidad en cuanto a un desarrollo de estas.

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
Esto puede ser por servidores o bien apis de la red.

¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si ya que estos no tienen una dependencia, pueden estar en otro lado y cumplir su función.

¿Cuáles son los principales desafíos de una arquitectura basada en microservicios?
Considero que los principales desafíos son que cuando se inicia muchos desarrolladores optan por una arquitectura monolítica, pero esto a la larga será algo que perjudique puesto que, al crecer la instancia y por ende los datos, así como la demanda, la arquitectura monolítica deja de ser eficiente.

¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
Con las llamadas en las funciones.

#Parte 2

•	¿Qué lenguaje de programación utiliza el equipo de Netflix?
Java web
•	¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Esta era una pieza de hardware que llamaba a una gran base de datos.
•	¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
La demanda constante hacia que tuvieran no solo que modificar la programación, sino que se requeria de mas hardware para poder hacer un escalado de esto.
•	¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler
•	¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
	Separación de procesos
	encapsulamiento
	Escalabilidad.
	virtualización y elasticidad
•	¿Qué analogía se utiliza para comparar los microservicios con la vida real?
Lo compara con el sistema de órganos de un cuerpo y habla como un órgano hace una función específica, pero todos se unen para formar un organismos.
•	Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
Zuul hace el enrutamiento dinámico
NCCP que admitía dispositivos, así como la muestra de la api de Netflix 
API el núcleo que llama a los demás servicios para cumplir con la solicitud.
•	¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
Escalabilidad
Varianza
Cambios
Dependencia
•	¿Qué es el falló en cascada?
Este es un fallo que ocurre pero que debido a como se esta construido en cascada derriba todo el servicio para los usuarios
•	¿Qué es Hystrix?
Este es una estructura la cual nos permite manejar los tiempos de espera asi como los reintentos de entrada, esto mediante una redireccion si no es posible acceder a un servicio.
•	¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
Hizo la comparación con un parasito pues pueden estar ahí y generar una serie de daños mas grandes con mas pasa el tiempo.
•	¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Esto fue con el teorema de CAP con el cual la existencia de alguna partición de red debe de elegir entre dos opciones que son la consistencia y disponibilidad.
•	¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
Esta consistió en una estrategia multiregional con tres regiones diferentes por si alguna fallaba podría funcionar.
•	¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
Stateless services
Stateful service
Hybrid services
•	¿De qué manera se describe un "stateless service" en el video?
No guarda datos o chache y accede con frecuencia a metadata y no tendrá afinidad de instancia.
•	¿Qué es Chaos Monkey?
Dice básicamente que si algún nodo muere esto no afecta al funcionamiento.
•	¿Qué es un microservicio híbrido?
Es la combinación de los servicios de stateless y stateful
•	¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
Partir la carga de trabajo 
Almacenamiento en cache
Respaldo de token
•	¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
Docker
Ruby
Node js
•	¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
Productiviy tooling
Insight & triage capabilities
Base image fragmentation
Node managment
•	¿Qué es Spinnaker?
Una plataforma de entrega y automatizacion
•	¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
Primero las soluciones, el equipo, refactorización para respaldos.
•	¿Qué es "chaos engineering" o "ingeniería del caos"?
Esto es cuando hacen pruebas en un sistema con la finalidad de ver la posibles capacidades que puedan causar problemas.
