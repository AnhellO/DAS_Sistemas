#9.13
from collections import OrderedDict

dicci = OrderedDict()

dicci['string'] = 'Cadena de caracteres.'
dicci['list'] = 'Estructura de datos.'
dicci['import'] = 'Enlaza los resultados de busqueda.'
dicci['from'] = 'Importa modulos.'
dicci['false'] = 'Son elmentos nulos o vacios.'
dicci['if'] = 'Se utiliza para ejecutar un bloque de codigo.'

for word, definicion in dicci.items():    
    print("\n" + word + " " + definicion)

#9.14
from random import randint


class Dado():
    def __init__(self, sides=6):
        self.sides = sides

    def girar_dado(self):
        return randint(1, self.sides)

dado = Dado()

resultados = []
for girar_num in range(10):
    resultado = dado.girar_dado()
    resultados.append(resultado)
print("dado de 6 caras - 10 tiros")
print(resultados)

dado = Dado(sides=10)

resultados = []
for girar_num in range(10):
    resultado = dado.girar_dado()
    resultados.append(resultado)
print("\ndado de 10 caras - 10 tiros")
print(resultados)

dado = Dado(sides=20)

resultados = []
for girar_num in range(10):
    resultado = dado.girar_dado()
    resultados.append(resultado)
print("\ndado de 20 caras - 10 tiros")
print(resultados)