from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'Para almacenar cualquie tipo de valor'
glossary['comment'] = 'Son, como su nombre lo dice, comentarios que sirven para saber que es lo que hace cada cosa que hacemos'
glossary['list'] = 'Es una coleccion de elementos'
glossary['loop'] = 'Trabaja iterando sobre un valor'
glossary['dictionary'] = "Una coleccion de llaves a las cuales se puede acceder"
glossary['key'] = 'El valor de un diccionario.'
glossary['value'] = 'Valor asociado a una llave en un diccionario'
glossary['conditional test'] = 'Una comparacion entre dos valores'
glossary['float'] = 'Tipo de numero con decimales extensos'
glossary['boolean expression'] = 'Una expresion que evalua si es verdad o falso'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)