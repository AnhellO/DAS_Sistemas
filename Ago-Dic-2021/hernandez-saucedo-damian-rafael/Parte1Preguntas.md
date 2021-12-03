# Práctica 1
___
**Objetivos** 
- **Expandir el conocimiento teórico sobre el tema de arquitectura de software**
- **Conocer casos de uso reales de las arquitecturas de software más utilizadas**
- **Revisar múltiples recursos para aprender sobre el uso de los diferentes patrones de arquitectura de software**
___
# Especificaciones

**Parte 1**

- **Ver y analizar los siguientes videos:**
- **DIFERENCIA ENTRE UNA ARQUITECTURA MONOLÍTICA Y UNA DE MICROSERVICIOS**
Diferencias entre Monolitica y Microservidores: Una Arquitectura monolitica se puede resumir donde tenemos un Frontend y tenemos todos los servicios, que son modulos que estan integrados en un desplegable.
Ejemplo: un JAVA podria ser un JAR. Que todos estos estan corriendo dentro la misma maquina virtual, toda la comunicacion entre todos los modulos pasan a memoria.
Una diferencia microservicios lo que hacemos es particionar nuestro dominio, lo que hace es tomar cada uno de los context se aislan y logran que se comuniquen mediante RED. Todos los servicios se comunican remotamente se puede ver que la arquitectura de microservidores es una programacion distrivuida. Se cre que microservicios se consigue mas agilidad al llevar la aplicacion hasta la produccion dependiendo de la tecnica que se utilize.
se puede llegar a desarrollar usando tecnicas de microservicios en monolitica.

- **Microservicios | ¿Qué son los microservicios?, Introducción a Microservicios**
Cuando se crea una aplicacion por lo general se escogue un lenguaje de programacion y un solo lenguaje de base de datos. de esta manera unidos se puede desarollar una aplicacion webbackend.
cuando la aplicacion empiesa a crecer necesitara mas recursos y poco a poco se agregan mucho mas funcionalidad pero recordemos que la funcionalidad tambien tiene que ser mantenida. Poco a poco va creciendo en codigo como funcionalidad.
Para una administracion mejor tendriamos que dividir es donde tenemos alli la alternitiva de los microservicios.
Procedemos que los microservicios es una manera de poder dividir una aplicacion del back-end en multiples partes que se comunican por separado y cada uno tiene una funcionalidad especifica.
Esta arquitectura es una de las preferidas para las aplicaciones gigantescas.
Se puede desarollar en distintos lenguajes de programacion.
Los microservicios son para aplicaciones grandes es decir que esta arquitectura de microservicios es perfecta para aquellas aplicaciones que ya estan funcionando y necesitan una mejor forma de administrarlas.

¿Que son los microservicios? son conocidos por ser una arquitectura de aplicacion de lado del servidor o aplicacion back-end y son para apliocaciones grandes y complejas.
Los microservicios es tener una aplicacion grande subdividida en varias partes.

- **¿Qué es la Arquitectura de Microservicios?**
Los microservicios son componentes distrivuidos en nuestro sistema en donde cada componente expone funcionalidad al sistema. asi podemos modalizar nuestro sistema a traves de servicios indendientes.

Es comun que en la arquitectura de los microservicios tenga una base de datos independientes uno de los desafios es como sincronizar los datos. para que se comuniquen entre si.

Tenemos conexion de tipo directa(un servicio depende de otro), o indirecta(los servicios se comunican a traves de eventos).

Los desafios de la arquitectura de microservicios es que tenemos multiples aplicaciones distrivuidas.Hoy en dia hay muchas tecnologias que faciliotan el despliegue de aplicaciones distrivuidas."Este tipo de servicio es aun mas dificil", que un sistema monolitico.Pero tal cual tambien tiene ventajas y desventajas.




