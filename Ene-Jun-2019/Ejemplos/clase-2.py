# Comentarios con hashtag :D print('Hi segunda clase!')

def ingresa_valores():
    variable1 = float(input('Ingresa variable1: '))
    variable2 = float(input('Ingresa variable2: '))

    return [variable1, variable2]

variable1, variable2 = ingresa_valores()

while not variable2:
    print('variable2 necesita ser diferente de 0')

    variable1, variable2 = ingresa_valores()

operaciones = []
operaciones.append(variable1 + variable2)
operaciones.append(variable1 - variable2)
operaciones.append(variable1 * variable2)
operaciones.append(variable1 / variable2)
operaciones.append(variable1 % variable2)
operaciones.append(variable1 ** variable2)

# print("""
# Suma {0} + {1} = {2}
# Resta {0} - {1} = {3}
# Multiplicación {0} * {1} = {4}
# División {0} / {1} = {5}
# Residuo {0} % {1} = {6}
# Potencia {0} ^ {1} = {7}
# """.format(variable1, variable2, *operaciones))

for operacion in operaciones:
    pass#print(operacion)

# Genera una lista con todos los números pares del 1 al 100
# [i for i in range(0, 100, 2)] o [i for i in range(0, 100) if i % 2 == 0]

# Genera una lista con todas las vocales existentes en un string
# [i for i in 'Diseño y Arquitectura de Software' if i in 'aeiou']

# Genera una lista con todos los caracteres del string, y convierte a mayúsculas aquellos caractéres que son vocales
# [i.upper() if i in 'aeiou' else i for i in 'diseño y arquitectura de software']
