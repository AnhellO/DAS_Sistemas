import string
#Retomando clase pasada

#Estructura de datos

otra_lista = [1,2,3,4,5,6]
#Accediendo a los elementos de una lista
print(otra_lista[0])
print(otra_lista[-1])
#Slicing
print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[3:])

copia_lista= otra_lista[:]
copia_lista.append(7)
print(otra_lista)
print(copia_lista)

#########################################
#Estructuras de control y de iteracion
#########################################

#if
if True:
    print("Es verdad!")

semaforo=input("Dame el color del semaforo\n")
if semaforo=="rojo":
    print("Detente!")
elif semaforo=="amarillo":
    print('Detente')
else:
    print("Avanza") 

print('Esta en la lista') if 1 in otra_lista else print('No esta en la lista')

#while
while otra_lista != []:
    elemento_borrado=otra_lista.pop()
    print(f'Extraje elemento {elemento_borrado}')#interpolacion

copia_lista.clear()
print(copia_lista)

while copia_lista:#[] evalua a false
    elemento_borrado=copia_lista.pop()
    print('Extraje elemento {}'.format(elemento_borrado))#interpolacion
else:
    print('No entro en while')


#for
vocales="aeiou"
for vocal in vocales:
    print(vocal)


vocales="aeiou"
for i in range(0, len(vocales)):
    print(vocales[i])

for n in range(0,101,2):
    print(n)

nueva_lista=[0,1,2,['otra','lista',[3,4,5]]]
print(nueva_lista[3][2][0])
print(isinstance(nueva_lista,list))
print('*' * 5)

for i in nueva_lista:
    if isinstance(i,list)==False:
        print(i)
        continue
    for j in i:
        if isinstance(j,list)==False:
            print(f"{' '* 2}{j}")
            continue

        for k in j:
            print(f"{' '* 4}{k}")

#Listas comprimidas

pares=[i for i in range(0,101,2) if i % 2 == 0]
print(pares)

impares=[i for i in range(1,100,2) if i % 2 != 0]
print(impares)

#Funcion map()
animales=['gato','perro','oso','leon','ballena']
print(list(map(str.upper,animales)))

###############################################
#tuplas
###############################################

una_tupla=(1,2,3)
#una_tupla[2]=5
print(una_tupla)
tupla_comprimida = tuple(x for x in string.string.ascii_lowercase if x in 'aeiou')
print(tupla_comprimida)


###############################################
#tuplas
#############################################

mi_diccionario={
    'luis':['perro','gato'],
    'daniela':['loro','gato'],
    'romina':['camaleon','geeko']
}

print(mi_diccionario)
print(mi_diccionario['daniela'])

for key in mi_diccionario.keys():
    print(f'key "{key}"')

for value in mi_diccionario.values():
    print(f'value "{value}"')
for key,value in mi_diccionario.items():
    print(f'key:"{key}"- value: "{value}"')

###############################################
#Funciones
#############################################

def suma(a,b):
    print(a+b)

def resta(a,b):
    print(a-b)

def multiplicacion(a,b):
    print(a*b)

def division(a,b):
    print(a/b)

suma(5,5)
resta(5,5)
multiplicacion(5,5)
division(5,5)

###############################################
#Clases y Objetos
#############################################

class Calculadora:
    #Magic methods
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

    def multiplicacion(self):
        return self.a * self.b

    def division(self):
         return self.a / self.b

    def __str__(self) -> str:

        return '### Numeros ###\nA:{self.a}\nB:{self.b}'

mi_calculadura=Calculadora(5,5)
print(mi_calculadura.suma())
print(mi_calculadura.resta())
print(mi_calculadura.multiplicacion())
print(mi_calculadura.division())
print(mi_calculadura)