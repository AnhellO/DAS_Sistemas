<h1>Parte 2</h1>
<h3>¿Qué lenguaje de programación utiliza el equipo de Netflix? </h3>
<p>R = Usan Python</p>
<br>

<h3>¿Qué sucedía con la base de datos de Oracle del monolito de Netflix? </h3>
<p>R = Sucedia que en la web usaban una arquitectura monolitica y como esto lo actualizaban semanalmente, y cuando se introducian cambios pues podian haber errorer, un dia hubo un error que causo un fallo que causo que los albumes fueran dificiles de diagnosticar. </p>
<br>

<h3>¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica? </h3>
<p>R = Una de las principales fallas era que no se podian detectar fallos facilmente, eran dificiles de detectar, aunque extrajeran partes del codigo era muy dificil detectar estos fallos ya que se revisaban individualmente.</p>
<br>

<h3>¿A qué autor cita el ponente cuando da el concepto de un microservicio? </h3>
<p>R = Martin Fowler.</p>
<br>

<h3>¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios? </h3>
<p>R = <li>La modularidad</li> <li>La escalabilidad</li> <li>La particion del trabajo</li> </p>
<br>

<h3>¿Qué analogía se utiliza para comparar los microservicios con la vida real? </h3>
<p>R = Menciona algo sobre la familia, el tema de dividir el tiempo entre su familia y el trabajo</p>
<br>

<h3>Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces </h3>
<p>R = Usaban base de datos Oracle, tambien usaban Apache y una tecnología llamada Tomcat.</p>
<br>

<h3>¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios? </h3>
<p>R = Se espera que sean utilizadas en aplicaciones muy grandes o en las que la aplicación este en constante crecimiento. En donde una arquitectura monolitica no de para mas y asi con los microservicios poder escalar muy facilmente.</p>
<br>

<h3>¿Qué es el falló en cascada? </h3>
<p>R = Como su nombre lo dice, si algo falla, todo lo que esta debajo de ese fallo tambien comienza a fallar y asi se provoca un fallo en cascada. Esto derriba los servicios para todos los miembros.</p>
<br>

<h3>¿Qué es Hystrix? </h3>
<p>R = Hystrix es una biblioteca que controla o lleva el control de todos los microservicios, de la interaccion entre ellos. Le hace saber al usuario que algo ha fallado y de esta forma modifica su interfaz para hacerselo saber.</p>
<br>

<h3>¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real? </h3>
<p>R = Las compara con las celulas nerviosas.</p>
<br>

<h3>¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios? </h3>
<p>R = Creando dos bases de datos, donde una seria la copia de la otra y que estas se ejecuten en tres redes diferentes que podrian ser ejecutadas en 3 distintas regiones y de esta manera, si alguna llega a fallar, ya saben a que base de datos ir para solucionar el problema.</p>
<br>

<h3>¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012? </h3>
<p>R = Netflix desarrollo una estrategia que es multirregional de estreptococos con tres regiones de AWS, y de esta manera, si alguna de ellas llegaba a tener alguna falla o fallaba por completo, no se veria afectado en absoluto el trafico de datos y se enviaria a las regiones supervivientes.</p>
<br>

<h3>¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento? </h3>
<p>R = El escenario con estado de componentes fundamentales, el escenario sin editado y por ultimo y no menos importante, el escenario hibrido </p>
<br>

<h3>¿De qué manera se describe un "stateless service" en el video? </h3>
<p>R = La describe como una biblioteca de clientes. Como una base de datos de donde se manda a llamar la informacion y que este lista al momento en la que se requiera.</p>
<br>

<h3>¿Qué es Chaos Monkey? </h3>
<p>R = Son bases de datos o tambien podrian ser servicios con estados los cuales tienen caches y en donde se manejan gandes cantidades de datos</p>
<br>

<h3>¿Qué es un microservicio híbrido? </h3>
<p>R = La define como dos riñones, donde los dos trabajan juntos pero no depende el uno del otro, si no que son independientes. Si te quitan uno, puedes sobrevivir sin el otro, asi es como trabaja un microservicio hibrido.</p>
<br>

<h3>¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva? </h3>
<p>R = Usando una tecnologia la cual lleva por nombre edie cash y easy cash las cuales son como arquitecturas.</p>
<br>

<h3>¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores? </h3>
<p>R = Empezo a manejar Docker, node JS y uno de los lenguajes de programacion mas famosos, python.</p>
<br>

<h3>¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix? </h3>
<p>R = El hecho de tyene que moverse de tecnologias, como lo fue el echo de cambiarse a contenedores de docker y tener que cambiarse a node.js</p>
<br>

<h3>¿Qué es Spinnaker? </h3>
<p>R = Es un programa diseñado para llevar a cabo mejores practicas, para poderlas integrar de una mejor manera y asi poderla integrar en producion de una mejor manera.</p>
<br>

<h3>¿Cómo manejo Netflix el problema de las arquitecturas híbridas? </h3>
<p>R = Dejando de martillar el mismo conjunto de sistemas por lotes y en tiempo real hacer caché a nivel de solicitud para que no se este llamando repetidamente al mismo servicio una y otra vez una y otra vez. </p>
<br>

<h3>¿Qué es "chaos engineering" o "ingeniería del caos"? </h3>
<p>R = Es experimentar la compatibilidad del software estando en producción y asi poder soportar condiciones inesperadas.</p>
