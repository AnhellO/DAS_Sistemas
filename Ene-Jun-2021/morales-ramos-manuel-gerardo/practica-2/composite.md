# Patrón de diseño Composite

El patrón de diseño Composite consiste en trabajar con objetos que, si a su vez tienen sub-objetos, trabajar con estos hasta llegar al último sub-objeto para después retornar
algo en concreto.


En la página [refactoring.guru][referencia] menciona un ejemplo de cómo sería la forma de cálcular el costo total de unos objetos suponiendo que estos estén dentro de cajas y, a su vez, hayan más cajas con productos dentro. Es la analogía perfecta para entender cómo funciona el patrón de diseño, pues nos menciona que:

~~~
Para una caja, recorre un cada artículo. Si uno de estos artículos fuera una caja más pequeña, en esa caja también se empezaría a repasar su contenido y así sucesivamente, hasta que se calcule el precio total de todos los componentes internos de la caja padre.
~~~

[referencia]: https://refactoring.guru/es/design-patterns/composite