#
# estructuras de datos

#listas 


otra_lista = [1,2,3,4,5,6]

#Accesediendo a elementos de una lista
print(otra_lista[0])
print(otra_lista[-1])

#Sticing
print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[3:])

copia_lista = otra_lista
copia_lista.append(7)
print(otra_lista)
print(copia_lista)

###Estructuras de control##

#if
if True:
    print("Es verdad")

semaforo = input("Dame el color de semaforo")

if semaforo == 'Rojo':
        print('Detenido')
    
elif semaforo == 'amarillo':
        print('Detente')
else:
        print('Avanza')

print('Esta en la lista :)')  if 1 in otra_lista else print('no ta')

while otra_lista  != []:
    elemento_borrado = otra_lista.pop()
    print(f'Extraje eñemento {elemento_borrado}')

copia_lista.clear()

while copia_lista: #Evalua el false
    elemento_borrado = copia_lista.pop()
    print('Extraje eñemento de copia lista {}'.format(elemento_borrado))    
else:
    print('no entra en whily')   



#for
vocales = 'aeiou'
for vocal in vocales:
    print(vocal)

vocales = 'aeiou'
for i in range(0, len(vocales)):
    print(vocales[i])   

for n in range(1, 101, 2):
    print(n)    

nueva_lista = [0, 1, 2, ['otra', 'lista',[3,4,5]]]
print(nueva_lista[3][2][0])
print(isinstance(nueva_lista, list))

for i in nueva_lista:
    if type(i) != 'list':
        print(i)
        continue

    for j in i:
        if type != 'list':
            print(j)   
            continue

        for k in j:
            print(k)


#listas comprimidas
pares = [i for i in range(0, 101, 2) if i % 2==0]
print(pares)
impares =  [i for i in range(1,100,2) if i % 2 !=0 ]
print (impares)

#map
animales = ['gato', 'perro','oso', 'leon', 'ballena']
print(list(map(str.upper, animales)))


#####tuplas
una_tupla = (1,2,3)
una_tupla[2] = 5
print(una_tupla)
tupla_comprimida = tuple(x for x in string.ascii_lowercase if x in 'aeiou')
print(tupla_comprimida)

#Diccionario

mi_dicionario = {
    'luis' : ['perro', 'gato'],
    'Daniela' : ['loro','gato'],
    'romina' : ['camaleon','geeko']
}

print(mi_diccionario)
print(mi_dicionario['Daniela'])

for key in mi_dicionario.keys():
    print(f'key "{key}" ')

for value in mi_dicionario.values():
    print(f'Value "{value}" ')    

for key, value in mi_dicionario.items():
    print(f'key "{key}" - values' "{value}") 


##Funciones

def suma(a,b):
    print(a+b)

def resta(a,b):
    print(a-b)    

def multiplicacion(a,b):
    print(a*b)

def division(a, b)    :
    print(a/b)

suma(5,5)
resta(5,5)
multiplicacion(5,5)
division(5,5)

#Clases y objetos

class videojuegos:
    #Magic methods
    def __init__(self,a ,b) this.none:
    self.a = a
    self.b = b

    def suma(self) int:
        print(self.a+self.b)

    def resta(self) int:
        print(self.a-self.b)    

    def multiplicacion(self) int:
        print(self.a*self.b)

    def division(self) float:
        print(self.a/self.b)

    def _str_ (self):
        return '## Números ###\nA: {self.a}\nB: {self.b}'
 pass