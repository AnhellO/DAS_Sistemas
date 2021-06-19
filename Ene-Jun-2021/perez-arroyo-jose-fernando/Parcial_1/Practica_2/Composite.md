# Composite 
Este es un patron de diseño en el cual las personas pueden hacer una estructura compleja tomando como una base algunas mas simples.
Un ejemplo que puedo nombrar es el de una casa, esta esta construida con ladrillos, blocks o adobe, podemos ver que estas paredes no estan construidas por uno solo de estos materiales sino que estan compuestas por varios de los objetos lo que crea la casa.
El patrón Composite requiere mínimo de tres componentes para poder existir los cuales son Componente, Leaf o Rama y Composite.

**Component:** Generalmente es una interface o clase abstracta la cual tiene las operaciones mínimas que serán utilizadas, este componente deberá ser extendido por los otros dos componentes Leaf y Composite. En nuestro ejemplo esto podría representar de forma abstracta un ladrillo o toda la casa (Mas adelante comprenderemos porque)

**Leaf:** El leaf u hoja representa la parte más simple o pequeña de toda la estructura y este extiende o hereda de Component. En nuestro ejemplo, este representaría un ladrillo de nuestra casa.

**Composite:** Aquí es donde está la magia de este patrón, ya que el composite es una estructura conformada por otros Composite y Leaf, si vemos en la imagen 1, vemos que los Composite tiene los métodos add y remove los cuales nos permiten agregar objetos de tipo Component, Sin embargo como hablamos anteriormente, el Componente es por lo general un Interface o Clase abstracta  por lo que podremos agregamos objetos de tipo Composite o Leaf. 

# Referencias
* <https://www.oscarblancarteblog.com/2014/10/07/patron>
