import string
#retomando clase
#estructura de datos
otra_lista =[1,2,3,4,5]

###########################
#Accediendo a los elementos de la lista
###########################

print(otra_lista[0])
print(otra_lista[-1])

#Slicing
print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[3:])

copia_lista =otra_lista
copia_lista.append(7)

print(copia_lista)
print(otra_lista)

#Estructura de control y de identacion 
if True:
    print("Es verdad")

#semaforo = input("Dame el color del semaforo")
semaforo="rojo"
if semaforo=='rojo':
    print("detenido")
elif semaforo=='amarillo':
    print("detende")
else:
    print("avanza")

print('No está en la lista c:') if 1 in otra_lista else print('No esta en la lista :c')

#while
while otra_lista != []:
    elemento_borrado=otra_lista.pop()
    print(f'Extraje elemento{elemento_borrado}') #interpolación

copia_lista.clear()
print(copia_lista)


while copia_lista: #evalua a false []
    elemento_borrado=otra_lista.pop()
    print('Extraje elemento de copia lista{}'.format(elemento_borrado))  
else:
    print("No entro el while")

###########################
#For
###########################

vocales="aeio"
for vocal in vocales:
    print(vocal)

vocales="aeio"
for i in range(0,len(vocales)):
    print(vocales[i])

for n in range(0,101,2): #imprimir numeros pares hasta el 100
    print(n)

nueva_lista=[0,1,2,["otra","lista",[3,4,5]]]
print(nueva_lista[3][2][0])
print(isinstance(nueva_lista,list))

for i in nueva_lista:
    if isinstance(i,list)==False:
        print(i)
        continue
    for j in i:
        if isinstance(j,list)==False:
            print(f"{' ' * 2} {j} ")
            continue
        for k in j:
            print(f"{' ' * 4} {k} ")

###########################
#Listas comprimidas
###########################
#pares
pares=[i for i in range(0,101,2) if i%2==0]
print(pares)

#impares
impares=[i for i in range(1,100,2) if i%2!=0]
print(impares)

###########################
#Funcion Map()
###########################
animales=['perro','gato','oso','león','ballena']
print(list(map(str.upper,animales)))

###########################
#Tuplas
###########################
#una tupla ya no es modificable
una_tupla=(1,2,3)
#una_tupla[2]=5 => esto da error
print(una_tupla)
tupla_comprimida = tuple(x for x in string.ascii_lowercase if x in 'aeiou')
print(tupla_comprimida)

###########################
#Diccionarios
###########################

mi_diccionario ={
    'luis':['perro','gato'],
    'daniela':['loro','gato'],
    'romina':['camaleon','geeko']
    } 

print(mi_diccionario)
print(mi_diccionario['daniela'])

for key in mi_diccionario.keys():
    print(f'key "{key}"')

for value in  mi_diccionario.values():
    print(f'value"{value}" ')

for value in  mi_diccionario.items():
    print(f'key: "{key}" - value: "{value}"')

#######################
#funciones
#######################

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

#################
#clase y objetos
#################

class Calculadoraa:
    #Magic Methods
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def suma(self):
        return self.a+self.b

    def resta(self):
        return self.a-self.b

    def multiplicacion(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def __str__(self):
        return f'### Números ### \nA: {self.a} \nB {self.b}'

mi_calculadora = Calculadoraa(5,5)
print(mi_calculadora.suma())
print(mi_calculadora.resta())
print(mi_calculadora.multiplicacion())
print(mi_calculadora.division())
print(mi_calculadora)