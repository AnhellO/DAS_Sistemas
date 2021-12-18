Lógia implementada en mienfoque:
    El enfoque que utilicé fue el de quitar esa flexibilidad de realizar la serialización con una sola función y dividirla en otras funciones que solo lo hagan en un formato en concreto ya que de esta forma se podría saber con exactitud si tiene algún tipo de fallo.

¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
    Si se quiere agregar algún otro formato se tendría que hacer otras funciones que solo serializaran solo ese formato en cuestión, ya si necesita ponerse en un formato en concreto, entonces se agregaría otra función con la única acción de darle formato.

¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
    Ya que usa métodos puntuales para serializar en esos formatos determinados, se podría pasar algún otro objeto sin problema ya que estas funciones son modulares.