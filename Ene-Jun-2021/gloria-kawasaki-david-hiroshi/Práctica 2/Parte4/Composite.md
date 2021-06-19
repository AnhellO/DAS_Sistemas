#¿Qué se entendió con Composite Pattern?

El patrón compuesto (Composite Pattern) lo que hace sería recorrer objetos estructurados a manera de un árbol. En estos árboles pueden haber 2 tipos de objetos: un ***objeto final*** al que ya no se le puede agregar más profundidad, y un objeto ***contenedor*** al que si se le pueden agregar más objetos ***contenedores*** u ***objetos finales***. Lo que hace es recorrer el árbol completo hasta llegar a un ***objeto final***, los cuales son los que realizan las tareas o acciones, y ejecuta todos estos nodos antes de pasar a otro ***contenedor***.

Estos conceptos y divisiones se pueden esclarecer e incluso ampliar al verlo como una división del ejército. En esta ocasion, el más alto mando de esta división en cuestión les dice a sus capitanes que es lo que esperan, luego estos capitanes les dicen a sus subordinados inmediatos, para es estos hagan lo mismo hasta llegar al final de la cadena de mando.

Ahora, aplicando los primeros conceptos y los segundos, se puede concluir que el patrón compuesto va delegando las funciones conforme se va profundizando en el árbol.