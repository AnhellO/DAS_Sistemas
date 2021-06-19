# Practica 1 Parcial 2 Cristian Edgardo Guerrero Lopez 15028518

## ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios) y por qué?

El patron mas sencillo se da en la monolitica ya que nos da la suficiente eficiencia. Es mas facil de programar y se corre dentro de la maquina virtual ya que son metodos.
 El entorno en el que se contruyen este tipo de soluciones esta muy bien definio y ofrece poco margen a los fallos, esta caracteristica tambien crea entornos muy rigidos que no pueden ser facilmente actualizables.

## ¿En qué consiste el patrón de arquitectura monolítica?
El estilo arquitectónico monolítico consiste en crear una aplicación autosuficiente que contenga absolutamente toda la funcionalidad necesaria para realizar la tarea para la cual fue diseñada, sin contar con dependencias externas que complementen su funcionalidad. En este sentido, sus componentes trabajan juntos, compartiendo los mismos recursos y memoria. En pocas palabras, una aplicación monolítica es una unidad cohesiva de código.
Los sistemas monoliticos agrupan la funcionalidad y sus servicios en una base de codigo unica.
Tienen como característica el uso de una base de código única para sus servicios o funcionalidades.

## ¿Cuáles son las principales desventajas de una arquitectura monolítica?
Aunque son fáciles de desarrollar, una aplicación que lleva toda su funcionalidad no es la mejor opción, en el caso de que se tengan aspiraciones de crecimiento complejas, más usuarios, más desarrolladores…
Algo que caracteriza a las aplicaciones monolíticas, es que en el momento que se quiera realizar un nuevo despliegue, se debería relanzar todo el sistema de nuevo.

Algunas de las desventajas mas notables son:
* Escalado Monolítico
* Las aplicaciones Monolíticas son fácil de operar con equipo pequeños, pero a medida que la aplicación crece y con ello el equipo de desarrollo, se vuelve cada vez más complicado dividir el trabajo sin afectar funcionalidad que otro miembro del equipo.
* Versión tras versión: Cualquier mínimo cambio en la aplicación implicará realizar una compilación del todo el artefacto y con ello una nueva versión que tendrá que ser administrada.
* La mas importante en mi opinion: Si falla, falla todo!

## ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
* La dificultad de escalado ya que habria que actualizar una nueva version esto implica gastos de recursos.
* Poco modificable para aumentar su rendimiento.
* Cualquier minimo cambio de la aplicacion implica comppilar todo el artefacto.

## ¿Qué sucede si falla una aplicación monolítica?
No hay vuelta atras fallo y fallo esto ocaciona mucho estres y flojera xd
Al tener tan poca escabilidad te forzara a tener que implementar mas recursos aparte de todos los problemas que puede haber como bloqueos en la base de datos, consumo desmedido de memoria,lecturas de disco etc. Un fallo puede dejar fuera de servicio a la aplicacion.

## ¿En qué consiste el patrón de arquitectura basada en microservicios?
Los microservicios son una manera de construir aplicaciones y servicios digitales. Una arquitectura de microservicios busca desacoplar o independizar los componentes individuales de una aplicación, para que cada componente sea una aplicación en sí misma. Los microservicios se conectan entre sí a través de API’s, permitiendo que diferentes equipos trabajen al mismo tiempo en diferentes partes de una aplicación.

## ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
El obtener y convertir datos haria que el servidor tenga mucho mas peso en el procesador al tener multiples partes necesitaras herramientas para verificar una por una todo esto consume TIEMPO.

## ¿Qué es un ambiente basado en contenedores?
La organización en contenedores automatiza la implementación, la gestión, la escalabilidad y la conexión en red de los contenedores. Las empresas que necesitan implementar y gestionar cientos o miles de hosts pueden beneficiarse de la organización en contenedores.
Los contenedores ofrecen a las aplicaciones basadas en microservicios una unidad para la implementación de aplicaciones y un entorno de ejecución autónomo ideales. A su vez, permiten ejecutar en microservicios múltiples partes de una aplicación de forma independiente, en el mismo hardware, con mucho más control sobre las partes y los ciclos de vida individuales.

## Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
No ya que podriamos usar multiples lenguajes no estamos atados a solo uno, cada profecional ocupara sus herramientas esto en proyectos o empresas grandes es muy beneficioso.
Todo funciona de manera comunicada ya que solo hablamos de separar conceptos de la aplicacion.

## ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
Se pueden comunicar atravez de lenguajes de programacion, internet o frameworks para diferentes lenguajes.

## ¿Los microservicios pueden ser distribuidos? ¿Por qué?
Si por que no estamos limitados a un solo equipo, podemos hacer que todo funcione correctamente dividiendo cada parte en pequeñas cosas donde cada objetivo o segmento se ocupara de su propoio trabajo poniendo la oportunidad de actualizacion y mejoramiento a facil acceso.

## ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
Desarrollar, testear e implementar cada apartado por separado esto llevara tiempo, tambien dependeriamos de la seguridad de la red ya que accederiamos por internet.
Tambien el codigo para comunicar servidores llega a ser algo complicado y tambien los procesamientos del procesador esto llevara mas carga al servidor.

## ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
Con la facilidad de actualziacion, testeo y despliegue.
Tambien la mejora de recursos y facilitacion de acceso a cada aaprtado.
Tener una app grande subdividida en pequeñas partes hace posible todo esto y es gracias a los microservicios.