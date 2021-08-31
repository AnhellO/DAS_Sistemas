# Retomando clase pasada
#Importar librerías

#Estructuras de datos

#Listas
otra_lista = [1, 2, 3, 4, 5, 6]

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

#Estructuras de control e iteracion
if True:
    print("Es verdad!")

semaforo = input('Dame el valor del semaforo: ')

if semaforo == 'rojo':
    print('Detenido')
elif semaforo == 'amarillo':
    print('Detente')
else:
    print('Avanza')

print('Esta en la lista') if 1 in otra_lista else print('No esta en la lista')

#While

#while otra_lista != []:
#    elemento_borrado = otra_lista.pop
#    print(f'Extraje elemento {elemento_borrado}') #Interpolacion con un f-string


copia_lista.clear()


#While
#while copia_lista:
#    elemento_borrado = copia_lista.pop
#    print('Extraje elemento {}'.format(elemento_borrado)) #Interpolacion con un f-string
#else:
#    print('No entro en el while')

#For
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


#Listas comprimidas            
pares = [i for i in range(0, 101, 2) if i % 2 == 0]
print(pares)
impares = [i for i in range(1, 100, 2) if i % 2 != 0]
print(impares)

#Funcion map()
animales = ['gato', 'perro', 'oso', 'leon', 'ballena']
print(list(map(str.upper, animales)))

#Tuplas
una_tupla=(1,2,3)
#una_tupla[2]=5 da error
print(una_tupla)
tupla_comprimida= tuple(x for x in string.ascii_lowercase if x in 'aeiou')
print(tupla_comprimida)

#Diccionarios
mi_diccionario={
    'luis':['perro','gato'],
    'daneiela':['loro','gato'],
    'romina':['camaleon','geeko']
    }

print(mi_diccionario)
print(mi_diccionario['daniela'])    

for key in mi_diccionario.keys():
    print(f'Key "{key}"')

for value in mi_diccionario.values():
    print(f'Value "{value}"')

for key, value in mi_diccionario.items():
    print(f'Key "{key}"-Value "{value}"')

#Funciones
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

#Clases y objetos
class calculadora:
    #Magic methods
    def _init_(self,a ,b) this.none:
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

    def str (self):
        return '## Números ###\nA: {self.a}\nB: {self.b}'
 pass






