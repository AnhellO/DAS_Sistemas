----------- Sintésis sobre lo comprendido acerca del patrón de diseño ---------------------------------
A mi me toco el patrón de diseño "Singleton", la verdad que fue un reto escribir el código, ya que 
existe poca información sobre la implementación éste en python, originalmente se útiliza en java
(odio java y java me odia a mí ), pero bueno... no me alargo más. 

El patrón Singleton es:

Es un patrón de diseño utilizado dentro de la programación orientada a objetos que, como su nombre lo 
sugiere, del inglés “single” que significa “único”, trata de diseñar clases que solo puedan ser 
instadas una vez, es decir, que de esa clase, durante toda la ejecución del programa, unicamente podrá
ser creado un objeto. El singleton es útil, por ejemplo, cuando una clase es diseñada para representar
un dispositivo único dentro de un programa: el teclado o el ratón por mencionar algunos, también es 
requerido en diseños de clases que interactúan con todas las demás como un recurso común, algo así 
como una clase de ámbito global. 

¡NOTA!: Debido a sus Atributos, muchos programadores lo consideran un anti-patrón.

---------------------- Descripción del ejemplo implementado --------------------------------------------
Realmente la forma de trabajar con éste patrón, es muy limitada, ya que el "Singleton" es de un solo 
valor; eso me llevo a pensar en una circustancia donde solo pueder uno, unico en su clase, donde no
puede haber otro igual. Así que... decidí implementarlo en la estructura de nuestra hermosa universidad.
Todos pueden hacer la siguiente pregunta: ¿Quien es el jefe?. Podría haber un sin fin de respuestas, pero
al final del dia la respuesta es: "Salvador Hernández Vélez", Rector de la UAdeC. Para evitar confusiones,
el patrón nos da la respuesta sobre quien es el jefe.

---------------------- Recursos -------------------------------------------------------------------------
https://refactoring.guru/es/design-patterns/singleton
https://refactoring.guru/es/design-patterns/singleton/python/example
https://python-patterns.guide/gang-of-four/singleton/
https://codingornot.com/patron-de-diseno-de-software-singleton
https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
https://www.youtube.com/watch?v=Qb4rMvFRLJw&t=131s&ab_channel=NeuralNine
