Arquitectura monolitica
La arquitectura monolítica se considera una forma tradicional de construcción de aplicaciones. Se construye como una unidad única e indivisible. Comprende una interfaz de usuario del lado del cliente, una aplicación del lado del servidor y una base de datos. Está unificado y todas las funciones se gestionan y sirven en un solo lugar. Las aplicaciones monolíticas tienen una gran base de código y carecen de modularidad. 

Puntos a favor de la arquitectura monolítica
- Less cross-cutting: El area de funcionalidad concierne solo a una aplicacion asi es mas facil de manejar.
- Easier debugging and testing: Es mas fácil depurar y probar el codigo de esta ya que es una sola unidad.
- Simple to deploy: Al ser una sola unidad se maneja una sola implementacion.
- simple to develop: Son faciles de desarrollar.

Puntos en contra de la arquitectura monolítica
- Understanding: Cuando escalas una app monolitica se vuelve muy dicicil de entender tambien tiene un sistema de codigo que es dificil de mantener.
- Making changes: Cada que la aplicacion crece se vuelve mas dificil de cambiar funcionalidades del codigo, esto se suele convertir en un proceso tardado.
- Scabiliity: No permite sus componentes independientemente.
- New technology barriers: Es muy complicado adaptar nuevas tecnologias a una aplicación monolitica ya que se debe reescribir gran parte del codigo.

Arquitectura de microservicios.
La arquitectura en microservicios divide la aplicacion en varias funciones o servicios haciendo que estos metodos compartan informacion y se comuniquen a traves de la web.

Puntos a favor de la arquitectura de microservicios
- Facil escalibilidad: puedes usar diferentes tecnologias en cada uno de los servicios ya que son independientes entre si.

Puntos en contra de la arquitectura de microservicios
- Si la aplicacion se incrementa en tamaño esto lo hace muy complicado de hacer cambios, a medida que crece el software el desarrollo se vuelve un poco menos agil que implica un gasto adicional en equipo de trabajo.

Testing.
- Los microservicios son dificiles de testear en conjunto, es complicado ejecutar un solo microservicio para testearlo sin que antes se cree mocks de los servicios que depende.
- Los monolitos son mas sencillos ya que todo su sistema se implementa en una unidad local.

No cambiaria respuestas pero si me gustaria complementar los conceptos de cada arquitectura, creo que las primeras definiciones fueron muy generales y podria complementarlas con como trabajan, describi como se componen mas no como trabajan a detalle, creo que seria un buen punto para complementar dicha información.