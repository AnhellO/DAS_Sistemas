# INTRODUCCIÓN A DOCKER - CLICKIT

##### **¿Qué es DOCKER?**
Es un proyecto desarrollado por la comunidad, en conjunto con la compañía que lo creó, para hacer un mejorproducto que pueda ser útil para todos.

A grandes rasgos, Docker es una tecnología de virtualización usada esencialmente para aislar procesos y aplicaciones del sistema principal (Host) y brindar mayor seeguridad a las aplicaciones y sistemas.

##### **¿Qué es un contenedor?**
Es una forma de separar procesos de manera independiente, también pueden ser agrupados en imágenes que más adelante serán usadas.

A diferencia de una virtualización normal que tendría que emular cada aspecto del sistema que se desea lanzar.

##### **¿Qué es una imagen en Docker?**
Una imagen es un conjunto de capas, cada una de estas se genera cada vez que realicemos algún cambio.

##### **Comandos principales para la construcción de una imagen**
   - Maintainer, From, Add, Copy, Run, Env, Entrypoint (Señalar el proceso principal), CMD, Expose (abrir puertos).

##### **¿Por qué usar Docker?**
   - Porque permite la creación de **ambientes inmutables**
   - **Portable**
   - Seguridad al manejar un ambiente aislado

##### **¿Es seguro?**
El principal problema de Docker es el mismo que le da sus ventajas, ya que al usar secciones del kernel de host, un ataque puede realizarse para ganar acceso al kernel principal.

Debe asegurarse que los procesos corran en ambientes sin privilegios de root, para que en caso de un ataque solo se tenga acceso a una sección del contenedor y no a todo.


#### **Comentario propio:**
Docker me parece una tecnología muy práctica, segura y útil. Si la utilizaría.
