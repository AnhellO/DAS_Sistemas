* Preguntas

  * ¿Qué busca solucionar esta arquitectura?
  > Aplicando el principio de diseño de software "separación de responsabilidades (SRP)", se busca mediante este principio establecer una resposabilidad unica establecida por capas para la logica de negocio y un mejor entendimiento en el diseño de la arquitectura del software.

  * ¿Qué es la "_regla de dependencia_" o "_dependency rule_"?
  > Esa regla especifica que algo declarado en un círculo exterior no debe ser mencionado en el código por un círculo interior .
Eso significa que las dependencias del código solo pueden apuntar hacia adentro.
Por ejemplo, el código de la capa de dominio no puede depender del código de la capa de infraestructura, el código de la capa de infraestructura puede depender del código de la capa de dominio (porque va hacia adentro).

  * ¿Qué abarca la capa de _Entidades_ o _Entities_?
> Las entidades son las que incluyen las reglas de negocio críticas para el sistema. Estas entidades pueden ser utilizadas por distintos componentes de la arquitectura, por lo que son independientes, y no deben cambiar a consecuencia de otros elementos externos.

  * ¿Qué abarca la capa de _Casos de Uso_ o _Use Cases_?
  > Los casos de uso, solo definen como se comporta nuestro sistema, definiendo los datos de entrada necesarios, y cual será su salida. Los cambios en esta capa no deberían afectar a las entidades, al igual que los cambios en otras capas externas no deberían afectar a los casos de uso.
  

  * ¿Qué abarca la capa de _Adaptadores_ o _Interface Adapters_?
  > Los datos generados por los casos de uso y las entidades, tienen que transformarse en algo entendible por la
  "Adaptadores de interfaz", los controladores y las vistas, pertenecerían a esta capa, y el modelo, serían los datos que se pasan entre los casos de uso y los controladores para luego poder presentar las vistas. 
  

  * ¿Qué abarca la capa de _Frameworks_ o _Frameworks and Drivers_?
  > En la capa más externa es donde van los detalles. Y la base de datos es un detalle, nuestro framework web, es un detalle etc.
  

  * ¿Puede haber más de 4 capas? Complementa tu respuesta explicando tu razonamiento
  > Pueden existir n capas, pero cada una debe tener una responsabilidad única. Una separación muy utilizada es la de tres capas “presentación”, “lógica de negocio” y “acceso a datos”. 
  


  * ¿Qué son los "_boundaries_"?
  > es una separación que definimos en nuestra arquitectura para dividir componentes y definir dependencias. 
  

