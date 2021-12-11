*¿Qué lenguaje de programación utiliza el equipo de Netflix?
R= Python

*¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
R= La base del codigo de java para web era monolitica, todos contribuian a una base de codigo que se implementaba semanalmente el problema radicaba que cuando se introdujo un cambio causo que el album fuera dificil de diagnosticar.

*¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
R= Los fallos eran dificiles de disgnosticar, la escabilidad vertical, la falta de agilidad.

*¿A qué autor cita el ponente cuando da el concepto de un microservicio?
R= Martin Fowler.

*¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
R= El dinamismo, lo facil que es hacer cambios en el codigo / El alcance de hacer funcionalidades especificas y de una manera muy simple

*¿Qué analogía se utiliza para comparar los microservicios con la vida real?
R= La analogia donde compara los microservicios con los organos.

*Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
R= Base de datos oracle / Apache / Tomcat

*¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
R= Aplicaciones en donde se ve un crecimiento exponencial, donde de tener una arquitectura monolitica no de abasto para este crecimiento y asi poder escalar fácilmente la aplicación.

¿Qué es el falló en cascada?
R= Es cuando un servicio falla y tira todos los demas servicios, si se desplegó este cambio erroneo en multiples regiones no hay lugar para recuperarlo, solo queda arreglarlo.

*¿Qué es Hystrix?
R= Es una biblioteca que controla la interacción entre microservicios para proporcionar latencia y tolerancia a fallas.  Además, tiene sentido modificar la interfaz de usuario para que el usuario sepa que es posible que algo no haya funcionado como se esperaba o que tomaría más tiempo.

*¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
R= De la infeccion parasitaria.

*¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
R= Empezando a pensar sobre las construccciones correctas y con el CAP Theorem, establece que es posible optimizar para dos de cualquiera de estos aspectos: consistencia, disponibilidad y tolerancia de partición de red, pero no los tres.

*¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
R= Aislar regiones, para que las interrupciones en los EE.UU. O Europa no se afecten entre sí.

*¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
R= Escenario sin estado, escenario con estado con componentes fundamentales y escenario hibrido.

R= ¿De qué manera se describe un "stateless service" en el video?
R= No es un efectivo o una base de datos, no esta almacenando cantidades masivas de datos tendras frecuentemente metadatos accesados en cache, asi que su naturaleza es no volatil, o de configuracion de información.

*¿Qué es Chaos Monkey?
R=  Es el responsable de terminar instancias de manera aleatoria, para asegurar se que los ingenieros hayan implementado servicios a prueba de fallos antes de hacer un deploy y asi poder regresar para que no se suba código con errores.

*¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
    acercado a una arquitectura usando una tecnología llamada edie cash y easy cash es esencialmente un envoltorio alrededor de Memcache D, está dividido de manera similar a los cachés de calamar, pero hay varias copias. escrito en varios nodos, por lo que cada vez que ocurre una escritura, no solo se escribe en varios nodos, sino que los escribe en diferentes zonas de disponibilidad, por lo que los esparce y los separa en la partición de red y, de la misma manera, cuando leemos, las lecturas son locales. porque desea esa eficiencia local, pero la aplicación puede recurrir a la lectura en las zonas de disponibilidad que necesita para llegar a esos otros

*¿Qué es un microservicio híbrido?
R= Lo describe como "Es fácil de tomar EVCache asegurado", 30 millones de peticiones por segundo, 2 trillones de peticiones por día globalmente, miles de millones de objetos, 10 mil instancias de memcached, milisegundos de latencia por peticion.

*¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
R= Con la tecnologia "EVCache" el cual es un wrapper alrededor de Memcached, multiples copias escritas a multiples nodos, asi que cada vez que una escritura pasa no solo se escribe en multiples nodos, sino que los escribe en varias zonas de accesibilidad.

*¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
R= Node.js y Docker.

*¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
R= Hacer las operaciones automaticamente / Escala y uso de dependencias

*¿Qué es Spinnaker?
R= Un administrador de aplicaciones, permite hacer cambios de software con una velocidad alta y confiable.

*¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
R= La solución fue eliminar completamente las unidades centrales de su arquitectura, por lo que los nodos comparten los mismos privilegios y responsabilidades de un cliente y un servidor.

*¿Qué es "chaos engineering" o "ingeniería del caos"?
R= Es la disciplina de experimentar en un software en producción para asi crear confidencia en la capabilidad del sistema para soportar condiciones inesperadas y turbulentas.