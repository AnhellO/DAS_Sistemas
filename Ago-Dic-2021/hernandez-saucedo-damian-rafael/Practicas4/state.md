# State

**También llamado: Estado** state es un patrón de diseño de comportamiento que permite a un objeto alterar su comportamiento cuando su estado interno cambia. Parece como si el objeto cambiara su clase.

El patrón State está estrechamente relacionado con el concepto de la Máquina de estados finitos.

El patrón State sugiere que crees nuevas clases para todos los estados posibles de un objeto y extraigas todos los comportamientos específicos del estado para colocarlos dentro de esas clases.

# Estructura

- **clase Contexto** La clase Contexto almacena una referencia a uno de los objetos de estado concreto y le delega todo el trabajo específico del estado. El contexto se comunica con el objeto de estado a través de la interfaz de estado. El contexto expone un modificador (setter) para pasarle un nuevo objeto de estado.
- **interfaz Estado** La interfaz Estado declara los métodos específicos del estado. Estos métodos deben tener sentido para todos los estados concretos, porque no querrás que uno de tus estados tenga métodos inútiles que nunca son invocados.
- **Estados Concretos ** Los Estados Concretos proporcionan sus propias implementaciones para los métodos específicos del estado. Para evitar la duplicación de código similar a través de varios estados, puedes incluir clases abstractas intermedias que encapsulen algún comportamiento común.
-Tanto el estado de contexto como el concreto pueden establecer el nuevo estado del contexto y realizar la transición de estado sustituyendo el objeto de estado vinculado al contexto.
___

## Problema ##

Implementar una simulación de un sistema utilizando STATE, donde se explique y
realise los siguientes objetivos.

## Objetivo ##
-adquirir más conocimientos sobre los patrones de diseño
-Desarrollar un patrón de diseño desde cero siguiendo las metodologías vistas en clase
-Mejorar en el aprendizaje y en el conocimiento sobre Python
-Mejorar en el aprendizaje y en el conocimiento sobre T.D.D.
-Poner en práctica la técnica de Red-Green-Refactor aprendida en clase
___

![UML state](uml.png)
___
## Recursos de estudio ##
Los recursos se estudiaron de la pagina recomendada [Refactoring Guru](https://refactoring.guru/es/design-patterns/state)
y lo que se vio en clase MS Teams

