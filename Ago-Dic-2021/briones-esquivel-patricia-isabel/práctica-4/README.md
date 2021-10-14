## Sintesis sobre Mediator

Mediator promueve el acoplamiento suelto al evitar que los objetos se refieran entre sí explícitamente, y le permite variar su interacción de forma independiente.  <br>
El patrón restringe las comunicaciones directas entre los objetos, forzándolos a colaborar únicamente a través de un objeto mediador.

## Descripción del ejemplo implementado

### Problema

Bob tiene una casa automática, gracias a la buena gente de HouseOfTheFuture. Todos sus electrodomésticos están diseñados para hacerle la vida más fácil.  
- Cuando Bob apaga su alarma, su despertador le dice a la cafetera que comience a preparar.  <br>
Aunque la vida es buena para Bob, él y otros clientes siempre están pidiendo muchas características nuevas:
- No hay café los fines de semana.
- Configura la alarma temprano en los días de basura.

### Solución

- Creamos las clases independientes de los electrodomésticos.
- Creamos la clase Mediator.
- Manejamos la relación entre los electrodomésticos directamente con el Mediator.

### ¿Por qué?

Hay eventos en los que se relacionan más de dos electrodomésticos, para no crear un conflico entre clases y para que se facilite el manejo de estas al mismo tiempo, los relacionamos a tráves del Mediador.  <br>
Por ejemplo:  <br>
- *Cuando Bob apaga su alarma, su despertador le dice a la cafetera que comience a preparar.*  <br>
En este caso:

    1. Bob apaga la alarma.
    2. El despertador manda señal al mediador de que la alarma ha sido apagada.
    3. El mediador llama al calendario.
    4. El calendario regresa el día de la semana.
    5. Si el dia está en rango Lunes-Jueves el mediador  llama a la cafetera.
    6. La cafetera prepara café.

En este caso se involucran 3 electrodomésticos, que bien podrían ser más, pero este patrón evita que interactúen directamente entre ellos, y en cambio manda los cambios al mediador, haciendo más fácil su  comunicación.

## Diagrama UML del ejemplo implementado 

![Diagrama UML HouseOfTheFuture](/DAS_Sistemas/Ago-Dic-2021/briones-esquivel-patricia-isabel/práctica-4/images/DiagramaUML.jpeg "Diagrama UML del ejemplo implementado")

## Recursos 

Information about Mediator: *[Refactoring Guru](https://refactoring.guru/es/design-patterns/mediator)*.  <br>
Information about Mediator: *[Source Making](https://sourcemaking.com/design_patterns/mediator)*.  <br>
Example about Mediator: *[Head First Design Patterns](https://uadecedu.sharepoint.com/sites/DiseoyArquitecturadeSoftware/Class%20Materials/Books/head_first_design_patterns.pdf?CT=1634048019024&OR=ItemsView)*.  <br>