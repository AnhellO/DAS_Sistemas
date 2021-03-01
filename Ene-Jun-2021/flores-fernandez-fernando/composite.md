Composite
=========

Composite es un objeto creado de otros objetos(partes) y este patron esta creado para algunos casos en los que necesitas usar objetos
compuestos y objetos singulares de manera uniformeo de manera transparente, por que desde la vista del cliente a veces no necesita
saber si es un objeto compuesto o un objeto singular. y esto se logra creando una sola interfaz que permita utilizarlos de manera uniforme
(de manera uniforme se refiere a que a una colleccion de objetos se le pueden hacer los mismos tratos que a un objeto singular ).

What if... 
----------

que tal si tenemos un arbol binario.
tenemos el nodo root, desde la perspectiva de root tiene otras dependencias que crea al arbol, pero si tomamos otro nodo que sea 
branch. el no puede ver todo el arbol, solo puede observar a su padre y a sus hijos. desde esta perspectiva podemos decir que el nodo 
branch que elegimos es el nodo root de su jerarquia. si encerramos solo la branch podemos decir que es un objeto composite(compuesto)
de solo su rama, y que el root del arbol es otro objeto composite de todo el arbol. pero si seguimos hasta llegar a los nodos leaves estos
ya no son objetos compuestos ya que solo estan ellos en singular 

Ejemplo
-------
tenemos un arbol binario que es un arbol genealogico en el root estoy yo luego estan los padres que son branch y al final los abuelos que 
son leaves.
si me llegan  a pedir get_last_name() a mi lo que pasa es que le doy mi nombre pero concatenando los nombres de los nodos dependientes  los padres, que al ser objectos composite regresan sus nombres pero
concatenando los de sus dependientes que son los abuelos.

el punto de composite es reemplazar lo condicional del ejemplo con polimorfismo asi que en lugar de tener branches que si en algun caso
hacemos algo y en otro caso hacemos una accion diferente. usamos polimorfirmo para decir que hay dos tipos de nodo. 
asi que solo tenemos los nodos composite que tienen una implementacion 
y los nodos leaves o singulares que tienen otra implementacion
haciendo que las dos utilicen la misma interfaz, podemos ponerlos en una estructura de datos y recorrerlos y que corran el metodo  get_last_name()
sin necesidad de preguntarnos si un solo componente es un composite o es una leave asi nos ahorramos del statement if 
