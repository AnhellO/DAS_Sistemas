#
# estructuras de datos

#listas 


from typing import MutableMapping


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
tupla_comprimida = tuple(x for x in str.ascii_lowercase if x in 'aeiou')
print(tupla_comprimida)

#Diccionario

mi_dicionario = {
    'luis' : ['perro', 'gato'],
    'Daniela' : ['loro','gato'],
    'romina' : ['camaleon','geeko']
}

print(mi_dicionario)
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

class calculadoras:
    #Magic methods
    def __init__(self,lista_numeros: list) -> None:
        self.lista_numeros = lista_numeros

    def operacion(self,operacion : str):
        s = 0
        for i in self.lista_numeros:
            if operacion == 'suma':
                s+=1
            elif operacion == 'resta':
                s-=1
            elif operacion == 'multiplicaciion':
                s*=1
            elif operacion == 'division':
                s/=1
        return s    
    #def suma(self) -> int:
        suma = 0
        for i in self.lista_numeros:
            suma += 1
        return suma

    #def resta(self) -> int:
        resta = 0    
        for i in self.lista_numeros:
            resta -=1
        return resta

   # def multiplicacion(self) -> int:
        multiplicacion = 0    
        for i in self.lista_numeros:
            multiplicacion*=1
        return multiplicacion

    #def division(self) -> float:
        division = 0    
        for i in self.lista_numeros:
           division /=1
        return division
  
  
    def _str_ (self):
        return f'## Números ###\nA: {self.lista_numeros}'
 
calculadoras = calculadoras(2,3,4)
print(calculadoras.operacion('suma'))
print(calculadoras.operacion('resta'))
print(calculadoras.operacion('multipliacion'))
print(calculadoras.operacion('division'))
print(calculadoras)




# kayboard arguments y protected attributes

class persona:
    def _init_(self,**kwargs) -> None:

        self.nombre = kwargs.get('nombre')
        self.edad = kwargs.get('edad')
        self.peso = kwargs.get('peso')
    
    def _str_(self) -> str:
        return f'##'
