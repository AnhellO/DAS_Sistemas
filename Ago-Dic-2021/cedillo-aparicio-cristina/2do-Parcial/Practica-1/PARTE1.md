# Parte 1

  * ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
     el de microservicios es más fácil de trabajar, porqué es más ágil y flexible

  * ¿En qué consiste el patrón de arquitectura monolítica?
     consiste en que los componentes de la aplicación funcionan en conjunto

  * ¿Cuáles son las principales desventajas de una arquitectura monolítica?
     Solo se puede utilizar un lenguaje de programación
     No se pueden reutilizar los componentes en otras aplicaciones
     Si se hace un cambio a la aplicación, toda debe ser desplegada de nuevo para que vuelva a funcionar
     Es dificíl de hacer tests
     
  * ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
      Se tiene que agregar la nueva funcionalidad a todas las réplicas de la aplicación
     
  * ¿Qué sucede si falla una aplicación monolítica?
     Toda la aplicación falla

  * ¿En qué consiste el patrón de arquitectura basada en microservicios?
     consiste en dividir una aplicación del backend en múltiples partes que se comunican por separado, estas partes se pueden comunicar entre sí y cada una tiene una diferente función

  * ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
     Cada servicio es independiente, esto permite que cada uno se adapte a las necesidades y mantener su disponibilidad sin afectar a los demás

  * ¿Qué es un ambiente basado en contenedores?
     Son los servicios implmentados en contenedores, estos se comunican entre sí a través de API
     
  * Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
     No, se pueden utilizar diferentes lenguajes de programación y bases de datos ya que los servicios se caracterizan por el servicio que ofrecen, la entrada y salida de información

  * ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
      Mediante protocolos de la red

  * ¿Los microservicios pueden ser distribuidos? ¿Por qué?
     Sí, porqué se organizan por diferentes servicios 
     
  * ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
     Se deben hacer pruebas a cada parte
     La comunicación de los servicios y la seguridad dependen de la red
     Convertir y procesar de manera correcta los datos que se obtienen, ya que se tienen que recibir y compartirlos para las diferentes tecnologías que se utlizan 
     Utilizar herramientas para poder monitorizar cada parte

  * ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
     Realizando las pruebas necesarias para verificar que todo este funcionando correctamente

