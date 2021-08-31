import string
# LISTAS
otra_lista = [1, 2, 3, 4, 5, 6]
print(otra_lista[0])
print(otra_lista[-1])

print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[3:])

copia_lista = otra_lista[:]
copia_lista.append(7)
print(otra_lista)
print(copia_lista)

#ESTRUCTURAS DE CONTROL Y DE ITERACION#

# IF
if True:
    print("Eh verdah")

semaforo = input('Dame el color del semaforo: ')
if semaforo == 'rojo':
    print("Detenido")
elif semaforo == 'amarillo':
    print("Detente")
else:
    print("Avanza")

    print("Si esta en la lista") if 1 in otra_lista else print(
        "Ni esta en la lista")

# WHILE

while otra_lista != []:
    elemento_borrado = otra_lista.pop()
    print(f'Extraje elemento {elemento_borrado}')  # interpolacion

copia_lista.clear()
while copia_lista:  # []: evalua a false
    elemento_borrado = copia_lista.pop()
    print('Extraje elemento de copia_lista {}'.format(elemento_borrado))
else:
    print("No entro en la lista")

# FOR

vocales = 'aeiou'
for vocal in vocales:
    print(vocal)

vocales = 'aeiou'
for i in range(0, len(vocales)):
    print(vocales[i])

for n in range(0, 100, 2):
    print(n)
# para imprimir de los pares de 0 a 100

nueva_lista = [0, 1, 2, ['otra', 'lista', [3, 4, 5]]]
print(nueva_lista[3][2][0])
# dimension 3, dentro de esa seria la 2, y dentro de esa la 0 para sacar el 3
print(isinstance(nueva_lista, list))
print("*" * 5)

for i in nueva_lista:
    # Si la el tipo de variable no es una lista imprime el valor, si si continua
    if isinstance(i, list) == False:
        print(i)
        continue
    for j in i:
        # Si el tipo de variable no es una lista imprime el valor, si si continua
        if isinstance(j, list) == False:
            print(f"{' ' * 2 }{j}")
        continue
        for k in j:
            print(f"{' ' * 4}{k}")


#LISTAS COMPRIMIDAS#
pares = [i for i in range(0, 101, 2) if i % 2 == 0]
print(pares)

impares = [i for i in range(1, 100, 2) if i % 2 != 0]
print(impares)

# Funcion map()
animales = ["gato", "perro", "oso", "leon", "ballena"]
print(list(map(str.upper, animales)))

# Tuplas

# A DIFERENCIA DE LAS LISTAS LAS TUPLAS NO SON MODIFICABLES EN NINGUN SENTIDO
una_tupla = (1, 2, 3)
#una_tupla[2] = 5
print(una_tupla)

tupla_comprimida = tuple(x for x in string.ascii_lowercase if x in 'aeiou')
print(tupla_comprimida)

# Diccionarios
mi_diccionario = {
    'luis': ['perro', 'gato'],
    'daniela': ['loro', 'gato'],
    'romina': ['camaleon', 'geeko']
}

print(mi_diccionario)
print(mi_diccionario['daniela'])

for key in mi_diccionario.keys():
    print(f'Key "{key}"')

for value in mi_diccionario.values():
    print(f'Values "{value}"')

for value in mi_diccionario.values():
    print(f'Values "{value}"')

for key, value in mi_diccionario.items():
    print(f'Key: "{key}" - Value: "{value}"')


# Funciones
def suma(a, b):
    print(a + b)


def resta(a, b):
    print(a - b)


def multiplicacion(a, b):
    print(a * b)


def division(a, b):
    print(a / b)


suma(5, 5)
resta(5, 5)
multiplicacion(5, 5)
division(5, 5)

# Clases y objetos


class Calculadora:
    #pass #ESTO SIRVE PARA QUE NO TIRE ERROR ES COMO PA DECIRLE QUE NO HAGA NADA AUN#
    # Magic Methods
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def suma(self):
        return(self.a + self.b)

    def resta(self):
        return(self.a - self.b)

    def multiplicacion(self):
        return(self.a * self.b)

    def division(self):
        return(self.a / self.b)
    
    def __str__(self):
        return '### Numeros ###\nA: {self.a}\nB: {self.b}'
        
    mi_calculadora = Calculadora(5,5)
    print(mi_calculadora.suma())
    print(mi_calculadora.resta())
    print(mi_calculadora.multiplicacion())
    print(mi_calculadora.division())
    print(mi_calculadora)
