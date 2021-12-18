#####       PARTE 3      ######
##### ERICK DIAZ DELABRA ######

# SINTESIS DEL ARTICULO: Complete Guide to Monolithic vs. Microservices Architecture

* ARQUITECTURA MONOLITICA
Es considerada como la manera mas tradiciona, de construir aplicaciones. Una aplicacion monolitica esta construida en una sola e indivisible unidad. Por lo genera, cada aplicacion monolitica tiene una parte de usuario/cliente, una parte de servidor/aplicacion y una parte de base de datos. Todas estan unidas y se manejan desde el mismo lugar.

* FOTALIEZAS
Menos preocupaciones: Son todas las areas que componen una aplicacion, desde el registro, manejo, cache y rendimiento. Todo esto en una aplicacion monolitica pues esta unificado entonces es mas facil de manejar.

Facilidad a testeo: Solo debemos hacer 1 testeo en 1 aplicaion, gracias a la unificacion de todas las partes.

Facil lanzamiento: Esta es otra caracteristica buena de las apps monoliticas, debido a que solo es un lanzamiento y no multiples.

Facilidad de desarrollo: Debido a que es la forma mas común y antigua de desarrollo, la mayoria de los ingenieros tienen el conocimiento para desarrollar estas aplicaciones.

* DEBILIDADES
Comprendimiento: Cuando una app es suficientemente grande se vuelve complicado de comprender, ademas de que el codigo se vuelve mas complicado de manejar.

Cambios: Es dificil implementar cambios mientras mas larga y compleja sea nuestra app, esto debido a que cualquier cambio afecta a todo el sistema, asi que todo esto debe de estar perfectamente medido y cordinado.

Escalabilidad: No puedes escalar componentes independientes, tendrias que escalar toda la app.

Barreras tecnologicas: Es demasiado difici aplicar nuevas tecnologias, debido a que toda la app tendria que ser re-escrita.

##############################################################

* ARQUITECTURA DE MICROSERVICIOS
Mientras que una app monolitica simplemente es una unidad unificada, los microservicios se basan en una coleccion de pequeñas pero independientes unidades. Todas estas se manejan por separado y procesan sus propios servicios. Tienen sus propias bases de datos y funcionan para dar soluciones especificas.

* BENEFICIOS
Podemos serpara equipos de trabajo por cada micro servicio que tengamos en nuestra app.
Podemos escalar los servicios independientemente de los que no necesitan ser escalados.
Si hay un error, solo fallara un micro-servicio y no toda la applicacion por completo.
Podemos usar lengaujes de programacion o bases de datos mas eficientes para cada proceso requerido en un microservicio.
Podemos conectar cada micro servicio usando APIs.

* FORTALEZAS
Componetnes independientes: Todos los servicios se desarrollan y actualizan de manera independiente. 
Si hay un error en alguno de los microservicios pues solo ese fallara y no comprometeria a toda la aplicacion.

Comprendimiento: El separar todo en pequeños componentes se puede comprender y manejar mas facil todo. Ya que solo te enfocarias en eso y en mejorarlo.

Escalabilidad: Cada elemento o microservicio puede ser escalado independientemente de los demas. Esto es mas efecto y barado en dinero y tiempo, debido a que solo estamos mejorando lo necesario y no la aplicacion completa como en el caso de los monoliticos.

Flexibilidad: Los equipos de ingenieros no estan limitados por la tecnologia por la que se inició. Ellos pueden escoger diferentes tecnologias y frameworks para cada microservicio independientemente de los demas.

Agilidad: Cualquier falla solo va a comprometer el microservicio y no a la aplicacion completa, ademas de que solo buscaremos una solucion especifica y no una para toda la aplicacion en general.

* DEBILIDADES
Largas y complejas apps: Si tienes una app muy larga esta va a incrementar el tamaño de la aplicacion y se hara mas compleja y dificil de hacerle cambios.

Desarrollo lento: Mientras mas grande sea la app, sera mas dificil de comprender y modificar. Esto porque hay muchos equipos trabajando independientemente de los demás. Es mas dificil que todos esten enfocados en lo mismo o la misma idea general.

Escalabilidad: Necesitamos mas requerimentos de hardware. Esto puede pedir mas CPU o mas memoria, dependiendo.

Fiabilidad: Un pequeño error tambien puede romper todo esl sistema, y mientras mas grande sea nuestra app es mas probable que pase. Esto porque las apps van creciendo en microservicios pero tienen una "base" pequeña.

Inflexibilidad: Es dificil de tener nuevos frameworks y lenguajes. Imagina que tenemos 1M de lineas de codigo en el Framework XYZ. Ahora sera muy caro en terminos de costo para re escribir toda la aplicacion para usar un nuevo framework ABC. Asi que igaul hay un agran barrera en adoptar nuevas tecnologias.

##############################################################

* ¿ CUAL DEBEMOS DE ESCOGER Y BAJO QUE CIRCUNSTANCIAS?

* DESARROLLO: 
Monolitico: Si nuestra app es simple y puede que no hagamos cambios, ya que cualquier cosa puede romper todo el proyeto.

Microservicios: Estos requieren mas trabajo, desarrollar cada cosa por separado. Pero para actualazicaciones e implementacion de nuevas tecnologias suele ser mejor.

* MANTENIMIENTO
Monolitico: El mantenimineto suele ser sencillo, cualquier persona conoce la app.

Microservicios: El mantenimiento suele ser mas complicado, debido a que necesitamos a alguien qeu tenga todos los conocimientos de cada cosa que se usa en cada microservicio.

* FIABILIDAD
Monolitico: Un error supondria el fallo de toda la apicacion al 100%

Microservicios: Esta es la mejor, debido a que romper una microservicio no va a romper toda la aplicacion.

* ESCALABILIDAD
Monolitico: Dificil escalabilidad, debido a que todos tienen que trabajar en un solo proyecto y aparte re escribir todo el codigo completo.

Microservicios: Esta es la mejor, ya que podemos escalar independiente cada micro servicio dependiendo de nuestras necesidades.

* COSTOS
Monolitico: Esta suele ser mas barata, pero depende mucho de la aplicacion que queremos hacer y que tan grande sera nuestro proyecto.

Microservicios: Mas cara, por parte de mas personas especializadas, mas recursos, mas aprendizaje y mas programas.

* DESARROLLO
Monolitico: Dificil mientras mas personas sean, debido a que todos trabajan sobre lo mismo.

Microservicios: Mas rapidez, cada quien se especialyza y enfoca en lo suyo y listo.

##############################################################

# CONCLUSION PERSONAL

En lo personal considero que los micro-servicios son mejores en general, esto porque se me hace una mejor manera de desarollo, asi cada quien teiene su parte y se enfoca en ahcer lo que le tocó. Aun que depende, si queremos hacer una app chiquita y que no requiera mucho costo y mantenimiento, pues usar una arquitectura monolitica pues puede estar muy bien.