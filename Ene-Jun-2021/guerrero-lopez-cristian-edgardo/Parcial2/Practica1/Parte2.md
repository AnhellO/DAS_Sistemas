# Parte 2 Parcial 2

## ¿Qué lenguaje de programación utiliza el equipo de Netflix?
Java

## ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
Que el codigo base era de tipo monolitico, todos contribuian a una base de codigo que se implementaba semanalmente. Llegado un cambio causo que el album fuera dificil de diagnositacar.
Perdieron mucho tiempo

## ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
La busqueda de todo lo que tenian ya que extraian parte por parte de codigos y los probaban y esto tardo demaciado tiempo se dieron cuenta de la falta de agilidad que tenian en ese entonces todo estaba profundamente interconectado tenian llamadas directas a la base de datos.

## ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
Martin Fowler

## ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
* Separacion de preocupaciones
* Escalabilidad
* Perspectiva mas amigable al ejecutarlo en un entorno virtualizado y elastico

## ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
Se utiliza la analogia de que un microservicio se compara con el cuerpo o la biologia de este poniendo como ejemplo que cada parte se encarga de una funcion y se unen para formar un organismo.

## Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
* Capa de proxi detras del ELB llamada zul encargada del enrutamiento dinamico
* Nivel heredado llamado NCCP quien admitia los dispositivos y capacidad dde reproduccion fundamental aparte de la API de Netflix
* API arquitectura que llama a todos los demas servicios para cumplir distintas solicitudes
## ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
* Dependencia
* Escala
* Variacion
* Cambios

## ¿Qué es el falló en cascada?
Donde el fallo se da desde el principio y derriba todo su servicios siguientes y para sus miembros de paso
pd: dijo el vato que dios no lo quiera :V

## ¿Qué es Hystrix?
Estructura para mejorar las pripiedades, mejorar tiempos de espera, es como un respaldo algo que le permite al usuario seguir usando el producto sin necesidad de obtener un error

## ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
Con la inoculacion donde se pondria defenderse de un virus vivo con uno muerto

## ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
Comenzando a pensar en los conceptos correctos sobre el teorema del limite, una particion de red consistente en disponibilidad para tener un buen servicio.

## ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
Desarrollo un estretococo, una estrategia multiregional con tres regiones de AWS de modo que si alguna de ellas falla por completo, todavia se puede llevar acabo el trafico a los otros sobrevivientes

## ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
* Esenario de servicio
* Esenario de servicio con estado
* Hibrido
## ¿De qué manera se describe un "stateless service" en el video?
No es efectivo o una base de datos que no esta almacenado de manera masiva, cantidades de datos a los que se habra accedido con frecuencia metadatos almacenados en cache.
Informacion normalmente que no tendra afinidad de instancia donde espera un cliente para una instancia particular.
## ¿Qué es Chaos Monkey?
Primera herramienta dolorosa, confirma que si un nodo muere lo demas sigue funcionando.
No se han tenido problemas desde la implementacion de esta herramienta

## ¿Qué es un microservicio híbrido?
Donde los apartados de ambos se combinan herramientas de cada uno.
ayudando a netflix de forma muy util.

## ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
Al llamar libremente al cache tantas veces como se quiera,
como lo es recibir una perdida de cache entonces llamo en el servicio.
Esto redujo la reserva de servicio y de la base de datos

## ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
* Workload partitioning
* Request-level caching
* Token seguro dentro de los dispositivos
* Kaos

## ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
* Equipos de interfaz muy eficientes
* Base de fragmentacion y gestion de nodos mas especializados
* Titus
* Duplicacion de plataformas

## ¿Qué es Spinnaker?
Nueva gestion global, plataforma de sistema que entrega de forma automatizada. Fue desarrollado para las mejores practicas de modo que a medida que las cosas se implementan en produccion se pueden integrar lecciones aprendidas a los componentes automatizados.

## ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
Despues del rellno que se metio ese wey dijo que se movieron a la API de Netflix se trasladaron a la ingenieria de operaciones y eso fue lo correcto para el negocio
Poniendo soluciones primero y luego el equipo.
Hablando con el equipo reconfigurando la arquitectura en equipo.

## ¿Qué es "chaos engineering" o "ingeniería del caos"?
La Ingeniería del Caos es la disciplina de experimentar en un Sistema, con la finalidad de generar confianza en la capacidad del Sistema para soportar condiciones turbulentas en producción.
