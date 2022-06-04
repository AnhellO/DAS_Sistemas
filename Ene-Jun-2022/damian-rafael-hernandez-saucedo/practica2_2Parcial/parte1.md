- **¿Qué lenguaje de programación utiliza el equipo de Netflix?**
> Python, Netflix dio a conocer cómo lo utilizan dentro de su estructura de programación.

- **¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?**
> Usaba una base de datos Oracle usando JDBC que se interconectaban con otra base de datos Oracle.
el problema es que todos contribuian a una base de codigo que se implementaban semanalmente, esto propiciono el cambio a un servicio de microservidores.

- **Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?**
> Una de las partes mas dolorosas fue la falta de agilidad porque todo estaba profundamente interconectado tenian que hacer llamadas directas a la base de datos, habia muchas aplicaciones que referenciaban a un esquema de tablas. Uno de los puntos mas relevantes fue el tiempo de respuesta la lentitud del sistema.

- **¿A qué autor cita el ponente cuando da el concepto de un microservicio?**
> Martin Fowler

- **¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?**
> Separacion de aplicaciones monoliticas: fomentan la modularidad la capacidad de encapsular sus estructuras de datos. Escalabilidad de cordinacion: tiende a prestarse al escalado horizontal si te aborda correctamente y la particion de la carga de trabajo. Por ser un sistema distribuido. Puede tomar su trabajo y dividirlo en componentes mas pequeños que los hacen mas manejables. Entorno visualizado y elastico: es mucho mas dificil administrar microservicios si no lo hacen en este tipo de entorno.

- **¿Qué analogía se utiliza para comparar los microservicios con la vida real?**
> Organ Systems
Each organ has purpose 
Organs form System
Systems form an organism.

- **Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces**
> Netflix se lanzó en 1998. Al principio solamente era un servicio para alquilar DVD a través del servicio postal de los Estados Unidos. En 2007 Netflix presentó su servicio de reproducción de vídeos a la carta que permitía a los suscriptores ver series de televisión y películas. El servicio a telefonos y aplicacion independiente.

- **¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?**
> Intra-Service requests
Client Libraries
Data persistence
Infrastructure

- **¿Qué es el falló en cascada?**
> Un servicio que falla como defensas inadecuadas. Puede caer en cascada y puede derivar todo servicios para tus miembros.

- **¿Qué es Hystrix?**
> Manejo de tiempos de espera. Este concepto de una reserva, por lo que si no se puede llamar a un servicio se puede devolver una respuesta estatica o una respuesta para que el cliente pueda seguir usando el producto. En si son atajos a seguir para el corecto funcionamiento de la aplicacion.

- **¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?**
> Utilizo la analogia de 
-Parasitic Infestation
-Heap consumption
-Logical defects
-Transitive dependencies


- **¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?**
> Comensamos a pensar en las construcciones correctas y el teorema del limite. Con una particion de RED donde se eligue ante consistencia y disponivilidad, NETFLIX eligio el ultimo y abrazo este concepto (Eventual consistency) tiene mucha flexibilidad. Ya que el cliente puede orquestar en varios nodos.

- **¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?**
> NETFLIX desarrollo una estrategia multiregional de estreptococos con tres regiones AWS de modo que si alguna de ellas fallaba por completo, aun se podia mandarv todo el trafico a las otras supervivientes.

- **¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?**
> USE CASES
-Stateless services

-Stateful services

-Hibrid services


- **¿De qué manera se describe un "stateless service" en el video?**
> No es una base de datos no esta almacenado cantidades masivas de datos a los que habran accedidos con frecuencia metadatos almacenados en cache de memoria, por lo que existe la naturaleza no volatil.
Por lo general no tendra afinidad a las istancias. 
Lo describe como una repiclacion, al igual que la mitocis en biologia, podemos crear celulas a pedido o las celulas mueren costantemente y se reponen costantemente.

- **¿Qué es Chaos Monkey?**
> fue la primera herramienta de dolor de caos y simplemente se confirma que cuando un nodo muere, todos siguen funcionando. NETFLIX a implementado el mono del caos "No deja de perder el servicio de Britt".

- **¿Qué es un microservicio híbrido?**
> un sistema de desarrollo software, proponen su propia arquitectura. mas eficiente y rapido.
- **¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?**
> Reservas, cuando toda la capa del cache de Evie se cayo todavia era una reserva para el servicio y la base de datos y ese es el antpatron.
Soluciones fueron varias, lo primero es trabajar en el mismo conjunto de sistemas, para el almacenamiento el cache de nivel de solicitud por lotes y en tiempo real para que este llamado rapidamente al mismo servicio.

- **¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?**
> NETFLIX se ha acercado a una arquitectura utilizando una  tecnologia llamada edie cash y easy cash.

- **¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?**
> Cuanto mas variantes tenga mayor seran sus desafios porque aumenta la complejidad del entorno que esta administrando.

- **¿Qué es Spinnaker?**
> Fue diseñada para integrar las mejores practicas, de modo que a medida que las cosas se implementan en produccion, podemos integrar estas lecciones aprendidas.

- **¿Cómo manejo Netflix el problema de las arquitecturas híbridas?**
> Inovacion de interfazv de usuario. ya que contienen metadatos de contenido por lo que todos lops datos.
codigo de respuesta, una arquitectura mas moderna.
un modulo de seguridad de OAuth porque eso es lo que se requeria.
Un mecanismo de seguridad personalizado para tratar con tokens.

- **¿Qué es "chaos engineering" o "ingeniería del caos"?**
> Depende de una disiplina de inyectar caos en ese entorno. Utilizando interuptores automaticos y retrocesos y aplicar el caos que desee tener clientes simples.
El caos bajo carga para asegurarse de lo que cree que es cierto es relmante cierto para que las variantes diseñen sus operaciones.
