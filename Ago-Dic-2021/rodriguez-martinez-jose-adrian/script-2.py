import string 

#Retomando clase pasada

#Estructuras de datos
#########################
#Listas
#########################

otra_lista = [1, 2, 3, 4, 5, 6]
#Accediendo a elementos de una lista
print(otra_lista[0])
print(otra_lista[-1])

#Slicing
print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[0:])

copia_lista = otra_lista[:]
#copia_lista = otra_lista es diferente a otra_lista[:]
copia_lista.append(7)
print(otra_lista)
print(copia_lista)

#Estructuras de control e iteracion

#if
if True:
    print("Verdadero")

semaforo = input('Color del semaforo: ')
if semaforo == 'rojo':
    print('Alto')
elif semaforo == 'amarillo':
    print('Detente')
else:
    print('Avanza')

print('Está en la lista :)') if 1 in otra_lista else print('No está en la lista >:(')

#While
otra_lista.clear()

while otra_lista != []:
    elemento_borrado = otra_lista.pop()
    print(f'Elemento extraido de otra_lista: {elemento_borrado}')

while copia_lista:
    elemento_borrado = copia_lista.pop()
    print('Elemento extraido de copia_lista: {}'.format(elemento_borrado))

else:
    print('No entró en el while')

#FOR
vocales = 'aeiou'
for vocal in vocales:
    print(vocal)

for vocal in range(0, len(vocales)):
    print(vocal)

for n in range(0, 10, 2):
    print(n)

nueva_lista = [0, 1, 2, ['otra', 'lista', [3, 4, 5]]]
print(nueva_lista[3][2][0])


print(isinstance(nueva_lista, list))
for i in nueva_lista:
    if isinstance(i, list) == False:
        print(i)
        continue

    for j in i:
        if isinstance(j, list) == False:
            print(f"{' '*2}{j}")
            continue

        for k in j:
            print(k)

#List Comprehension 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "a" in x]

print(newlist)

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

"""
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
        return f'### Numeros ###\nA: {self.a}\nB: {self.b}'
mi_calculadora = Calculadora(5, 5)
print(mi_calculadora.suma())
print(mi_calculadora.resta())
print(mi_calculadora.multiplicacion())
print(mi_calculadora.division())
print(mi_calculadora)
"""


"""class Calculadora:
    #pass #ESTO SIRVE PARA QUE NO TIRE ERROR ES COMO PA DECIRLE QUE NO HAGA NADA AUN#
    # Magic Methods
    def __init__(self, lista_numeros: list) -> None:
        self.lista_numeros = lista_numeros

    def suma(self) -> int:
        suma = 0
        for i in self.lista_numeros:
            suma += i
        return(suma)

    def resta(self) -> int:
        resta = 0
        for i in self.lista_numeros:
            resta -= i
        return resta

    def multiplicacion(self) -> int:
        multiplicacion = 0
        for i in self.lista_numeros:
            multiplicacion *= i
        return multiplicacion

    def division(self) -> float:
        division = 0
        for i in self.lista_numeros:
            division *= i
        return division

    def __str__(self):
        return f'### Numeros ###\nA: {self.lista_numeros}'


mi_calculadora = Calculadora(5, 5)
mi_calculadora_2 = Calculadora(5, 5, 2)
print(mi_calculadora_2.suma())
print(mi_calculadora_2.resta())
print(mi_calculadora_2.multiplicacion())
print(mi_calculadora_2.division())
"""

class Calculadora:
    #pass #ESTO SIRVE PARA QUE NO TIRE ERROR ES COMO PA DECIRLE QUE NO HAGA NADA AUN#
    # Magic Methods
    def __init__(self, *lista_numeros) -> None:
        self.lista_numeros = lista_numeros

    def operacion(self, operacion: str):
        s = 1
        for i in self.lista_numeros:
            if operacion == 'suma':
                s += i
            elif operacion == 'resta':
                s -= i
            elif operacion == 'multiplicacion':
                s *= i
            elif operacion == 'division':
                s /= i
        return s

    def __str__(self):
        return f'### Numeros ###\nA: {self.lista_numeros}'


mi_calculadora_2 = Calculadora(5, 5, 2)
print(mi_calculadora_2.operacion('suma'))
print(mi_calculadora_2.operacion('resta'))
print(mi_calculadora_2.operacion('multiplicacion'))
print(mi_calculadora_2.operacion('division'))


class Persona:
    def __init__(self, **kwargs) -> None:
        self.nombre = kwargs.get('nombre')
        self.edad = kwargs.get('edad')
        self.peso = kwargs.get('peso',0.0)



    def __str__(self) -> str:
        return f'### Persona ###\nNombre: {self.nombre}\n Edad: {self.edad}\n Peso: {self.peso}'

#p = Persona('Fulanito', 15, 70.5)
p = Persona(nombre='Fulanito', edad=15, peso=70.5)
print(p)