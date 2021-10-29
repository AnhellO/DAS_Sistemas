import string
# Retomando clase pasada

# Estructura de datos

###########################
# Listas
#########################3
otra_lista = [ 1, 2, 3, 4, 5, 6]

# Accediendo a los elementos de una lista
print(otra_lista[0])
print(otra_lista[-1])

# Slicing
print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[3:])

copia_lista = otra_lista[:]
copia_lista.append(7)
print(otra_lista)
print(copia_lista)

###########################################
# Estructuras de control y de iteración
###########################################

# IF (de control)
if True:
    print("Es verdad")

semaforo = input("Dame el color del semáforo: ")
if semaforo == 'rojo':
    print('Detenido')
elif semaforo == 'amarillo':
    print('Detente')
else:
    print('Avanza')

print('Está en la lista') if 1 in otra_lista else print('No está en la lista') #?

# while (iteración)
while otra_lista != []:
    elemento_borrado = otra_lista.pop()
    print(f'Extraje elemento  de otra_lista {elemento_borrado}') #interpolación

copia_lista.clear()
#print(copia_lista)
while copia_lista: #[] evalúa False
    elemento_borrado = copia_lista.pop()
    print('Extraje elemento de copia_lista {}'.format(elemento_borrado))
else:
    print('No entró en el while')
# print([] == False)

#FOR
vocales= 'aeiou'
for vocal in vocales:
    print(vocal)

vocales= 'aeiou'
for i in range(0, len(vocales)):
    print(vocales[i])

for n in range(0,101,2): #pares
    print(n)

for n in range(1,100,2): #impares
    print(n)

nueva_lista = [0, 1, 2, ['otra', 'lista', [3, 4, 5], 'nueva'], 6]
print(nueva_lista[3][2][0])
print(isinstance(nueva_lista, list))
print('*' * 5)

for i in nueva_lista:
    if isinstance(i, list) == False:
        print(i)
        continue

    for j in i:
        if isinstance(j, list) == False:
            print(f"{' ' * 2}{j}")
            continue

        for k in j:
            print(f"{' ' * 4}{k}")

#  Listas comprimidas
pares = [i for i in range(0, 101, 2) if i % 2 == 0]
print(pares)
impares = [i for i in range(1, 100, 2) if i % 2 != 0]
print(impares)

#Función map()
animales = ['gato','perro','oso','leon','ballena']
print(list(map(str.upper,animales)))

#################################
# Tuplas
#################################
una_tupla = (1, 2, 3)
# una_tupla[2] = 5 -> esto da error
print(una_tupla)

tupla_comprimida = tuple(x for x in string.ascii_lowercase if x in 'aeiou')
print(tupla_comprimida)

#################################
# Diccionarios
#################################
mi_diccionario = {
    'luis': ['perro','gato'],
    'daniela': ['loro','gato'],
    'romina': ['camaleón','geeko'],
    }

print(mi_diccionario)
print(mi_diccionario['daniela'])

for key in mi_diccionario.keys():
    print(f'Key "{key}"')

for value in mi_diccionario.values():
    print(f'Values "{value}"')

for key, value in mi_diccionario.items():
    print(f'Key: "{key}" - Value: "{value}"')

# Funciones
def division(a, b):
    print(a / b)
def suma(a, b):
    print(a + b)

def resta(a, b):
    print(a - b)

def multiplicacion(a, b):
    print(a * b)

suma(5,5)
resta(5,5)
multiplicacion(5,5)
division(5,5)

#################################
# Clases y Objetos
#################################
class Calculadora:
    # Magic Methods
    def __init__(self, a, b)-> None:
        self.a = a
        self.b = b

    def suma(self) -> int:
        return (self.a + self.b)

    def resta(self) -> int:
        return (self.a - self.b)

    def multiplicacion(self) -> int:
        return (self.a * self.b)

    def division(self) -> float:
        return (self.a / self.b)

    def __str__(self):
        return f'### Números ###\nA: {self.a}\nB: {self.b}'

mi_calculadora = Calculadora(5,5)
print(mi_calculadora.suma())
print(mi_calculadora.resta())
print(mi_calculadora.multiplicacion())
print(mi_calculadora.division())
print(mi_calculadora)
