#####       PARTE 2      ######
##### ERICK DIAZ DELABRA ######

# ¿Qué lenguaje de programación utiliza el equipo de Netflix?
Phyton

# ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Usaban una base monolitica y cuando habia un  fallo todo se colapsaba, empezaba a fallar y aparte de que era dificil encontrar el error.


# ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
El encontrar los errores, una plataforma tan grande no podia permitirse tener errores que pudieran colapsar todo el sistema, asi que esta fue una de suis principales desventajas, junto con la necesidad cada vez de mas recursos.


# ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler


# ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
Modularidad, escalabilidad y virtualizacion.


# ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
Como se divide una familia para funcionar. Por ejemplo en mi caso, cada miembro de la familia puede ser un micro servicio xd, ya que mi mama se encarga mas de la casa, mi papa del trabajo, mis hermanos y yo escuela, limieza y asi.


# Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
Zuul que servia para el enrutamiento
Bases de datos de Oracle
Apache
NCCP

# ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
Usar micro servicios en aplicaciones muy grandes .
Usar micro servicios por si queremos compartir uno con dos aplicaciones diferentes.


# ¿Qué es el falló en cascada?
Un fallo que se lleva todo lo que le sigue. Por ejemplo si tenemos una falla en un dato en una base de datos, pues el uso de ese dato estara mal en toda la aplicacion.


# ¿Qué es Hystrix?
Una biblioteca de Netflix que sirve para controlar todos los microsericios que se usan. Sirve para detener fallos en cascada y notificar facilmente de un error.


# ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
Analgoia de las celulas nerviosas


# ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?

# ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
Usando tres regiones de AWS, si una llegaba a fallar se notificaba y se enviaba todo el trafico a otro servidor de alguna region qeu estuviera funcionando correctamente.


# ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
Stateless, Stateful y escenario Hibrido.


# ¿De qué manera se describe un "stateless service" en el video?
Una base de datos que se contiene toda a la informacion requerida y la informacion puede ser procesada por servidores distintos.


# ¿Qué es Chaos Monkey?
Software que contiene grandes cantidades de datos y sirve para detener instancias y contenedores, ayuda a detectar fallos y limites de los sitemas. Esto sirve para que sepamos hasta donde pude llegar nuestra aplicacion y sepamos en donde debemos de mejorar.


# ¿Qué es un microservicio híbrido?
Un micro servicio que trabaja en conjunto con otro, pero no depende del otro para funcionar.
En caso de que uno falle o tenga un error el otro puede seguir funcionando correctamente.


# ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
Python, docker y node js.


# ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
La actualizacion de tecnologias, el cambio de monolitico a micro servicios, la utilizacion de node js junto con docker y tener que aprender y dominar todas estas tecnologias. 


# ¿Qué es Spinnaker?
Software que sirve para probar cambios en nuestro software de manera rapida y confiable, nos ayuda a integrar los cambios de mejor manera a nuestra aplicacion.


# ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
Procesando las solicitudes en tiempo real y evitar que los servicios sean llamados en repetidas ocaciones.
Mejorando sus bases de datos.


# ¿Qué es "chaos engineering" o "ingeniería del caos"?
La ingenieria del caoes no sirve para probar nuestra aplicacion o sistema, nos permite expermientar para saber como reacciona nuestra app a condiciones extremas o inesperadas, ya sea por sobre cargo de solicitudes, informacion, falta de recursos, etc.