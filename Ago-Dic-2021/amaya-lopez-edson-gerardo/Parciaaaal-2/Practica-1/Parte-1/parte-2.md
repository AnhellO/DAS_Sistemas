# Parte 2

### ¿Qué lenguaje de programación utiliza el equipo de Netflix?
   - python

### ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
    era que en la base del codigo de java para web era monolitica en el sentido de que todos contribuian a una base de codigo que se implementaba semanalmente el probelma era que cuando se introduco un cambio causo que el album fuera dificil de diagnosticar.

### ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
    que era dificil diagnosticar que fallo, aun sacando fragmento de codigo para revisarlo individualmente, la escabilidad vertical , falta de agilidad

### ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
    Martin Fowler.

### ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
    el dinamismo lo facil que es hacer cambios en el codigo
    el alcance de hacer funcionalidades especificas y de una manera muy simple
### ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
    la analogia donde compara con los organos
### Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
   - base de datos oracle
   - Apache
   - Tomcat

### ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
    -

### ¿Qué es el falló en cascada?
    derriba todo el servicio para los miembros, implementacion mal del cambio en multiples regione, solo se tiene que solucionar en el lugar

### ¿Qué es Hystrix?
    Es una biblioteca que controla la interacción entre microservicios para proporcionar latencia y tolerancia a fallas.  modifica la interfaz de usuario  que sepa que es posible que algo no haya funcionado como se esperaba

### ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
    de la infeccion parasitaria

### ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
    en escribir dos bases de datos una copia de los mismos datos en dos nases quue se ekecutan en tres redes diferentes o una AWS, esto podria ser tres zonas de disponibilidad diferentes

### ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
    desarrollo una estrategia multirregional de estreptococos con tres regiones de AWS, de modo que si alguna de ellas fallaba por completo, aun se podia enviar todo el trafico a las otras regiones supervivientes

### ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
    el escenario sin edtado, escenaro con estado con componentes fundamentales, escenario hibrido

### ¿De qué manera se describe un "stateless service" en el video?
    no es un efectivo o una base de datos, no esta almacenando cantidades masivas de datos alos que habra accedido con frecuencia de metadatos almacenados, no tiene aginidad de instancia donde espera que un cliente se apague, la perdida de un nodo es esencialmente un no evento

### ¿Qué es Chaos Monkey?
    servicios con estado son bases de datos y cachés,tiene cachés internalizados pero de grandes cantidades de datos y  estrategias para replicar datos, este fue el mayor problema, por lo que le recomiendo encarecidamente que intente evitar almacenar su lógica comercial y su estado dentro de una aplicación si puede evitarlo ahora,que es eso la pérdida del nodo es un evento notable , puede llevar horas reemplazar ese nodo y hacer girar uno nuevo.

### ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
    acercado a una arquitectura usando una tecnología llamada edie cash y easy cash es esencialmente un envoltorio alrededor de Memcache D, está dividido de manera similar a los cachés de calamar, pero hay varias copias. escrito en varios nodos, por lo que cada vez que ocurre una escritura, no solo se escribe en varios nodos, sino que los escribe en diferentes zonas de disponibilidad, por lo que los esparce y los separa en la partición de red y, de la misma manera, cuando leemos, las lecturas son locales. porque desea esa eficiencia local, pero la aplicación puede recurrir a la lectura en las zonas de disponibilidad que necesita para llegar a esos otros

### ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
    node js,docker, python

### ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
    la escala de la dependencia
    uso dentro de las dependencias

### ¿Qué es Spinnaker?
    programa diseñado para integrar las mejores practicas, de modo que como se implementa en la produccion

### ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
    eliminando las unidades centrales de la arquitecura, para asi que estos nodos esten en el mismo nivel con los mismos beneficios y obligaciones

### ¿Qué es "chaos engineering" o "ingeniería del caos"?
    diciplina experimental en el sofware pero en tiempo de produccion siendo los beneficios de esta la capacidad y respuestas del sistema al soportar condiciones inesperadas, algo asi como pruebas de estres

