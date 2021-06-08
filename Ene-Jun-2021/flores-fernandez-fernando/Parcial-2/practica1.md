Práctica 1 - Parte 1 
==================================================================================================================================
¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?
----------------------------------------------------------------------------------------------------------------------------------
R = El patrón de arquitectura monolítica es el mas facil de desarrollar por que todo el sistema está dentro de un solo servidor 
cada modulo se comunica por medio de memoria haciendolo mas sencillo de comunicarse y tambien de administrar cuando se usa en un 
sistema pequeño.

¿En qué consiste el patrón de arquitectura monolítica?
----------------------------------------------------------------------------------------------------------------------------------
R = el patrón de arquitectura monolítica consiste en tener todos sus módulos(servicios) dentro de un solo desplegable o servidor, 
y solo se comunica con el front end.

Y debido a que todo esta encapsulado en donde mismo los diferentes módulos se comunican entre ellos llamando métodos mediante el 
uso de memoria. 

¿Cuáles son las principales desventajas de una arquitectura monolítica?
----------------------------------------------------------------------------------------------------------------------------------
R = 
- como toda la aplicación esta en el mismo servidor al momento de escalarla se tendria que duplicar toda la aplicación, o en su 
defecto aumentar el hardware de una maquina para escalar cada componente.  

- otra desventaja es el uso de un solo sistema operativo que maneje toda la aplicación y tambien se utiliza un solo lenguaje de 
programación para todo el sistema.

- es mas difícil realizar test y medidas de los componentes.
- los componentes de este tipo de aplicaciones no puede ser reutilizado en otro tipo de aplicaciones.
- si hay cambios dentro del sistema hay que volver a desplegarla.  

¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
----------------------------------------------------------------------------------------------------------------------------------
R = 
- en primera se tendria que dar de baja la aplicación para poder realizar el cambio y volver a desplegar el sistema para poder 
volverlo a utilizar, teniendo tiempo muerto.

- debido a que todo se comunica dentro del mismo sistema hay que cambiar todo el sistema para hacer funcionar esta nueva 
funcionalidad  

¿Qué sucede si falla una aplicación monolítica?
----------------------------------------------------------------------------------------------------------------------------------
R= si un módulo de una aplicación monolítica falla todo el sistema falla. 

¿En qué consiste el patrón de arquitectura basada en microservicios?
----------------------------------------------------------------------------------------------------------------------------------
R = Este patrón esta basado en particionar el dominio de la aplicación, unificando cada servicio o módulo del sistema haciendo que 
se comuniquen por medio de la red, remotamente. 

Cada microservicio es una parte del sistema que hace una tarea en particular.

¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
----------------------------------------------------------------------------------------------------------------------------------
R = solo se tendria que escalar ese servicio por separado y no afectaria a ningun otro servicio. 

¿Qué es un ambiente basado en contenedores?
----------------------------------------------------------------------------------------------------------------------------------
R = un ambiente basado en contenedores ofrece a las aplicaciones basadas en microservicios una unidad para la implementación de 
de aplicaciones y un entorno de ejecución autónomo ideales.  

A su vez, permiten ejecutar en microservicios múltiples partes de una aplicación de forma independiente, en el mismo hardware, con
mucho más control sobre las partes y los ciclos de vida individuales.

Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, 
¿y por qué?
----------------------------------------------------------------------------------------------------------------------------------
R = no seriamos dependiente de ningun lenguaje de programación en específico ya que al solo recibir informacion de manera remota 
nosotros podemos mantener un formato para que todos los microservicios se entiendan entre si, sin necesidad de tener el mismo 
lenguaje o framework incluso.

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
----------------------------------------------------------------------------------------------------------------------------------
R = por medio de la red, ya sea internet si son microservicios remotos o red local si estan en la misma red.

¿Los microservicios pueden ser distribuidos? ¿Por qué?
----------------------------------------------------------------------------------------------------------------------------------
R = si, ya que pueden funcionar en diferentes servidores por medio de la red.

¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
----------------------------------------------------------------------------------------------------------------------------------
R = Uno de los principales desafios es la confiabilidad de la red que se tiene para comunicarse con los otros microservicios ya 
que muchas veces el sistema no tiene control en la velocidad de conexión ni la seguridad de las redes que se conectan 

¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
----------------------------------------------------------------------------------------------------------------------------------
R = Duplicando el microservicio para que si llega a fallar tener el mismo componente dentro del mismo servidor o en otro pero asi 
se asegura que se tiene otro de respaldo. 

Práctica 1 - Parte 2 
==================================================================================================================================

¿Qué lenguaje de programación utiliza el equipo de Netflix?
----------------------------------------------------------------------------------------------------------------------------------
R = todo estaba en Java usando tomcat para Javaweb.

¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
----------------------------------------------------------------------------------------------------------------------------------
R = Solo tenian un equipo de hardware donde tenian la base de datos, por lo tanto si se caía todo el sistema caía. y como tenia 
una arquitectura monolitica cuando la querian escalar solo se podia hacer vertical llegando a elevar el precio de mantenerla.  

¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
----------------------------------------------------------------------------------------------------------------------------------
R = la falta de agilidad (agility) que tenia el sistema ya que todo estaba conectado entre si, se hacian llamadas directas a la 
base de datos, muchas aplicaciones referenciaban directamente esquemas de tablas (table schemas) y simplemente agregar una columna a una tabla se tenia que modificar todo el sistema (big cross-functional project).

