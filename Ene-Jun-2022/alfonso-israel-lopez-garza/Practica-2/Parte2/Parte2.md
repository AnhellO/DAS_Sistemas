# Preguntas
1.- ¿Qué busca solucionar esta arquitectura?
R = 
2.- ¿Qué es la "regla de dependencia" o "dependency rule"?
R = De  afuera hacia dentro por ejemplo infraestructura a aplicacion y de aplicacion a dominio. Mientras mas avance, mayor el nivel del software.
3.- ¿Qué abarca la capa de Entidades o Entities?
R = Encapsulan las reglas comerciales de toda la empresa.
4.- ¿Qué abarca la capa de Casos de Uso o Use Cases?
R = Contiene las reglas comerciales especificas de la aplicacion. Encapsula e implementa todos los casos de uso del sistema.
5.- ¿Qué abarca la capa de Adaptadores o Interface Adapters?
R = Es el conjunto de adaptadores que convierten datos del formato más conveniente para los casos de uso y entidades, al formato más conveniente para alguna agencia externa como la base de datos o la web.
6.- ¿Qué abarca la capa de Frameworks o Frameworks and Drivers?
R = Se compone por frameworks y herramientas como la base de datos, marco web, etc. En esta capa van todos los detalles.
7.- ¿Puede haber más de 4 capas? Complementa tu respuesta explicando tu razonamiento
R = Si, porque segun lo que estamos desarrollando podemos descubrir que necesitamos mas de 4.
8.- ¿Qué son los "boundaries"?
R = Muestra a los controladores y presentadores comunicándose con los casos de uso en la siguiente capa.Por ejemplo, considere que el caso de uso necesita llamar al presentador. Sin embargo, esta llamada no debe ser directa porque violaría la regla de dependencia : ningún nombre en un círculo externo puede ser mencionado por un círculo interno. Así que tenemos el caso de uso llamando a una interfaz (que se muestra aquí como puerto de salida de caso de uso) en el círculo interior, y el presentador en el círculo exterior lo implementa.