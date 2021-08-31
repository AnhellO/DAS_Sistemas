import string
#Estructura de datos

#################################
#Listas                         #
#################################
otra_lista=[1, 2, 3, 4, 5, 6]

#Accediendo a los elementos de una lista
print (otra_lista[1])
print (otra_lista[-1])

#Slicing
print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[3:])
#Copia Lista
copia_lista = otra_lista[:]
copia_lista.append(7)
print(otra_lista)
print(copia_lista)

#######################################
#Estructura de control y de iteracion #
#######################################
#IF  (Se separa por indentaciones)    #
#######################################
if True:
    print("Es verdad!")

semaforo = input("Dame el color del semaforo: ")
if semaforo == 'rojo':
    print('Detenido')
elif semaforo == 'amarillo':
    print('Detente')
else:
    print('avanza')


print('Esta en la lista') if 1 in otra_lista else print('No esta en la lista')
#######################################
#while                                #
#######################################
#while otra_lista != []:
    #elemento_borrado = otra_lista.pop()
    #print(f'Extraje elemeto de otra_lista {elemento_borrado}') # Interpolacion

copia_lista.clear()

#while copia_lista:
    #elemento_borrado = copia_lista.pop()
    #print('Extraje elemeto de copia_lista {}'.format(elemento_borrado))
    #else:
#print('No entro en el while') 
#######################################
#for                                  #
#######################################
vocales = 'aeiou'
for vocal in vocales:
    print(vocal)

for i in range(0, len(vocales)):
    print(vocales[i])

for n in range(0, 101, 2):
    print(n)

nueva_lista = [0, 1, 2, ['otra', 'lista', [3, 4, 5]]]
print(nueva_lista[3][2][0])
print(isinstance(nueva_lista, list))
print('*' * 5)

for i in nueva_lista: #Recorrer lista de 3D opcion 1
    if (type(i) != 'list'):
        print(i)
        continue;
        
    for j in i:
        if (type(i) != 'list'):
            print(i)
            continue;

        for k in j:
            print(k)

for i in nueva_lista: #Recorrer lista de 3D opcion 2
    if (isinstance(i, list) == False):
        print(i)
        continue;
        
    for j in i:
        if (isinstance(j, list) == False):
            print(j)
            continue;

        for k in j:
            print(k)
#####################################
#Listas comprimidas                 #
#####################################
pares = [i for i in range(0, 101, 2) if i % 2 == 0]
print(pares)
impares = [i for i in range(1, 100, 2) if i % 2 != 0]
print(impares)

#Funcion map()
animales = ['gato', 'perro', 'oso', 'leon', 'ballena']
print(list(map(str.upper, animales)))

#Tuplas
una_tupla = (1, 2, 3)
#una_tupla[2] = 5 no se pueden modificar valores de una tupla
print(una_tupla)
tupla_comprimida = tuple(x for x in string.ascii_lowercase if x in 'aeiou')
print(tupla_comprimida)
#Diccionarios
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
    print(f'Value "{value}"')

for key, value in mi_diccionario.items():
    print(f'Key "{key}" - Value: "{value}"')

#Funciones
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

#Clases y objetos
class Calculadora:
    #Magic methods
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    #Funciones
    def suma(self):
        return (self.a + self.b)

    def resta(self):
        return (self.a - self.b)

    def multiplicacion(self):
        return (self.a * self.b)

    def division(self):
        return (self.a / self.b)

    def __str__(self) -> str:
        return 'Numeros: {}, {}'.format(self.a, self.b)

mi_calculadora = Calculadora(5, 5)
print(mi_calculadora.suma())
print(mi_calculadora.resta())
print(mi_calculadora.multiplicacion())
print(mi_calculadora.division())
print(mi_calculadora)
