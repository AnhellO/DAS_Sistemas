PARCIAL 2 Practica 1

Parte 1
¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
    Los microservicios con mucho más fáciles de trabajar que las aplicaciones monolíticas. Además permiten introducir nuevos marcos, fuentes
    de datos y demás recursos sin dificultades.

¿En qué consiste el patrón de arquitectura monolítica?
    Es donde se tiene una parte de Frontend, y otra parte de servicios o modulos, que estan integrados en un desplegable, y absolutamente
    todos estan corriendo bajo la misma maquina virtual, por lo tanto toda la comunicación pasa a memoria.

¿Cuáles son las principales desventajas de una arquitectura monolítica?
    El entorno en el que se construyen este tipo de soluciones está muy definido y ofrece poco margen a los fallos. Con todo, esta característica
    tambíen crear entornos muy rigidos que no pueden ser fácilmente actualizables.

¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
    Que en el momento que se quiera realizar un nuevo despliegue, se debería relanzar todo el sistema de nuevo.

¿Qué sucede si falla una aplicación monolítica?
    Si falla alguna función o componente de una sola aplicación, toda la aplicación deja de funcionar.

¿En qué consiste el patrón de arquitectura basada en microservicios?
    Consiste en una arquitectura de aplicaciones del lado del servidor, y es para aplicaciones grandes y complejas, se divide una aplicacion en 
    multiples partes o mejor conocidos como servicios, y estos hacen partes especificas, para así unirse y funcionar como una sola.

¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
    Nuestra aplicación tiene que seguir respondiendo de una mejor manera incluso, también necesitamos poder proveer mayores servicios a nuestra aplicación cuando va creciendo.

¿Qué es un ambiente basado en contenedores?
    Los contenedores proporcionan aplicaciones basadas en microservicios con una sola unidad ideal para la implementación de aplicaciones y entornos de tiempo de ejecución independientes. A su vez, permiten que varias partes de una aplicación se ejecuten de forma independiente en microservicios, en el mismo hardware, con  más control sobre las partes individuales y los ciclos de vida.

Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
    No, ya que al ser aplicaciones grandes se utilizan muchas tecnologías, ya que se tratan como componentes o servicios individuales, para así ser unidas despúes, lo que nos ofrece o permite trabajar con muchas tecnologías.

¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
    La comunicación entre estos servicios se produce a través de protocolos como HTTP, AMQP y TCP. Los protocolos más utilizados son HTTP/REST y los mensajes asíncronos.

¿Los microservicios pueden ser distribuidos? ¿Por qué?
    Si, ños servicios distribuidos, como su nombre  indica, se distribuyen en diferentes máquinas. Un servicio puede ser responsable de varias funciones. Es una arquitectura orientada a SOA. Los servicios también interactúan a través de rpc o un servicio web.

¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
    Son complejos de probar, complejos de implementar y gestionar, complejos de comprender en su conjunto. Por lo tanto, no debe subestimar la creciente complejidad.
    
¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
    Para lograr una alta disponibilidad, es necesario comenzar en el diseño, implementación, operación y mantenimiento, etc., para lograr el objetivo de disponibilidad inmediata. La única arma mágica para la alta disponibilidad es la redundancia, es decir, para evitar la falla de un solo punto, se agregarán uno o más puntos, y es mejor colocarlos en diferentes ubicaciones físicas para reducir la probabilidad de múltiples puntos de falla.