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

El desarrollo de software empezó utilizando una arquitectura monolítica que agrupaba todas sus funciones y servicios dentro de una base única y centralizada de código.
Este tipo de arquitectura ha ido quedando desfasada, sobre todo al crecer los proyectos en complejidad, número de desarrolladores, usuarios y cargas de trabajo. Por eso en la actualidad se tiende a utilizar una estructura basada en microservicios, que es escalable y facilita el trabajo colaborativo de los desarrolladores.
La tendencia actual en el desarrollo de software adopta la cultura DevOps y el uso de contenedores, haciendo necesario construir una aplicación de forma distribuida, permitiendo que los distintos componentes puedan ser desplegados de forma independiente. 
por lo visto anterior podemos decir lo siguiente: podemos destacar que los servicios de tipo monolitico cabe destacar su eficiencia y ofrece poco margen de fallo.pero su mayor ventaja es tambien su mayor desventaja por su entorno que es muy rigido que es muy dificil actualizar por eso se opto por los microservicios por el entorno en el cada elemento es independiente.

- **¿En qué consiste el patrón de arquitectura monolítica?**
De forma resumida.Puede decirse que la arquitectura monolitica es aquella en la que el software se estructura de forma que todos los aspectos funcionales del mismo quedan acoplados y sujetos en un mismo programa.

- **¿Cuáles son las principales desventajas de una arquitectura monolítica?**
Los problemas de este tipo de arquitectura, como la escalabilidad o la dificultad para los desarrolladores (necesitan entender todo el código de la aplicación) han hecho que este tipo de desarrollo de software deje de ser utilizado en muchos proyectos (aunque su sencillez y bajo coste hace que siga siendo interesante para ciertos proyectos con bajos requerimientos).

- **¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?**
Debido a que todo el software es solo una pieza, implica que utilisimos el mismo Stack tecnologico para absolutamente todo, lo que impide que aprovechemos todas las tecnologias disponibles.

Cualquier minimo cambio en la aplicacion implicara realizar una compilacion de todo el artefacto y con ello una nueva version que tendra que ser administrada.

- **¿Qué sucede si falla una aplicación monolítica?**
A menos que tengamos alta disponibilidad, si la aplicación Monolítica falla, falla todo el sistema, quedando totalmente inoperable.

- **¿En qué consiste el patrón de arquitectura basada en microservicios?**
La arquitectura de microservicios es un método de desarrollo de aplicaciones software que funciona como un conjunto de pequeños servicios que se ejecutan de manera independiente y autónoma, proporcionando una funcionalidad de negocio completa. En ella, cada microservicio es un código que puede estar en un lenguaje de programación diferente, y que desempeña una función específica. Los microservicios se comunican entre sí a través de APIs, y cuentan con sistemas de almacenamiento propios, lo que evita la sobrecarga y caída de la aplicación.

- **¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?**
al tratarse de servicios autónomos, se pueden desarrollar y desplegar de forma independiente. Además un error en un servicio no debería afectar la capacidad de otros servicios para seguir trabajando según lo previsto.

- **¿Qué es un ambiente basado en contenedores?**
Brindan a las aplicaciones basadas en microservicios una unidad ideal de implementación de aplicaciones y un entorno de ejecución autónomo. Esto le permite aprovechar mejor el hardware y coordinar los servicios con facilidad, lo que incluye el almacenamiento, las redes y la seguridad.

- **Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?**
cada microservicio es un código que puede estar en un lenguaje de programación diferente, y que desempeña una función específica.
es la ventaja que nos da se puede trabajar en diferentes lenguajes no esta sujeto a uno exclusivo.

- **¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?**
En una arquitectura de microservicios, cada microservicio posee una tarea sencilla y se comunica con los clientes o con otros microservicios mediante mecanismos de comunicación ligeros, como las solicitudes de API de REST.
La capa API es el punto de entrada para todas las solicitudes de cliente a un microservicio. La capa API también permite a los microservicios comunicarse entre sí a través de HTTP, gRPC y TCP/UDP.

- **¿Los microservicios pueden ser distribuidos? ¿Por qué?**
si:- debido a que los componentes de la aplicación están distribuidos, las pruebas y test globales son más complicados de realizar.

- **¿Cuáles son los principales desafios de una arquitectura basada en microservicios?**
Diseño: debe invertir tiempo en identificar las dependencias entre los servicios. Y debe estar atento, porque cuando se termina un diseño, puede surgir la necesidad de muchos otros debido a esas dependencias. También debe considerar los efectos de los microservicios en sus datos.

Pruebas: las pruebas de integración, así como las pruebas finales, pueden tornarse más complejas e importantes que nunca. Tenga en cuenta que una falla en una parte de la arquitectura puede producir un verdadero error, y esto depende de la manera en que haya diseñado la arquitectura de sus servicios para que sean compatibles entre sí.

Registro: con los sistemas distribuidos, se necesitan registros centralizados para integrar todos los elementos. De lo contrario, es imposible controlar la expansión.

Depuración: la depuración remota no es opción y no funcionará en decenas ni cientos de servicios. Desgraciadamente, no hay una única respuesta sobre cómo realizar la depuración en este momento.

- **Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?**
Dado que las aplicaciones más grandes se desglosan en piezas más pequeñas, los desarrolladores pueden comprender, actualizar y mejorar más fácilmente esas piezas; de esta manera, se obtienen ciclos de desarrollo más rápidos, especialmente cuando se combinan con metodologías de desarrollo ágiles.

