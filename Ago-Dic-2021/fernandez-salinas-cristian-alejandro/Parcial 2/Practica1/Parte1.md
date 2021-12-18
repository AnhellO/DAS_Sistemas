## ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
Los microservicos son mas faciles de desarrollar ya que cuentan con una gran flexibilidad para iintroducir macros,bases de datos y mas cosas sin ningun problema.

## ¿En qué consiste el patrón de arquitectura monolítica?
Consiste en crear una aplicacionque tenga toda la capacidad para realizar el objetivo para la que fue creada, sin dependencias de terceros que trabajen en aumentar la funcionalidad y utilizen los recursos.

## ¿Cuáles son las principales desventajas de una arquitectura monolítica?
- El sistema tarda mucho en iniciarse
- Si un modulo llega a fallar es posible que todo se vaya para abajo
- Toma muchos recursos para poder aplicarlo en una escala mas grande
- Si se requiere actualizar un componente del sistema es necesario actualizar todo el sistema completo

## ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
Se tendria que volver a desplegar todo el programa, y si este es muy extenso podria tomar mucho tiempo, no es posible solo actualizar ese componente.

## ¿Qué sucede si falla una aplicación monolítica?
Se tiene que redesplegrar todos sus componentes, porque todo es dependiente, y si el problema no tiene solucion se tendria que empezar de nuevo.

## ¿En qué consiste el patrón de arquitectura basada en microservicios?
Consiste en desarrollar aplicaciones que funcionan como un conjunto de servicios pequeños e independientes que juntos brindan la funcionalidad completa de lo que se requiere

## ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
Solamente el servicio que es afectado brindaría un rendimiendo deficiente al usuario mientras los demás funcionarian con normalidad

## ¿Qué es un ambiente basado en contenedores?
Un entorno operativo ligero que proporciona a las aplicaciones los archivos, las variables y las bibliotecas necesarias para ejecutarse y estos se utilizan para garantizar que la aplicación se ejecute correctamente cuando cambia su entorno, reduciendo así posibles errores.

## Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
No, la arquitectura basada en microservicios sigue un enfoque de diseño único, y esto permite que los equipos seleccionen el lenguaje que mejor se adapte a sus necesidades

## ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
- Por medio de los protocolos de la web HTTP(REST)
- Por medio de la API

## ¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si, cada servicio componente en una arquitectura de microservicios se puede desarrollar, implementar, operar y escalar sin afectar el funcionamiento de otros servicios.

## ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
- Diseño
- Pruebas
- Control de versiones
- Implementación
- Registro
- Depuración
- Conectividad

## ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
- Funcionalidad con un alcance adecuado
- Preparación de una API.
- Gestión del tráfico.
- Descarga de datos.
- Monitorización.
