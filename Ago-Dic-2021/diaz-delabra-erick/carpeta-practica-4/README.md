## Sintésis sobre lo comprendido acerca del patrón de diseño
    Iterator: Iterator es un patrón de diseño que como su nombre lo indica, itera. Este lo que hace es
    recorrer cualquier estrutctura de datos como listas, que son las que usamos en este ejemplo.
    Es muy popular debido a su "facil implementacion" ya que es muy comun que querramos recorrer algúna 
    coleccion que tengamos.
## Descripción del ejemplo implementado, desde el problema hasta la forma de implementar la solución y el por qué
    En este problema tenemos lo que seria varias listas llamadas con el nombre de los queipos de la Formula 1.
    Cada lista con el nombre del equipo tiene dentro 2 valores, los que son el nombre de los 2 pilotos principales
    de cada equipo.
    Primero tenemos la clase iteraciones que es la clase que recibe la lista y la recorre elemento por elemento. 
    Esta clase funciona de la siguiente manera: Itera la lista que le mandamos y guarda sus valores en otra lista (nueva_lista) para despues mandar esta nueva_lista a los casos de prueba y asi comprobar que el recorrido funciono.

    Después tenemos la funcion pilotos, que es la que le asignara que datos tendra la lista principal que vamos a iterar, dependiendo del equipo requerido y seleccionado en los casos de prueba.

    Después tenemos la clase ListPilotos que lo que hace es recibir los valores de la lista para despues mandarlos a la clase que itera.

    Solucion al problema: En si no hay ningun problema solo comprobamos que los valores que requerimos en los casos de prueba son los mismos que tiene la lista.
    Esto seria muy sencillo de hacer si solo evaluamos nuestros valores requeridos con la lista principal pero en este caso estamos evaluando nuestros valores requeridos con una nueva_lista creada a partir de la iteracion de la lista original.

## Diagrama UML del ejemplo implementado

![UML_ITERATOR](DAS_Sistemas\Ago-Dic-2021\diaz-delabra-erick\carpeta-practica-4\UML.png)

## Recursos desde los cuáles estudiaste, investigaste e implementaste el patrón
Videos:
![Video_Iterator_En_Python](https://www.youtube.com/watch?v=RskNd-DfIgM&ab_channel=seanwasereytbe)
![Video2_Iterator_En_Python](https://www.geeksforgeeks.org/iterators-in-python/)
![Video3_Informacion_Patrones_De_Diseño](https://www.youtube.com/watch?v=4pTtTHg-guw&t=41s&ab_channel=nicosiored)
Informacion:
![Iterator_Pattern](https://medium.com/design-patterns-in-python/iterator-design-pattern-54655e97552c)
![Iterator_En_Python](https://refactoring.guru/es/design-patterns/iterator/python/example)

