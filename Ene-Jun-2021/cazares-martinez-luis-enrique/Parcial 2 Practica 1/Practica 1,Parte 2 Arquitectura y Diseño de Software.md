¿Qué lenguaje de programación utiliza el equipo de Netflix?
- Python.

¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
- Si habia algun error en la base de datos, todo comenzaba a fallar.

¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
- la falta de capacidad de respuesta: no se podian hacer cambios lo suficientemente rápido, ya que todos 
los componentes de la arquitectura estaban estrechamente conectados entre sí. 
por lo que incluso agregar una columna a una tabla se convirtió en un gran problema 
para un proyecto multifuncional. 

¿A qué autor cita el ponente cuando da el concepto de un microservicio?
- Martin Fowler.

¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
- • Separación de componentes.
  • Modularidad y la capacidad de encapsular estructuras de datos.	
  • No se tiene que lidiar con la organización de la coordinación de su interacción.

¿Qué analogía se utiliza para comparar los microservicios con la vida real?
- Los micorservicios se comparan a los Organos de un sistema.
	• Cada organo tiene un proposito.
	• Los organos forman un sistema.
	• Los sistemas forman un organismo.

Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
- •Subscriber:
El servicio de suscriptor brinda información detallada sobre los clientes.
  •Recomendations: 
Brinda la información necesaria para crear una lista de películas que serán presentadas a cada cliente.
  •Platform services/Routing:
permite que los servicios se encuentren entre sí.
 
¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
- Hay cuatro áreas para explorar: 
	• Dependencias: Solicitud de infra-servicio.
	• Escalado: Servicios apátridas (Stateless services).
	• Diferencias según su arquitectura: Cuanta más variedad tengas en tu sistema, más complejo y 
	difícil de administrar se volverá.
	• Cambio: Cómo se deben realizar estos cambios. 

¿Qué es el falló en cascada?
- Un servicio falla sin defensas, puede caer en "cascada" y derribar toda su red.
Solution "Hystrix".

¿Qué es Hystrix?
- Hystrix es una biblioteca de latencia y tolerancia a fallas diseñada para aislar puntos de acceso a sistemas remotos, 
servicios y bibliotecas de terceros, detener fallas en cascada y habilitar la resistencia en 
sistemas distribuidos complejos donde las fallas son inevitables.

¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
- A una infección parasitaria. 
" La fea criatura del tobogán no tiene el tamaño de Godzilla y no es capaz de destruir Tokio,
pero infectará tus intestinos, que son adecuados para los vasos sanguíneos, y comenzará a beber tu sangre como un vampiro. 
Esto provocará anemia y debilitará enormemente su cuerpo. "

¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
- Netflix ha propuesto un enfoque de "consistencia final" 
No se espera que cada registr se lea inmediatamente de cualquier fuente en la que registramos los datos, escribimos más
y luego se repliquen completamente para lograr la consistencia de los datos. 
Cassandra hace frente a esta tarea a la perfección, tiene una gran flexibilidad, por lo que el cliente solo puede 
escribir en un nodo, que luego escribe en varios otros nodos mediante la orquestación.

¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
- Después de este incidente, se implemento una estrategia multirregional con tres regiones de AWS para que, 
si una de ellas fallaba, se pudiera transferir todo el tráfico a otras dos regiones.

¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
- Servicios sin estado, servicios con estado y servicios híbridos.

¿De qué manera se describe un "stateless service" en el video?
- Para empezar, esto no es un caché o una base de datos donde almacena una gran cantidad de información.
En su lugar, ha utilizado con frecuencia metadatos almacenados en caché en la memoria no volátil.

¿Qué es Chaos Monkey?
- Chaos Monkey es una herramienta que destruye aleatoriamente instancias o procesos de AWS en servidores 
que ejecutan Netflix. Esta herramienta confirma que si uno de los nodos del nodo “muere”, 
entonces todo lo demás sigue funcionando sin problemas.

¿Qué es un microservicio híbrido?
- Son una combinación de servicios apátridas y con estado (Stateless service & State service). 
En este caso, es muy fácil utilizar EVCache (Básicamente es un envoltorio de Memcache, que escribe múltiples copias 
en múltiples nodos en múltiples ubicaciones) como la tecnología de tolerancia a fallos más adecuada.
Lo cual permite procesar 30 millones de solicitudes por segundo, lo que equivale a 2 billones de solicitudes por día.

¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
- La solución a este problema es compleja:

 • Detener la "manipulación" del mismo grupo del sistema con solicitudes fuera de línea y llamadas en tiempo real, 
   dividiendo la carga de trabajo en segmentos en línea y fuera de línea.
 • Organizar el cobro a nivel de solicitud, es decir, vincular siempre el ciclo de vida de escritura al área de solicitud actual, 
   de modo que sea imposible llamar al mismo servicio una y otra vez.
 • Incorporación de tokens de seguridad alternativos en los dispositivos de los usuarios.
En Netflix se logro capacitando continuamente al personal y aprendiendo rápidamente de los incidentes a medida que ocurrian, 
y automatizando la implementación de técnicas avanzadas de solución de problemas en la infraestructura.

¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
- las mejores tecnologías para Netflix que se integraron en las mejores prácticas predefinidas basadas en 
Java y EC2, pero a medida que el negocio crecía, los desarrolladores comenzaron a agregar nuevos componentes como Python, 
Ruby, Node-JS. y Docker.

¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
- El costo de estos cambios es bastante elevado y consta de los siguientes factores:
	• Herramientas de productividad
	• Fragmentación de imágenes básicas
	• Gestión de nodos.
	• Duplicación de biblioteca o plataforma.
	• Curva de aprendizaje y experiencia en fabricación.

¿Qué es Spinnaker?
- Una nueva plataforma global de administración y entrega continua (CD) basada en la nube.

¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
- Se movio de un hash de servicios a una arquitectura llamada Blade Runner.
"Blade Runner", porque aquí estamos hablando de servicios de límites y las capacidades de NCCP para 
separarse e integrarse directamente en proxies Zuul, puertas de enlace API y las correspondientes 
funciones Las "piezas" se convirtieron en nuevos microservicios con funciones de seguridad más avanzadas,
reproducción, clasificación de datos, etc.

¿Qué es "chaos engineering" o "ingeniería del caos"?
- La ingeniería del caos es la disciplina de experimentar en un sistema de software en producción con el 
fin de generar confianza en la capacidad del sistema para resistir condiciones turbulentas e inesperadas.