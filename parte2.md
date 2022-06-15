¿Qué busca solucionar esta arquitectura?
     R = Separar la lógica de negocio de la infraestructura/persistencia. Lo cual hace que su mantenimiento y escalabilidad resulte más fácil.

¿Qué es la "regla de dependencia" o "dependency rule"?
    R = Ir de fuera hacia dentro, las capas de afuera pueden llamar a las capas de adentro.

¿Qué abarca la capa de Entidades o Entities?
    R = Encapsulan las reglas más generales y de alto nivel. Capa más adentro.

¿Qué abarca la capa de Casos de Uso o Use Cases?
    R = Las reglas comerciales específicas de la aplicación, encapsula e implemeta todos los casos de uso del sistema.

 ¿Qué abarca la capa de Adaptadores o Interface Adapters?
     R = Se encuentran adaptores con base de datos, conecciones con servicios , transformación de la información entrante y definición de endpoints.

¿Qué abarca la capa de Frameworks o Frameworks and Drivers?
    R = En esta capa van todos los detalles, tanto para mostrar datos en la UI como para obtener los datos requeridos.

¿Puede haber más de 4 capas? Complementa tu respuesta explicando tu razonamiento
    R = Las capas pueden aumentar o disminuir según sea necesario. Aquí lo principal es que la regla de dependencia se garantize y esto se puede lograr a medida que el nivel de abstracción sea mayor.

¿Qué son los "boundaries"?
    R = Son los límites que definimos dentro de nuestra arquitectura para dividir entre componentes y definir dependencias