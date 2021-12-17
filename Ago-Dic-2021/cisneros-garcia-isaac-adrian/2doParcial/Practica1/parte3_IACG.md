#Parte 3 IsaacElCrack

**_Prácticamente el artículo es un amplio texto, donde se expresan las diferencias entre la arquitectura monolítica y la de microservicios, la más grande dificultad de realizar esta síntesis en que: “I don't speak English” entonces, muchas palabras van a cambiar y/o perder el sentido, debido al traductor de Google, sin mas que agregar, gracias por su atención_**

_Arquitectura Monolítica_

En una aplicación monolítica, esta área de la funcionalidad concierne solo a una aplicación, por lo cual es más simple de manejar. 

Continuamente que el enfoque monolítico sea una forma estándar de producir aplicaciones, cualquier equipo de ingeniería tiene los conocimientos y las habilidades adecuados para desarrollar una aplicación monolítica. 

- Debilidades de la arquitectura monolítica

Es más complejo llevar a cabo cambios en una aplicación tan enorme y compleja con un acoplamiento bastante ajustado. 

Es drásticamente problemático utilizar nueva tecnología en una aplicación monolítica pues entonces toda la aplicación tiene que ser reescrita. 

_Arquitectura de microservicios_

Una arquitectura de microservicios toma este mismo enfoque y lo alarga a los servicios acoplados libremente que tienen la posibilidad de desarrollar, llevar a cabo y conservar de manera sin dependencia. Todos dichos servicios es responsable de labores discretas y puede comunicarse con otros servicios por medio de API primordiales para solucionar un problema comercial complejo más enorme. 

- Beneficios clave de una arquitectura de microservicios 

Una vez desarrollados, dichos servicios además tienen la posibilidad de llevar a cabo de manera libre entre sí y, por consiguiente, es simple detectar los servicios calientes y escalarlos independientemente de toda la aplicación. Una vez que se soluciona el error, se puede llevar a cabo solo para el servicio respectivo en vez de volver a llevar a cabo una aplicación completa. 

- Puntos fuertes de la arquitectura de microservicios 

Cualquier fracaso en una aplicación de microservicios perjudica solo a un servicio en especial y no a la solución completa. 

En segundo sitio, un error en un microservicio tiene un efecto solo en un servicio en especial y no perjudica a toda la aplicación. 

- Debilidades de la arquitectura de microservicios 

Aplicaciones enormes y complicadas: si tiene una aplicación enorme, incrementará la medida de la aplicación y va a ser bastante complejo y difícil hacer cambios en dicha aplicación. 

Desarrollo lento: mientras su aplicación y los accesorios respectivo crecen, la aplicación es complicado de comprender y cambiar. 

_Pros y Contras_

- Despliegue 

No obstante, hay un lado positivo; si algo sale mal, solo romperá un diminuto microservicio, que es menos problemático que todo el plan. Además es muchísimo más simple revertir un microservicio diminuto que una aplicación monolítica completa. 

- Mantenimiento 

No todos los desarrolladores estarán familiarizados con Docker o con los instrumentos de orquestación, como Kubernetes, Docker Swarm, Mesosphere o cualquier herramienta parecida que logre ayudarlo a regir la infraestructura con muchas piezas móviles. Alguien tiene que monitorear y conservar el estado de manejo de su configuración de CI para cada microservicio y toda la infraestructura. 

- Fiabilidad 

Romper un microservicio perjudica solo a una sección y causa inconvenientes a los consumidores que lo utilizan, sin embargo a nadie más. Si, ejemplificando, está construyendo una aplicación bancaria y el microservicio responsable del retiro de dinero no funciona, esto de manera definitiva es menos grave que toda la aplicación que se ve obligada a detenerse. 

- Escalabilidad 

Las aplicaciones Monolito son difíciles de escalar ya que, inclusive si hacen más trabajadores, todos los trabajadores estarán en el plan completo y exclusivo, una forma ineficiente de utilizar los recursos. Los recursos tienen la posibilidad de utilizar con más cuidado y le permiten escalar solo las piezas que necesitan más recursos. 

- Costo 

Con una pequeña aplicación monolito, se puede llevar a cabo en un host de $ 5 a $ 20 y activarla rápido. Con una aplicación monolito más enorme, puede alojar una instancia bastante cara ya que no puede compartirla entre diversos hosts pequeños y baratos

- Desarrollo 

La mejor forma de lidiar con los microservicios es compilar su documento docker-compose a partir de el inicio y desarrollarlo por medio de Docker. 

- Soltando 

Los microservicios que son más pequeños y con una arquitectura idónea de comunicación de microservicios le permiten arrojar novedosas funcionalidades más inmediatamente al minimizar la era de control de calidad, la era de compilación y la época de ejecución de pruebas. 

_Conclusión_

Y bueno, después de todo lo anterior mencionado, aún así creo que la arquitectura por microservicios es muy superior a la monolito(jajaja se escucha como manolito), y claro que no es perfecta, tiene sus fallas, pero aún así presenta mejores características y matengo firmemente mi decisión y no cambio ninguna respuesta
Saludos 😊
