*¿Qué lenguaje de programación utiliza el equipo de Netflix?
Java

*¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Que si esta se caia todo el sistema se caia

*¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica
Que todo estaba interconectado por lo que tenian mucho problema con el codigo ya que cosas de base datos estaban en diferentes lados.

*¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler

*¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
Separacion de concerns, que cada cosa tiene una funcion, la escalabilidad, que puede crecer mas facil un sistema en esta arquitectura, virtualizacion y elasticidad, que el sistema es mas flexible con implementacion de por ejemplo automatizacion.

*¿Qué analogía se utiliza para comparar los microservicios con la vida real?
El cuerpo humano y las funciones de los organos

*Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
Recomendaciones, era el servicio que usaban para saber que lista de peliculas o programas tenian que recomendar al usuario,Suscripcion, es donde se obtenian los datos de sus suscriptores, Ruteado, para ver si los servicios se encontraban unos con otros y sus conexiones

*¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
Los servicios del cliente y del cache

*¿Qué es el falló en cascada?
Es cuando un servicio falla y este se lleva consigo a otros servicios lo cual ocasiona que varios fallen siendo que comenzo con uno.

*¿Qué es Hystrix?
Es una estructura creada por Netflix para toma de decisiones a la hora llamar a algun servicio, por si alguno falla o se puede tomar otra ruta, aqui se tome la decision

*¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
Las vacunas, estar preparados para cualquier caso

*¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Tomado una seleccion especifica de microservicios y trabajar sober estos, usaron algo llamado cassandra que ayudaba mandando el llamdo del cliente a un nodo que despues tomaba la decision de reenviarlo a otros nodos para saber si el commit se podria llevar acabo

*¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
Despues de que calleron sus servicios con AWS distribuyeron los llamados del servidor east a dos servidores, a uno en europa y otro en west

*¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
Stateless services,Stateful services, Hybrid services

*¿De qué manera se describe un "stateless service" en el video?
Son servicios que no guardan datos y que son bastante accesibles y accesados, lo describe como celulas que constantemente mueren y viven

*¿Qué es Chaos Monkey?
Asegurarse que si algun servicio muere no afecte a otros y el sistema continue funcionando

*¿Qué es un microservicio híbrido?
Es donde se convinan el Stateless y el Stateful, teniendo un servicio que necesariamente necesita de las propiedades de ambos

*¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
Teniendo varias formas de lidiar con esto, como un catching de niveles de request para llevar de forma mas eficiente los llamados

*¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
NodeJs,python,ruby y docker

*¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
Las herramientas y la productividad que daban, las capacidades del contenedor, el manejo de los nodos

*¿Qué es Spinnaker?
Una plataforma que crearon para el manejo en la nube de la toma de decisiones que hacian y llevar estadisticas.

*¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
Crearon algo que llamaron Blade Runner, donde conectaron los servicios para permitir tener una estructura mas organizada

*¿Qué es "chaos engineering" o "ingeniería del caos"?
Es introducir fallos a tu sistemas de manera que puedas saber que arreglando esto tendras un sistema estable, se basa en poner a pruebas la disponibilidad, seguridad y el rendimiento.