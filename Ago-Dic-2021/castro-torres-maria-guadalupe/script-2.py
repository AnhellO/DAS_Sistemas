#retomando clase pasada


#Estructura de datos
#################################
#listas


otra_lista = [1, 2, 3, 4 , 5, 6]

#Accediendo a los elementos de una lista
print(otra_lista[0])
print(otra_lista[-1])

#Slicing
print(otra_lista[0:3])
print(otra_lista[3:])

copia_lista = otra_lista

copia_lista.append(7)
print(otra_lista)
print(copia_lista)


##################
#estructura de control y de iteracion
#######################################

if True:
    print("Es verdad")


semaforo = 'rojo'

if semaforo == 'rojo':
    print('detenido')
elif semaforo == 'verde':
    print('avanza')
else:
    print('detente')

print('No esta en la lista') if 1 in otra_lista else print('No esta en la lista')  

#while


while otra_lista != []:
    elemento_borrado = otra_lista.pop()
    print(f'Extraje elemento {elemento_borrado}') #interpolacion


while copia_lista:
    elemento_borrado = copia_lista.pop()
    print('Extraje elemento de copia_lista {}'.format(elemento_borrado)) #interpolacion    
else:
    print("No entro en el while:(")


#For

vocales = 'aeiou'

for vocal in vocales:
    print(vocal)

vocales = 'aeiou'
for i in range(0, len(vocales)):
    print(vocales[i])


for n in range(0, 101, 2):
    print(n)

nueva_lista = [0, 1, 2['otra', 'lista',[3, 4, 5]]]
print(nueva_lista[3][2][0])
print(isinstance(nueva_lista,list))
print('*' * 5)


for i in nueva_lista:
    if isinstance(i,list)== False:
        print(i)
        continue

    for j in i:
        if isinstance(j, list)== False:
            print(j)
            continue
        for k in j:
            print(k)


#listas comprimidas

pares = [ i for i in range(0, 101, 2) if i % 2==0]
print(pares)

impares = [ i for i in range(1, 100, 2) if i % 2==0]
print(impares)

# Function map()

animales= ['gato', 'perro', 'oso','leon', 'ballenaa']
print(list(map(str.upper, animales)))


################
#Tuplas
################

una_tupla=(1, 2, 3)
print(una_tupla)
tupla_comprimida = tuple( x for x in string.ascii.lowercase if x in 'aeiou')
print(tupla_comprimida)




#################
#Diccionarios
#################

mi_diccionario = {
    'luis':['perro','gato'],
    'daniela':['loro','gato'],
    'romina':['camaleon','gato'],
}

print(mi_diccionario)
print(mi_diccionario['daniela'])


for key in mi_diccionario.keys():
    print(f'key "{key}"')

for value in mi_diccionario.values():
    print(f'Value "{value}"') 


############################
#Funcion
###########################
def sum(a, b):
    print(a+b)

def rest(a, b):
    print(a - b)  

def division(a, b):
    print(a / b)  

def multiplicacion(a, b):
    print(a * b) 


sum(5, 5)
rest(5, 5) 
division(5, 5) 
multiplicacion(5, 5)              

#########################
#clases y objetos
########################


class Calculadora:

    def __init__(self) -> None:

        self.a = a
        self.b = b

    def suma(self) -> int:
        print(self.a + self.b)

    def __str__(self):
        return '#### Numeros ###\nA: {self.a}\nB: {self.b}'

    mi_calculadora = Calculadora(5,5)
    mi_calculadora.suma

    pass
   




