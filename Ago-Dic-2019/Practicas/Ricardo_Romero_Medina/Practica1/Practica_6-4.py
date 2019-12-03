glosario={
    'if': 'Sirve como una condicion para hacer una comparacion y si es cierta ejecutar lo que se pide',
    
   'elif':'Sirve para meter una condicion dentro de un if',
    
    'else':'Sirve para ejecutar parte de un programa cuando la condicion if no se cumple',
    
    'for':'Sirve para poder crear un bucle mientras se mantenga dentro de un rango',

    'append':'Sirve para agregar un dato en una lista al final de ella'
}

glosario['sorted']='Sirve para acomodar los datos de una lista por orden alfabetico o por oden numerico sin modificar la lista'

glosario['sorted reverse']='Sirve para acomodar los datos de una lista por orden alfabetico inverso o por oden numerico inverso sin modificar la lista'

glosario['sort']='Sirve como el metodo sorted acomoda por orden alfabetico o numerico pero este si modifica la lista'

glosario['sort reverse']='Sirve como el metodo sorted acomoda por orden alfabetico inverso o numerico inverso pero este si modifica la lista'

glosario['insert']='Sirve para agregar un dato a la lista en cualquer lugar de ella'

palabras=glosario.keys()

definicion=glosario.values()

elementos=glosario.items()

for palabras,definicion in elementos:
    print(palabras, ':' ,definicion)