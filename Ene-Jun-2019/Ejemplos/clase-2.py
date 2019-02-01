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
    print(operacion)
