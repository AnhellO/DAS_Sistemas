"""Try it yourself 9-13 """

from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'Es una serie de caracteres'
glossary['comentario'] = 'Una nota en un programa que el interprete de python ignorara'
glossary['lista'] = 'Una colección de items en un particular orden, nuestros arreglos en python'
glossary['ciclo'] =  'Se trabaja en una colección de elementos, uno a la vez'
glossary['dictionario'] ='Una colección de valores clave y llaves'
glossary['llave'] = 'El primer item en una llave en un diccionario '
glossary['valor'] =  'Un elemento asociado a una llave en un diccionario'
glossary['conditional test'] =  'Una comparación entre dos valores'
glossary['float'] = 'Una expresion numerica con componentes decimales'
glossary['boolean expression'] = 'Una exoresión que evalua solamente verdadero o falso'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)