# Práctica 5

## Objetivos

* Mejorar en el conocimiento de patrones de diseño
* Mejorar técnicas de desarrollo como refactorización y `T.D.D.`
* Desarrollar lógica y capacidad análitica para poder implementar soluciones
* Calentar motores para el 1er exámen parcial

## Especificaciones

1. Para el archivo de [facade.py](facade.py)
   1. El subsistema complejo que ya se encuentra en el ejemplo implementa el patrón de diseño `Composite`. La funcionalidad de este no debería de modificarse como tal, pero si lo consideras necesario puedes hacerlo
   2. El objetivo es crear un objeto que nos permita representar una computadora con los componentes de hardware provistos en el ejemplo. Implementa el patrón de diseño `Facade`, de tal manera que podamos _"encender"_ y _"apagar"_ una instancia de nuestro objeto computadora, el cual deberá de construirse con el código existente de `Composite`
2. Para el archivo de [strategy_test.py](strategy_test.py)
   1. Imagina que estamos desarrollando la capa de autenticación para una aplicación y las especificaciones nos dicen que podemos acceder al servicio por medio de diferentes métodos de autenticación. Implementa la funcionalidad necesaria para tener flexibilidad de cambio en el tipo de autenticación requerida, todo esto utilizando el patrón de diseño de `Strategy`
   2. En este ejercicio aplicaremos una estrategia `T.D.D.`, por lo cual tendrás que partir de los tests para modelar las clases y objetos necesarios. Los tests **NO** deben de modificarse, sin embargo, sí es posible agregar nuevos casos de prueba a la suite en caso de considerarlo pertinente

## Recursos

* Todos los recursos que hemos utilizado y visto de patrones de diseño hasta el momento

## Deadline

* `Domingo 11 de Octubre a las 11:59pm`
