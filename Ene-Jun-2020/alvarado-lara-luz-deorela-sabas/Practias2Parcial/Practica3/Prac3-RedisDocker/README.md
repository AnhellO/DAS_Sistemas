<h1>DOCKER & REDIS </h1> 
        
        Redis me parecio efectiva al momento de proporcionar 
        la informacion, ya que los datos residen, principalmente, 
        en memoria, gracias a esto ofrece rápidos accesos en la recuparacion 
        de datos.

<h2> Ventajas </h2>
    -   Velocidad por encima de la media gracias 
        a su almacenamiento en memoria.
    -   Posibilidad de persistir datos en disco para
        recuperacion ante fallas
    -   Facil configuracion
    -   Alta disponibilidad
<h2> Desventajas </h2>
    -   El metodo de persistencia RDB consume mucho I/O
        (Escritura en disco)
    -   Todos los datos trabajados deben encajar en la 
        memoria (en caso de no usar persistencia fisica)