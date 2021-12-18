# Parte 3

## Arquitectura monolítica
Esta arquitectura se crea en un solo bloque el cual se desarrolla comúnmente en un solo lenguaje de
programación y con solo una base de datos. Sus ventajas son las siguientes: Es fácil de desarrollar 
para equipos pequeños, tiene una baja probabilidad de que falle ya que no depende de otros servicios
y es fácil de probar; y sus desventajas son que se enfoca en una sola tecnología, es difícil de 
comprender y escalabilidad deficiente.

## ARQUITECTURA DE MICROSERVICIOS
Esta arquitectura se basa en que divide la aplicación en múltiples partes, que se les conoce como 
servicios.Estos servicios tienen determinada una sola función que trabajan en conjunto para poder 
conformar la aplicación. Estos se comunican por métodos API.
Tiene ventajas como amplío uso de tecnologías dependiendo de la funcionalidad del servicio, 
los servicios son independientes y si falla uno, los demás siguen funcionando y es fácil de comprender.
Entre sus desventajas esta que es más costoso tener una aplicación con esta arquitectura, ya que como 
es una aplicación grande requiere de un grupo de desarrolladores para darle mantenimiento a cada 
servicio o hacer las pruebas para comprobar que funcionen bien, se lleva más tiempo al momento de
desarrollar. 

## Consideraciones al decidir Monolith vs Microservices
A mí punto de vista para poder decicir por uno u otro, esta decisión depende de las necesidades 
de la aplicación que se va a desarrollar, ya que desarrollar un monolito es más fácil que 
un microservicio. También se debe tener en cuenta el costo de aplicar cada arquitectura.

