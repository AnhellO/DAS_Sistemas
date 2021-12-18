
ARQUITECTURA MONOLÍTICA 

La arquitectura monolítica se considera una forma tradicional de construcción de aplicaciones. Una aplicación monolítica se construye como una unidad única e indivisible. Normalmente, dicha solución comprende una interfaz de usuario del lado del cliente, una aplicación del lado del servidor y una base de datos. Está unificado y todas las funciones se gestionan y sirven en un solo lugar. 
Normalmente, las aplicaciones monolíticas tienen una gran base de código y carecen de modularidad. 

ARQUITECTURA DE MICROSERVICIOS 

Mientras que una aplicación monolítica es una sola unidad unificada, una arquitectura de microservicios la divide en una colección de unidades independientes más pequeñas. 

Beneficios clave de una arquitectura de microservicios

Como los servicios constituyentes son pequeños, pueden ser construidos por uno o más equipos pequeños desde el principio separados por límites de servicio, lo que facilita la ampliación del esfuerzo de desarrollo si es necesario. 
Una vez desarrollados, estos servicios también se pueden implementar de forma independiente entre sí y, por lo tanto, es fácil identificar los servicios activos y escalarlos independientemente de toda la aplicación. Los microservicios también ofrecen un mejor aislamiento de fallas, por lo que en el caso de un error en un servicio, la aplicación completa no necesariamente deja de funcionar. Cuando se soluciona el error, se puede implementar solo para el servicio respectivo en lugar de volver a implementar una aplicación completa.
Otra ventaja que aporta una arquitectura de microservicios es facilitar la elección de la pila de tecnología que mejor se adapte a la funcionalidad requerida en lugar de tener que adoptar un enfoque más estandarizado y único para todos. 


Consideraciones al decidir Monolith vs Microservices 

Antes de sumergirnos en las consideraciones mismas, vale la pena detenerse un momento y comprender qué implica realmente la eficacia de un equipo. Si bien la idea ostensible de agregar más personas a los equipos existentes puede parecer bastante razonable para ayudar a escalar la eficiencia general, sin embargo, hay pruebas bastante sólidas en la industria de que agregar más personas no significa realmente que los proyectos se entregarán más rápido. . 


Despliegue

Las aplicaciones Monolith le permiten configurar su implementación una vez y luego simplemente ajustarla en función de los cambios en curso. 

Mantenimiento 

Si se planea utilizar una arquitectura de microservicios, obtenga un DevOps para su equipo y prepárese. 

La arquitectura de microservicios de confiabilidad es el ganador obvio aquí. 

Escalabilidad 

Para la escalabilidad, los microservicios son nuevamente más adecuados. 

Costo 

El costo es complicado de calcular porque la arquitectura monolítica es más barata en algunos escenarios, pero no en otros. 

Desarrollo 

La mejor manera de lidiar con los microservicios es compilar su archivo docker-compose desde el principio y desarrollarlo a través de Docker. 

Despliegue

Los microservicios que son más pequeños y con una arquitectura adecuada de comunicación de microservicios le permiten lanzar nuevas funciones más rápidamente al reducir el tiempo de control de calidad, el tiempo de compilación y el tiempo de ejecución de pruebas. 

¿Qué arquitectura es mejor? 

Es mejor la arquitectura monolítica si: 
Se tiene un equipo pequeño.
No se generan los suficientes recursos para un equipo DevOps.


Puede ser tentador adoptar microservicios solo porque ahora es una palabra de moda. 
Sin embargo, cuando se trata de migrar grandes aplicaciones monolíticas a una arquitectura de microservicios y una cultura DevOps / DevSecOps, lo ideal es que exista integración continua y entrega continua.
Hacer cumplir la compatibilidad con versiones anteriores: si otros equipos u organizaciones van a depender de sus microservicios, la API debe pensarse cuidadosamente para que sea fácil de usar, para empezar, la compatibilidad con versiones y versiones anteriores se debe mantener estrictamente. 


Es un viaje dividido verticalmente en lugar de horizontalmente, lo que significa que implicaría un esfuerzo tanto de backend como de frontend en lugar de ser solo un esfuerzo de front-end o solo de backend Este viaje de un extremo a otro podría dividirse en varias historias de usuarios repartidas en varios sprints si necesario. Forme un equipo multifuncional ágil. Ahora podemos hacer que nuestro equipo nuevo o existente comience a desarrollar el recorrido del cliente seleccionado. 
Lo que va a ser muy importante aquí es contar con estrictas pruebas automatizadas y, como empresa, permitirle a su equipo el tiempo necesario para escribir estas pruebas desde el principio. 

Hemos seleccionado uno o algunos viajes de clientes de nuestro monolito y ahora estamos listos para transmitirlos a los clientes como microservicios. También puede haber una aplicación de front-end separada o actualizada que se vincule a estos nuevos microservicios que también pueden tener que estar disponibles. 
Será importante asegurarse de tener una forma de volver a una versión anterior y / o poder volver al viaje monolítico en caso de que las cosas salgan mal.
Muchas empresas que veo intentan jugar con el aprovisionamiento de servidores manualmente y tratando de calcular la carga que recibirían. 
En su lugar, recomiendo simplemente tener en cuenta la prima de usar un servicio en la nube como AWS, Azure o GCP para comenzar a funcionar al instante y tener acceso a capacidades cruciales de escalado automático y autorreparación. 

Este microservicio se comunica solo a través de SOAP,.


¿Y si la cola se hace grande? 

Cada pregunta plantea una serie de otras preguntas. 

El monolito es simple 

Nueva construcción. 
Scripts de automatización.
Los microservicios requieren más puntos finales y datos entre servicios. Monolith puede contener muchos servicios web diseñados para realizar funciones comerciales del programa. Pero los microservicios tendrán más de ellos, porque, además de los mismos servicios para realizar funciones comerciales, agregamos más servicios técnicos para conectar microservicios entre sí. Y todo el mundo necesita pruebas. 
Cada servicio web debe transmitir más datos al mismo tiempo porque sucede que el primer microservicio transmite datos al segundo, que usa dos campos condicionales para sus cálculos, y todo el resto de los datos pasa al siguiente servicio al que son útiles. . 


Los microservicios están diseñados para ser pequeños e independientes. Si hay un problema durante la prueba y el equipo no quiere ayudar en la prueba, siempre debe recordarlo.

Enfoque de microservicios 

Cuando hay un sistema grande y complejo que necesita administración de componentes, escalado, desarrollo individual, entonces necesita microservicios. 

¿Cuáles deberían ser las consideraciones de diseño al pensar en microservicios? 

CI / CD: Integración continua y desarrollo continuo es una práctica de desarrollo moderna que fusiona el desarrollo con las pruebas, lo que permite a los desarrolladores crear código en colaboración, enviarlo a la rama maestra y verificar si hay problemas.


/////////////////////////////////////¿Qué respuestas cambiaría de la parte 1?/////////////////////////////////////
Probablemente cambiaría la definición de la arquitectura monolítica, mejor dicho la complementaría, y seguramente los problemas que presenta un monolito al querer agregar una nueva funcionalidad.