¿A qué autor cita el ponente cuando da el concepto de un microservicio?
----------------------------------------------------------------------------------------------------------------------------------
R = Cita a Martin Fowler. 

¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
----------------------------------------------------------------------------------------------------------------------------------
R =
- separación de problemas (modular o encapsulamiento)
- escalabilidad (horizontal)
- virtualización y elasticidad (operaciones automáticas)

¿Qué analogía se utiliza para comparar los microservicios con la vida real?
----------------------------------------------------------------------------------------------------------------------------------
R = Compara un sistema con microservicios con los sistemas de organos.
- cada órgano tiene su propósito.
- varios órganos forman sistemas.
- sistemas forman un organismo.

Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
----------------------------------------------------------------------------------------------------------------------------------
R =
- Zuul : hace routing dinámico.
- NCCP : legacy tier que soporta devices antiguos y tiene una capacidad fundamental de playback.
- Netflix API : se usa como API gateway manda a llamar a los servicios para llenar solicitudes de los clientes.

¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
----------------------------------------------------------------------------------------------------------------------------------
R = 
- Dependencias.
- Escala.
- Varianza.
- Introducir Cambios. 

¿Qué es el falló en cascada?
----------------------------------------------------------------------------------------------------------------------------------
R = es cuando un servicio en el cual dependen otros falla y los demas servicios no tienen una defensa propia para contrarestarlo
comienzan a fallar tambien haciendo un movimiento en cascada que termina con que todo el sistema falle. 

¿Qué es Hystrix?
----------------------------------------------------------------------------------------------------------------------------------
R = Es un sistema de antifallo que maneja los timeouts y los reintentos, haciendo que en lugar de que aparezca un error al cliente
tenga una respuesta estatica que mantenga el uso de la aplicación.

¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
----------------------------------------------------------------------------------------------------------------------------------
R = compara el problema con una infestación parasitica, no es un problema enorme que destruya el sistema completo de inmediato 
pero si son problemas pequeños que a la larga afectan a todo el sistema.  

¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
----------------------------------------------------------------------------------------------------------------------------------
R = utilizaron un metodo llamado cassandra que utilizaba Eventual Consistency, no espera a que cada write singular tenga un 
regreso de inmediato de cada lugar donde se escribe la informacion, haciendo que el cliente pueda guardar en un solo nodo para 
luego ser orquestado y guardado en diferentes nodos, luego se tiene el concepto de foro local (local Qourum) que dicta si se 
necesitan que varios nodos respondan que si se termino de hacer los cambios.

¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
----------------------------------------------------------------------------------------------------------------------------------
R = la estrategia fue dividir las regiones en varios servidores para que si por alguna razón una falla, las otras podian manejar 
el trafico de la que falló. 

¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
----------------------------------------------------------------------------------------------------------------------------------
R =
- stateless services
- stateful services 
- hybrid services

¿De qué manera se describe un "stateless service" en el video?
----------------------------------------------------------------------------------------------------------------------------------
R = 
- no se tiene cache ni base de datos.
- metadata frecuentemente accesada.
- no afinidad en instancias.
- perder un nodo es un no-evento. 

¿Qué es Chaos Monkey?
----------------------------------------------------------------------------------------------------------------------------------
R = es una herramienta de caos la cual se encarga de confirmar cuando un nodo muere pero el sistema sigue funcionando. 

¿Qué es un microservicio híbrido?
----------------------------------------------------------------------------------------------------------------------------------
R = es un servicio que funciona tanto como stateless y stateful. 

¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
----------------------------------------------------------------------------------------------------------------------------------
R = 
- en primera se dejó de mandar requests al mismo set de sistemas batcho y real-time.
- hacer los requests en el nivel de cache asi solo un servicio se usa al principio y los demas requests se hacen al cache del 
mismo.
- utlizar un token en cada device para hacer cada request agilizando la seguridad.    
- utilizar las herramientas de caos. 

¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
----------------------------------------------------------------------------------------------------------------------------------
R = se integró: 
- Python para trabajo operacional.
- Ruby para aplicaciones back-office.
- node.js para la aplicación web. 
- Docker para contenedores. 

¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
----------------------------------------------------------------------------------------------------------------------------------
R =
- herramientas de productividad.
- capacidades de triaje(clasificación) e intuición.
- fragmentación de la imagen base.
- mantenimiento de nodos.
- librerías/ plataformas duplicadas.
- curva de aprendizaje. 

¿Qué es Spinnaker?
----------------------------------------------------------------------------------------------------------------------------------
R = es un manejador de nube global que gestiona los cambios que se llegan a tener dentro de los microservicios. 

¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
----------------------------------------------------------------------------------------------------------------------------------
R = dejando a un lado la organizanión y comenzar a pensar del lado del cliente haciendo movimientos que sin importar los equipos
las soluciones es lo primero.

¿Qué es "chaos engineering" o "ingeniería del caos"?
----------------------------------------------------------------------------------------------------------------------------------
R = es la disciplina de experimentar en un sistema de software en producción para poder generar una confianza en las capacidades 
del Sistema. 
