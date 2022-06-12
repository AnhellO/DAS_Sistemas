# Respuesta
¿Qué busca solucionar esta arquitectura?
Bueno en primer lugar genera un lenguaje ubicio, bueno lo que busca es que todos
entiendan el mismo lenguaje pues estan hablando del mismo termino.
¿Qué es la "regla de dependencia" o "dependency rule"?
La regla dice que la arquitectura no depende de la existencia de alguna
biblioteca de software, bueno es decir no import el lenguje de programación que
estemos utlizando se pueden aplicar estos principios.
¿Qué abarca la capa de Entidades o Entities?
Son las que encapsulan las reglas más generales y de alto nivel, 
son las menos propensas a cambiar cuando algo externo cambia
¿Qué abarca la capa de Casos de Uso o Use Cases?
Esta abarca las reglas comerciales especificas de la aplicación y encapsula
e implementa todos los casos de uso del sistema y no se espera que los cambios en 
esta capa afecten a las identidades.
¿Qué abarca la capa de Adaptadores o Interface Adapters?
Esta capa abarca poseer los controladores, presentadores y puntos
de entrada.
¿Qué abarca la capa de Frameworks o Frameworks and Drivers?
En la capa más externa  donde van los detalles. Y la base de datos es un detalle, nuestro framework web, es un detalle etc.
¿Puede haber más de 4 capas? Complementa tu respuesta explicando tu razonamiento
¿Qué son los "boundaries"?
es una separación que definimos en nuestra arquitectura para dividir componentes y definir dependencias.