# Práctica 1
___
**Objetivos** 
- **Expandir el conocimiento teórico sobre el tema de arquitectura de software**
- **Conocer casos de uso reales de las arquitecturas de software más utilizadas**
- **Revisar múltiples recursos para aprender sobre el uso de los diferentes patrones de arquitectura de software**
___
# Especificaciones

**Contestar a las siguientes preguntas en un archivo .md (Markdown) por separado**

- **¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?**
La tendencia actual en el desarrollo de software adopta la cultura DevOps y el uso de contenedores, haciendo necesario construir una aplicación de forma distribuida, permitiendo que los distintos componentes puedan ser desplegados de forma independiente. 
por lo visto anterior podemos decir lo siguiente: podemos destacar que los servicios de tipo monolitico cabe destacar su eficiencia y ofrece poco margen de fallo.pero su mayor ventaja es tambien su mayor desventaja por su entorno que es muy rigido que es muy dificil actualizar por eso se opto por los microservicios por el entorno en el cada elemento es independiente.

- **¿En qué consiste el patrón de arquitectura monolítica?**
Puede decirse que la arquitectura monolitica es aquella en la que el software se estructura de forma que todos los aspectos funcionales del mismo quedan acoplados y sujetos en un mismo programa.

- **¿Cuáles son las principales desventajas de una arquitectura monolítica?**
Los problemas de este tipo de arquitectura, como la escalabilidad o la dificultad para los desarrolladores (necesitan entender todo el código de la aplicación).

- **¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?**
implica que utilisimos el mismo Stack tecnologico para absolutamente todo, lo que impide que aprovechemos todas las tecnologias disponibles.

- **¿Qué sucede si falla una aplicación monolítica?**
A menos que tengamos alta disponibilidad, si la aplicación Monolítica falla, falla todo el sistema, quedando totalmente inoperable.

- **¿En qué consiste el patrón de arquitectura basada en microservicios?**
Una arquitectura de microservicio es un método para desarrollar aplicaciones de software que operan como un grupo de microservicios que operan de forma independiente e independiente, proporcionando una funcionalidad empresarial completa. En él, cada microservicio es un código que puede estar en un lenguaje de programación diferente y realizar una función específica. Los microservicios se comunican entre sí a través de API y tienen su propio sistema de almacenamiento en caché que evita la sobrecarga y los bloqueos de las aplicaciones.

- **¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?**
se pueden desarrollar y desplegar de forma independiente. Además un error en un servicio no debería afectar la capacidad de otros servicios para seguir trabajando según lo previsto.

- **¿Qué es un ambiente basado en contenedores?**
Brindan a las aplicaciones basadas en microservicios una unidad ideal de implementación de aplicaciones y un entorno de ejecución autónomo. Esto le permite aprovechar mejor el hardware y coordinar los servicios con facilidad, lo que incluye el almacenamiento, las redes y la seguridad.

- **Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?**
cada microservicio es un código que puede estar en un lenguaje de programación diferente, y que desempeña una función específica.
es la ventaja que nos da se puede trabajar en diferentes lenguajes no esta sujeto a uno exclusivo.

- **¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?**
En una arquitectura de microservicios, cada microservicio posee una tarea sencilla y se comunica con los clientes o con otros microservicios mediante mecanismos de comunicación ligeros, como las solicitudes de API de REST.
La capa API es el punto de entrada para todas las solicitudes de cliente a un microservicio. La capa API también permite a los microservicios comunicarse entre sí a través de HTTP, gRPC y TCP/UDP.

- **¿Los microservicios pueden ser distribuidos? ¿Por qué?**
Sí: - Debido a la distribución de los componentes de la aplicación, las pruebas y las pruebas globales son más complejas de implementar.

- **¿Cuáles son los principales desafios de una arquitectura basada en microservicios?**
Pruebas: las pruebas de integración, así como las pruebas finales, pueden tornarse más complejas e importantes que nunca. Tenga en cuenta que una falla en una parte de la arquitectura puede producir un verdadero error, y esto depende de la manera en que haya diseñado la arquitectura de sus servicios para que sean compatibles entre sí.

Control de versiones: cuando actualice sus sistemas a las nuevas versiones, tenga en cuenta que corre el riesgo de anular la compatibilidad con las versiones anteriores. Se puede diseñar en función de una lógica condicional para manejar este problema, pero se torna una tarea engorrosa y desagradable. Otra opción es implementar múltiples versiones en vivo para distintos clientes, pero esto puede ser más complejo durante el mantenimiento y la gestión.

Registro: con los sistemas distribuidos, se necesitan registros centralizados para integrar todos los elementos. De lo contrario, es imposible controlar la expansión.

Depuración: la depuración remota no es opción y no funcionará en decenas ni cientos de servicios. Desgraciadamente, no hay una única respuesta sobre cómo realizar la depuración en este momento.

- **Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?**
Dado que las aplicaciones grandes se dividen en partes más pequeñas, es más fácil para los desarrolladores comprender, actualizar y mejorar estas partes; De esta manera, obtiene ciclos de desarrollo más rápidos, especialmente cuando se combina con métodos de desarrollo ágiles.
