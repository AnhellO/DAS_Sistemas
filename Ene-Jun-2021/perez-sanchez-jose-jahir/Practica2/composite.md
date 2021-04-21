# Composite
El patron de diseño composite te permite crear objetos y que estos objetos se alberguen en una estructura de arbol,
asi tendras un mejor control y busqueda de los atributos que tienen tus objetos. Puedes tratar a estos objetos con 
una misma interfaz por lo tanto no importa mucho su complejidad, ademas el patron se comporta de forma recursiva.

El patron tiene una clase componente que tiene operaciones comunes del arbol, despues seguirian las hojas que como es
comun en un arbol no tienen subelementos y son las encargadas de hacer la mayoria del trabajo, despues tendriamos la 
clase contenedor que tendria en este caso subelementos como otros contenedores y/o hojas, a su vez esta le pasaria el
trabajo a estos, despues le regresan el resultado, lo procesa y lo devuelve al cliente. Y para terminar estaria el 
cliente que es parecido al de los demas patrones.