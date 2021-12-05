##Parte 2##
**¿Qué lenguaje de programación utiliza el equipo de Netflix?**
_Python_

**¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?**
_En la web usaban arquitectura monolítica y era actualizado cada semana pero al haber cambios podían presentarse erores, uno de los fallos causó que los álbumes fueran difíciles de diagnosticar._

**¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?**
_El encontrar los fallos era complicado, estos eran dificiles de detectar, aunque extrajeran partes del codigo era muy dificil detectar estos fallos ya que se revisaban individualmente._

**¿A qué autor cita el ponente cuando da el concepto de un microservicio?**
_Martin Fowler._

**¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?**
_La modularidad, la escalabilidad y la particion del trabajo_

**¿Qué analogía se utiliza para comparar los microservicios con la vida real?**__
_Menciona algo sobre la familia, el tema de dividir el tiempo entre su familia y el trabajo_

**Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces**
_Se usaba base de datos Oracle, Apache y Tomcat._

**¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?**
_Que se usen en aplicaciones grandes o de constante crecimiento, donde una arquitectura monolitica no de para mas y asi con los microservicios poder escalar muy facilmente._

**¿Qué es el falló en cascada?**
_Como su nombre lo dice, si algo falla, todo lo que esta debajo de ese fallo tambien comienza a fallar y asi se provoca un fallo en cascada. Esto derriba los servicios para todos los miembros._

**¿Qué es Hystrix?**
_Hystrix es una biblioteca que controla o lleva el control de todos los microservicios, de la interaccion entre ellos. Le hace saber al usuario que algo ha fallado y de esta forma modifica su interfaz para hacerselo saber._

**¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?**
_Las compara con las celulas nerviosas._

**¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?**
_Creando dos bases de datos, donde una seria la copia de la otra y que estas se ejecuten en tres redes diferentes que podrian ser ejecutadas en 3 distintas regiones y de esta manera, si alguna llega a fallar, ya saben a que base de datos ir para solucionar el problema._

**¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?**
_Netflix desarrollo una estrategia que es multirregional de estreptococos con tres regiones de AWS, y de esta manera, si alguna de ellas llegaba a tener alguna falla o fallaba por completo, no se veria afectado en absoluto el trafico de datos y se enviaria a las regiones supervivientes._

**¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?**
_El escenario con estado de componentes fundamentales, el escenario sin editado y por ultimo y no menos importante, el escenario hibrido_

**¿De qué manera se describe un "stateless service" en el video?**
_La describe como una biblioteca de clientes. Como una base de datos de donde se manda a llamar la informacion y que este lista al momento en la que se requiera._

**¿Qué es Chaos Monkey?**
_Son bases de datos o tambien podrian ser servicios con estados los cuales tienen caches y en donde se manejan gandes cantidades de datos_

**¿Qué es un microservicio híbrido?**
_La define como dos riñones, donde los dos trabajan juntos pero no depende el uno del otro, si no que son independientes. Si te quitan uno, puedes sobrevivir sin el otro, asi es como trabaja un microservicio hibrido._

**¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?**
_Usando una tecnologia la cual lleva por nombre edie cash y easy cash las cuales son como arquitecturas._

**¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?**
_Empezo a manejar Docker, node JS y uno de los lenguajes de programacion mas famosos, python._

**¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?**
_El hecho de tyene que moverse de tecnologias, como lo fue el echo de cambiarse a contenedores de docker y tener que cambiarse a node.js_

**¿Qué es Spinnaker?**
_Es un programa diseñado para llevar a cabo mejores practicas, para poderlas integrar de una mejor manera y asi poderla integrar en producion de una mejor manera._

**¿Cómo manejo Netflix el problema de las arquitecturas híbridas?**
_Dejando de martillar el mismo conjunto de sistemas por lotes y en tiempo real hacer caché a nivel de solicitud para que no se este llamando repetidamente al mismo servicio una y otra vez una y otra vez._

**¿Qué es "chaos engineering" o "ingeniería del caos"?**
_Experimentar con la compatibilidad del sw mientras este está en producción._
