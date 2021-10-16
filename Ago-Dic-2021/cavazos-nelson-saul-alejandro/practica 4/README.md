# Sintesis de Chain of Responsibility
es un patron diseñado que te permite pasar solisitudes a lo largo de una cadena, viendo como ejemplo: **una cadena donde personas donde se pasa cubetas de agua para apagar un incedio.**
## Problemas
a lo que yo entendi es que puede llegar a hacer muy complicado modificar el codigo ya que si quieres metere una nueva solisitud en medio de las demas tendrias que modificar casi todo el codigo y a la vista se podria ver muy desordenado.
## Solucion 
poniendo cada caso, cada comprobacion en su clase y un unico metodo que realice la comprobacion sera mucho mas facil, la solisitud y su informacion se pasara al metodo como argumenro, viendoce mas lineal 

[referencia](https://refactoring.guru/es/design-patterns/chain-of-responsibility "refactoring guru")