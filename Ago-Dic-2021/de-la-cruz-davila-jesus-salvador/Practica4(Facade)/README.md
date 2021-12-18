<b>#Sintésis de lo comprendidp en clase</b>

#Patrón de Diseño Facade
##¿Qué es?
####Es un tipo de patrón de diseño estructural. Este viene motivado por la necesidad de estructurar un entorno de programación y reducir su complejidad, dividiendolo en subsistemas y asi minimizando las comunicaciones y dependencias entre los metodos.

####Este patron conciste en un objeto fachada central que:
* Implementa una interfaz para interfaces del subsistema o subsistemas.
* Puede realizar funciones adicionales antes o después de reenviar una solicitud al cliente.

##Ventajas
* La fachada oculta los subsistemas de software y asi reduce la complejidad de estos sistemas.
* Los cambios(modificaciones, mantenimiento) son vonvenientes y posibles en cualquier momento.
* Un subsistema es mas fácil de expandir.

##Desventajas
* La implementación de una fachada es una tarea tediosa y complicada, especialmente si es en algun codigo ya existente.
* Presenta el riesgo de que el software se vuelva demasiado dependiente de la interfaz central.

#Diagrama UML
<p>El diagrama UML esta dentro de la carpeta Practica4(Facade) y se llama <b>Diagrama_UML(Facade)</b></a></p>

#Implementación de mi ejemplo y recursos de los cuales me base
<p>El ejemplo que lleve a cabo fue la implementacion de una lavanderia, al principio no tenia una idea de que es lo que se podia implementar con este patron, pero, investigando en distintos foros tuve la idea de llevarlo a cabo de esta manera.
Primero tenia que saber cual seria mi fachada y al final llegue a la conclución de que la fachada, como su nombre lo dice, solo es lo de afuera, lo que aparenta ser, lo que la gente ve, y por eso mi fachada lleva el nombre de <em><b>"LavanderiaFachada"</b></em>, ya que llegue a la conclusión que la fachada puede ser el nombre que se le da a cierto lugar, por ejemplo, una fabrica, la fachada seria como tal el lugar, "Fabrica".
Después de esto, me pase a los subsistemas, que estos vendrian siendo las acciones que realiza ese lugar, como por ejemplo en el que realice seria <em><b>"Lavado", "Enjuague"</b></em>, entre otros. Asi que son las cosas que puede realizar dentro de ese lugar.
Y por ultimo, esta el cliente, que es el que pide las cosas, en este caso viene siendo el metodo <b>main</b>, pero puede implementarse de distintas maneras, no solo que este sea el cliente.<br><br>
Para llevar a cabo este ejemplo, investigue en distintos foros, incluyendo el visto en clase <a href = "https://refactoring.guru/es/design-patterns/facade"><b>Refactoring guru</b></a>, de ahi puede sacar alguna informacion para saber como funcionaba este metodo. Al igual, tambien revise el ejemplo que esta en el repositorio llamado <a href = "https://github.com/AnhellO/td-design-patterns/tree/development/structural/python/facade"><b>td-design-patterns</b></a>, el cual fue de mucha ayuda, ya que, revisandolo y viendo de nuevo las clases en Teams, me fue mas facil poder entender, de una manera mejor, este patron de diseño, y no solo este patron, si no todos los vistos en clase. Tambien, revisé muchas mas paginas e incluso videos para realizar este ejemplo, como este <a href = "https://www.youtube.com/watch?v=w5Mvs6UbPzU&t=24s"><b>video</b></a>,pero al final, solo era para saber hacia que orientar el ejemplo.<br>
Para esto, hice un diccionario con las prendas que podian ingresar a la lavanderia, cada una tiene un determinado tiempo que tarda en poder realizarsele el servicio que quiera escoger, en este caso solo son 3 servicio, el lavado, enjuagad y secado. Para los test, se hicieron distintos de estos, como por ejemplo si un cliente pide solo un servicio para una prenda, si pide todos los ervicios para una prenda o tambien si no pide ningun servicio, entre otros.<br>
Quice hacerlo sobre una lavanderia ya que parecia una forma sencilla de ejemplificar este ejercicio y de esta manera, fuera facil de entender. Al final, creo que lo mas complicado fue el pensar los test que se harian, aunque deberia de haber sido el por donde empezar, al fin y al cabo tambien se utilizo la metodologia <b>"Red-Green-Refactor"</b>, a prueba y error.

