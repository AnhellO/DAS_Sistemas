# Estructura de datos

###### listas ##########
otra_lista = [1, 2, 3, 4, 5, 6]

print(otra_lista)

#Accediendo a los elementos de una lista
print(otra_lista[1])
print(otra_lista[-1])

#Slicing
print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[3:])

#Copia lista
copia_lista = otra_lista[:]
copia_lista.append(7)
print(otra_lista)
print(copia_lista)

####################################
#Estructuras de control e iteracion
####################################

if True:
    print("Es verdad!")

semaforo = 'rojo'
if semaforo == 'rojo':
    print('Detenido')
elif semaforo == 'amarillo':
    print('Detente')
else :
    print('Avanza')

print('Esta en la lista') if 1 in otra_lista else print('No está')

#while
while otra_lista != []:
    elemento_borrado = otra_lista.pop()
    print(f'Extraje elemento de otra lista {elemento_borrado}') #interpolacion


otra_lista.clear
print(otra_lista)

#for
vocales = 'aeiou'
for vocal in vocales:
    print(vocal)

vocales = 'aeiou'
for i in range(0, len(vocales)):
    print(vocales[i])

for n in range(0, 101, 2):
    print(n)

print('------------------------') #esto lo hago pa separar resultados

nueva_lista =[0, 1, 2, ['otra', 'lista', [3, 4, 5]]]
print(nueva_lista[3][2][0])
print(isinstance(nueva_lista, list))
print('------------------------')

for i in nueva_lista:
    if isinstance(i, list) == False:
        print(i)
        continue

    for j in i:
        if isinstance(j, list) == False:
            print(j)
            continue

        for k in j:
            print(k)

print('------------------------')

#listas comprimidas
pares = [i for i in range(0, 101, 2) if i % 2 == 0]
print(pares, '\n')

impares = [i for i in range(1, 100, 2) if i % 2 != 0]
print(impares, '\n')

#funcion map
animales = ['perro', 'gato', 'pajaro', 'pez']
print(list(map(str.upper, animales)))
print('------------------------')
print('\n')

##################
#Tuplas
##################

una_tupla = (1,2,3)
#una_tupla[2] = 5 #does not support modifications#
print(una_tupla)
#tupla_comprimida = tuple(x for x in string.ascii_lowecase if x in 'aeiou')
#print(tupla_comprimida)


##################
#Diccionarios
##################

mi_diccioanrio = {
    'luis': ['perro', 'gato'],
    'daniela': ['loro', 'gato'],
    'romina': ['camaleon', 'geeko']
}
print(mi_diccioanrio, '\n')
print(mi_diccioanrio['daniela'])
print('\n')

for key in mi_diccioanrio.keys():
    print(f'key"{key}"')
    
print('\n')
print('\n')

##################
#Funciones
##################

def suma(a, b):
    print(a + b)

def resta(a, b):
    print(a - b)

def mul(a, b):
    print(a * b)

def div(a, b):
    print(a / b)

suma(5, 5)
resta(5,5)
mul(5,5)
div(5,5)
print('\n \n \n')

##################
#Clases y objetos
##################

class Calculadora:
    #magic methods
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def suma(self):
        print(self.a + self.b)

    def resta(self):
        print(self.a - self.b)

    def mul(self):
        print(self.a * self.b)

    def div(self):
        print(self.a / self.b)
    
    def __str__(self):
        return (f'### Números ###\nA:{self.a}\nB:{self.b}')

mi_calculadora = Calculadora(5,5)
print(mi_calculadora.suma())
print(mi_calculadora.resta())
print(mi_calculadora.mul())
print(mi_calculadora.div())
print(mi_calculadora)