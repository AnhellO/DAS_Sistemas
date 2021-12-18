from collections import OrderedDict

glosario = OrderedDict()

glosario['String'] = 'Cadena de caracteres'
glosario['int'] = 'Numero entero'
glosario['list'] = 'Coleccion de items en un orden'
glosario['loop'] = 'Trabajar sobre una coleccion de items, uno a la vez'

for i, j in glosario.items():
    print('\n' + i + ': ' + j) 