### ¿Qué es la arquitectura monolítica?
Es una forma de crear aplocaciones que se utiliza muy seguido, estas son solo una capa logica y una interfaz y si se requiere de realizar alguna actualizacion se tiene que volver a desplear todo.

### Puntos fuertes de la arquitectura monolítica
No hay preocupaciones en las actividades ya que todo se realiza desde una sola aplicación, las pruebas en el codigo son sencillas de hacer ya que pues es todo una sola unidad y gracias a esto es muy facil de implementar

### Debilidades de la arquitectura monolítica
Al momento de tratar de escalar una aplicacion monolitica se puede empezar a perder un poco la estructura del codigo y se hace dificil de entender, y al momento de querer implementar cambios corremos el riesgo de que nuestra app ya no funcione y solo podemos saber si funciona al desplegarse, lo que puede llevar mucho tiempo si la app es muy grande

### ¿Qué es la arquitectura de microservicios?
Es una aquitectura para crear una aplicacion pero esta tiene servicios pequeños que se comunican entre ellos para lograr un objetivo.

### Puntos fuertes de la arquitectura de microservicios
Es muy facil de escalar y se pueden utilizar diferentes lenguajes de programacion para adaptarlo segun el caso necesario, todo es independiente y los modulos se comunican entre si, y al momento de querer agregar mas funcionalidades solo se tiene que actualizar los modulos afectados.

### Debilidades de la arquitectura de microservicios
Si la aplicacion llega a crecer mucho, se vuelve un poco mas dicifil implementar los cambios necesarios, ademas a medida de que crece el software el desarrollo se vuelve menos agil.

### Arquitectura mejor para ti
Para decidir que tipo de estructura se debe de elegir existen varias caracteristicas que se deben de tomar en cuenta por ejemplo: 

- La cantidad de integrantes que hay en el equipo de desarrollo, si se tiene una cantidad limitada se recomienda utilizar la arquitectura monolitica

- Si no hay suficientes recursos para contratar developers se le dedica mas tiempo para el desarrollo de la arquitecturas

- Se tiene que tomar en cuenta la expleriencia en frameworks

- Si se quiere utilizar los microservicios se teien que considedar si hay el tiempo suficiente para diseñar la arquitectura y preocuparse por la escabilidad


### Arquitectura desde el punto de vista del testing.

- Los microservicios son dificiles de probar una vez ya integrados porque no se pueden probar los componentes individualmente

- Los monolitos son mas faciles de probar pues todo su sistema se implementa localmente


