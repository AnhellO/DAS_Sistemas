# Práctica 1
___
**Objetivos** 
- **Expandir el conocimiento teórico sobre el tema de arquitectura de software**
- **Conocer casos de uso reales de las arquitecturas de software más utilizadas**
- **Revisar múltiples recursos para aprender sobre el uso de los diferentes patrones de arquitectura de software**
___
# Especificaciones

**Parte 3**

- **Lee, analiza, revisa y procesa el siguiente artículo: https://faun.pub/complete-guide-to-monolithic-vs-microservices-architecture-fe1858c2cfef. Tómate tu tiempo y re-leélo de ser necesario 😉**

- **Elabora una síntesis de lo que aprendiste y entendiste del artículo (síntesis y NO resumen ni copy / paste)**

# Guía completa de arquitectura monolítica vs. microservicios

En este articulo posteriormente veremos sobre la arquitectura monolitica VS microservicios.

Recordemos por lo que hemos visto a lo largo de los articulos y videos que hemos visto nos podemos dar una idea mas amplia de que se trata este tema con abundancia y centrarnos en los puntos mas importantes.

Hablemos un poco de la arquitectura monolitica.
tal cual se entendio es una forma o se considera una forma tradiccional de crear aplicaciones. su interfaz es mejor por lado del cliente.
Todas las funciones se administran y se sirven en un solo lugar.
Por lo regular las aplicaciones monoliticas tienen una gran base de codigo y carecen de modularidad.
lo malo de esto cuando quieren hacer un cambio a la base o codigo tienen que realisar cambio total.
Tal vez esa es una de sus mayores desventajas pero tambien tiene sus fortalezas hablaremos de ellas.
Menos preocupaciones transversales, Depuración y pruebas más sencillas, Fácil de implementar, Fácil de desarrollar,
tal vez algo que podemos destacar es la facilidad que se puede manejar e implementar este servicio pero no ostante en mi pensar es un poco obsoleto y no es eficas para gran cantidades de datos.
Las devilidades que tiene creo yo son muy severas ya que es propenso al fallo continuo.
uno de ellos es al hacer cambios, más difícil implementar cambios en una aplicación tan grande y compleja con un acoplamiento muy ajustado.
el cambio del codigop afecta considerablemente al sistema.
esto es para entender como se conporta este tipo de arquitectura.

Arquitectura de microservicios
Este tipod de arquitectura es mejor a mi pensar claro habra muchos que prefieran el otro tipo de arquitrctura pero eso depende de cada persona a muchos se les puede facilitar el otro tipo de arquitectura mientras que los demas prefieren esta.
Este tipo de arquitectura nos da la confiansa que cada cambio se realisa por aparte sin afectra al resto del sistema podriamos decir que es una actualizacion a cierto punto. y claro cada servicio tiene su propia base de datos. 

una de las mejores ventajas a mi pensar es que puedes desarrollar en diferentes tipos de lenguaje sin interferir con los demas que sean dependientes o exclusivos de uno.
Claro asi como tenemos un amplia ventaja tambien tenemos desventajas.
mientras mas grande la aplicacion mas compleja se ara que queremos decir, que al realisar cambios se volvera cada vez mas dificiles.
ya que tambien tiene que tener diferentes tipos de recursos, su estabilidad debido a que todos los módulos se ejecutan en el mismo proceso, un error en cualquier módulo potencialmente descompone todo el proceso. 

Tal vez al escoger con que tipo de arquitectura trabajaremos debemos pensar 2 minutos para que la quiero, cuales son mis intereses, que tipo de negocio o infrastructura quiero tener son detalles que a largo plazo afectan.

El mantenimiento que llva acabo recuerda que todos no estan familiarizados con DOCKER.
lguien tiene que supervisar y mantener el estado de funcionamiento de su configuración de CI para cada microservicio y toda la infraestructura.

La confiansa aqui sin dudas el mejor es microservicios La ruptura de un microservicio afecta solo a una parte y causa problemas a los clientes que lo usan, pero a nadie más. 

Vaya podemos decir que los servicios de microservicios es mejor con lo que hemos visto pero recordemos que muchos prefieren otras alternativas y es valido al final de cada quien uno escoge lo que se facilite mas.

- **Re-visita las respuestas que proporcionaste a las preguntas de la 1era parte de esta práctica: ¿Qué respuestas cambiarías?**

para mi pensar seria ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
Aqui van ms razones y creo la mas importante. Depende de cada quien como este familiarizado con estos tipos de arquitectura para unos es megor los monoliticos y para otros microservicios y aqui no hay ventaja cada quien tiene sus propias ventajas sobre esta arquitectura






