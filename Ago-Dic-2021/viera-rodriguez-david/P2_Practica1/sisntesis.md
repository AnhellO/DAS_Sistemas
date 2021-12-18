## Arquitectura monolitica
Es una arquitectura que se suele usar de forma seguida para construir o hacer aplicaciones y estas aplicaciones tienen demasiado codigo y no tienen muchos modulos.

Si queremos hacer algun cambio hay que hacerlo de forma general osea en toda nuestra app.

## Ventajas
No hay preocupaciones en las actividades ya que solo es una sola app y esto facilita todo , las pruebas son mas sencillas de hacer por lo mismo que es una sola unidad y gracias a esto es sencilla de implementar ya que no se suelen manejar muchas implementaciones al contrario, solo suele ser un solo archivo y lo que trae cosigo esto es que sea facil de desarrollar ya que cualquier persona con conocimeitno de crear este tipo de apps puede lograrlo lo cual creo que suena un poco logico.

## Desventajas
Como no todo lo que brilla es oro claro que hay desventajas.

Su comprension puede ser dificil si esta app crece es por eso que que creo que suele recomendar tener conocmientos previos, ademas que hacer cambios esta muy complejo porque no solo es hacerlo sino que estamos corriendo riesgo en hechar a perder toda nuestra app ya que el cambio es general lo cual considero que seria la ultima opcion que tomaria.

Su escalabilidad es limitada ya que sus comeponentes no trabajn de forma independiente y claro, si aplicar tecnologias nuevas es dificil en este tipo lo es mas ya que como quien dice hay que hacer practicamente una nueva app.

## Microservicios
Es una aquitectura para crear una aplicacion pero esta tiene servicios pequeños que se comunican entre ellos para lograr un objetivo.

## Ventajas
Lo que me agrada de esta arquitectura es que tiene componentes independientes y esto facilita su actualizacion, tambien es muy atractivo que sea de facil comprension ya que te puedes concentrar en un solo servicio y no te perderas, su escalabilidad es muy buena por la misma razon que todo es independiente y su flexibilidad permite implementar cualquier tipo de tecnologia en cualquier momento.

## Desventajas
Creo que su desarrollo es demasiado lento ya que mientras mas crece una aplicacion se requirar un equipo mas amplio para poder trabajar en el codigo y eso toma tiempo y trae consigo que se inescalable ya que cada componente tiene requisitos diferentes y ademas es poco fiable ya que si un servicio cae los demas lo haran y esto provoca un fallo en nuestra app.

## Monolitico vs Microservicios ¿Cual escoger?

Hay que recordad que todo tiene alguna solucion es por eso que no hay que ser cerrado. Ademas, un monolito se puede escalar de manera efectiva siempre y cuando este bien estructurado. El como se estructura el proyecto juega un papel importante ya que todo estose piensa a largo a plazo y es por ello tomar mucho en cuenta las futuras implemtaciones a realizar. Todo esto va deacuerdo al equipo con el que se cuente ya que hay equipos multifuncion y claramente esto requeriria micro servicios. Son muchos los factores a tomar en cuenta pero creo que estos son los mas sobresalientes

## Ventajas y Desventajas de forma general

Las apps monolicitas solo se puede implementar una cosa a la vez y despues solo se ajustan los cambios conforme se requieran.

Por otro lado, los micro servicios son mas laboreosos, ya que cada micro servicio se implementa de forma independiente y esto complica el proceso de unificacion, pero lo bueno es que si aparece un error solo afectara a un solo servicio y no a toda la app.

Para un mantenimiento adecuado, los microservicios requieren un DevOps ya que se requiere mantener un estado de funcionamiento de CI para cada microservicio.

Sin duda alguna los microservicios son los mas fiables al desarrollar una app ya que un error solo queda en un servicio y no extiende a mas.

Los micro servicios tienen mejor escalabilidad ya que sus recursos se pueden usar con mas cuidado y se puede escalar todo aquello que requiera mas recursos.

En el desarrollo al menos para mi siento que los microservicios son mejores ya que se puede construir un archivo docker-compose mas facil y a su vez es mas facil trabajar en ellos.

En conclusion 

Si tienes un equipo pequeño , desarrollas la version definitiva un producto y tienes experiencia en frameworks solidos, la arquitectura monolitica es la ideal.

Si no tienes una fecha limite, cuentas con un equipo con amplio conocimiento y te preocupas por la escalabilidad y fiabilidad, los microservicios son los ideales.

## Desde la vista del test
Los microservicios no son facil de testear ya que no solo se puede ejecutar un solo servicio, en cambio los monolitos solo ejecutas el test y listo.

La informacion es muy dificil de manejar en los microservicios ya que cada uno de estos tiene su propia base de datos las cuales no tienen ninguna relacion entre si.

Los microservicios en la mayoría de los casos se basan en diferentes canales y protocolos para poder llevar a cabo alguna interaccion y cada canal es dificil de hacerle un test.

Desarrollar scripts de automatización es creo que sencillo pero el problema es cuando se intenta agregar pruebas automáticas a CI / CD.

Claro esta que los microservicios requieren más puntos finales y datos entre servicios y esto trae consigo que sea mas dificil encontrar el origen de un error. Y es obvio que los microservicios requieren muchos recursos.

## Consideraciones para los microservicios
-Integracion continua y Desarrollo continuo para que los desarrolladores puedan colaborar para construir el codigo.

-El registro y rastreo es suma importancia ya que se necesita saber cuando se inicia y termina una operacion.

-Controlar latencia nos ayudaria a brindar un servicio de calidad y dar satisfaccion a nuestro consumidor.

-Tener un sistema asincrono no nos ayudara a controlar la latencia es por eso no confiarze.

- Es una buena idea el orquestar ya que se toma en cuenta un punto central el cual nos guiara para sacar el proyecto adelante.

## ¿Cómo hacer el cambio a los microservicios?
Lo primordial es tener un plan, una infrastructura que de soporte y sin duda metricas de soporte por igual, como por ejemplo:

- Tener un plan.
- Usar un enlace de API.
- Medir flexibilidad, velocidad de entrega y resilencia.
- Hacer DevOps
