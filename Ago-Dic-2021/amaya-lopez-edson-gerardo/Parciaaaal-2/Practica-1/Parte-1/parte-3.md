# Síntesis


### ¿Qué es la arquitectura monolítica?
    es una forma ya un poco tradicional de construir aplicaciones, es como una unidad que es una misma principalmete es la capa de logica y la de la interfaz

### Puntos fuertes de la arquitectura monolítica
    - Less cross-cutting: conerns las preocupaciones transversales son las que afectan menos, asi como el manejo de almacenamiento  y cache. en esta arquitectura el area de funcionalidad concierne solo a una aplicacion asi es mas facil de manejar

    - Easier debugging and testing: otro punto fuerte son las formas de depurar y probar el codigo de esta arquitectura ya que es una sola unidad. asi se aplican pruebas de extremo a extramo mas rapido

    - Simple to deploy: simple de implementar, como solo es uuna estructura no se tienen que manejar muchas implementaciones

    - simple to develop: cualquier equipo de ingenieros que tenga los conocimientos adecuados puede desarrollar una app monolitica

### Debilidades de la arquitectura monolítica
    - Understanding: cuando escalas una app monolitica se vuelve muy dicicil de entender tambien tiene un sistema de codigo que es dificil de mantener

    - Making changes: cada que la app crece se vuelve mas dificil de cambiar funcionalidades del codigo, esto hace que se tarde mas en sacar a produccion

    - Scabiliity: no deja escalar sus componentes independientemente

    - New technology barriers: es muy complicado implementar diferentes tecnologias a una app monolitica lo que provocaria que reescribieras la app

### ¿Qué es la arquitectura de microservicios?
    la arquitectura en microservicios su principal caracteristica es que divide la app en sus funciones haciendo estos metodos servicios que se comunican cuya principal funcion es compartir informacion.

### Puntos fuertes de la arquitectura de microservicios
    facil escalibilidad, puedes usar diferentes tecnologias en diferentes servicios hace la aplicacion mas independiente, dividiendolo en modulos que se comunican entre si, siendo estos independientes a la forma de implementar, escalar y mantener

### Debilidades de la arquitectura de microservicios
    si la aplicacion se incrementa en tamaño esto lo hace muy complicado de hacer cambios, a medida que crece el software el desarrollo se vuelve un poco menos agil, tambien la escabilidad se complica a la hora de no tener tantos recursos


### Arquitectura mejor para ti
    a la hora de decidir cual es la arquitectura por la que te debes ir, existe una pseudo-guia o mas que eso unas caracteristicas generales a tomar en cuenta

    de estas caracteristicas es importante ver en que estado te encuentras

    -la primera es ver que tantos integrantes tienes en el equipo si es pequeño considera la arquitectura monolitica.
    -no tienes suficientes recursos para contrata DevOps para dedicar mas tiempo al desarrollo de la arquitectura
    -considerar la experiencia en frameworks
    -no ve cuellos de botella en las funciones clave
    ---si es asi inclinese hacia la arquitectura monolitica
    -para los microservicios considere lo siguiente
    posee el tiempo suficiente para planear la arquitectura.
    -tienes un equipo con multiple conocimiento de lenguajes de proramacion
    -te preocupas por la escabilidad


### Arquitectura desde el punto de vista del testing.
    los microservicios son dificiles de probar juntos, en el 90% de los casos no se puede ejecutar un solo microservicio para probarlos, sin que antes se cree unos mocks de los servicios que depende.

    Los monolitos son mas facilites de probar pues todo su sistema se implementa en una unidad local.

    es mas dificil de testear ya que cada microservicio cuenta con su propia bd, y esto no genera integridad al momento de almacenar


