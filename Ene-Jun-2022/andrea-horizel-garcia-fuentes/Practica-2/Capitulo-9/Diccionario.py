from collections import OrderedDict

diccionario = OrderedDict()

diccionario['string'] = 'Cadena de caracteres.'
diccionario['key'] = 'Generador de llave.'
diccionario['value'] = 'Valor de codigo.'
diccionario['comment'] = 'Nota en un programa que python ignora.'
diccionario['list'] = 'Estructura de datos.'
diccionario['import'] = 'Enlaza los resultados de busqueda.'
diccionario['from'] = 'Importa modulos.'
diccionario['false'] = 'Son elmentos nulos o vacios.'
diccionario['try'] = 'Es utilizada para referise a una accion.'
diccionario['if'] = 'Se utiliza para ejecutar un bloque de codigo.'

for word, definicion in diccionario.items():    
    print("\n" + word + " " + definicion)