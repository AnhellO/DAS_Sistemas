import string 
#Retomando la clase pasada

#estructura de datos

#lista
otra_lista=[1, 2, 3, 4, 5, 6]
#acciones de la lista

print(otra_lista[0])
print(otra_lista[-1])

# slocong
print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[3:])

copia_lista= otra_lista[:]
copia_lista.append(7)
print(otra_lista)
print(copia_lista)

#estructuras de interaccion 
#if
if True:
    print ("verdad")
semaforo= input("dame el color del semaforo ")
if semaforo =='verde':
  print ("abansa")
elif semaforo=='amarillo':
    print ("detente")
else :
    print ("detente")
print ("esta en la lista")if 1 in otra_lista else print ("no esta")

#while

while otra_lista != []:
   elemento_borrado=otra_lista.pop()
   print (f"estraje elemento {elemento_borrado}")#interpolacion 

copia_lista.clear()
print(copia_lista)

while copia_lista != []:# evalua como false porque esta basia 
    elemento_borrado=copia_lista.pop()
    print ("estraje elemento {}".format(elemento_borrado))#interpolacion 
else:
        print("no entro en el while")

#for
vocales ='aeiou'
for vocal in vocales:
    print(vocal)
       
vocales ='aeiou'
for i in range(0,len(vocales)):
    print(vocales[i])

for n in range(0, 101, 2):
    print(n)

nueva_lista=[0, 1, 2, ["otra", "lista",[3, 4, 5]]]
print (nueva_lista[3][2][0])
print(isinstance(nueva_lista, list))
print('*' * 5)
for i in nueva_lista:
    if type(i) != 'list':
        print(i)
        continue
    for j in i:
        if type(j) != 'list':
         print(j)
         continue 
        for k in j :
            print (k)
    
for i in nueva_lista:
    if isinstance(i, list)==False:
        print(i)
        continue
    for j in i:
        if isinstance(j, list)==False:
         print(f"{' '* 2}{j}")
         continue 
        for k in j :
           print(f"{' '* 4}{k}")
    
#listas comprimidas 
pares =[i for i in range (0, 101, 2) if i % 2 == 0]
print (pares)
pinpares =[i for i in range (1, 101, 2)if i % 2 != 0]
print (pinpares)

# funcion map 
animales =["garo", "perro", "oso", "leon", "ballena"]
print (list(map(str.upper, animales)))
#tuplas

una_tupla=(1, 2, 3)
print(una_tupla)

tupla_comprimda =tuple(x for x in string.ascii_lowercase if x in 'aeiou')

print(tupla_comprimda)
#no soportan asignacion no se puede modificar 

#diccionario
mi_diccionario ={
    'luis':['perro', 'gato'],
    'daniel' :['loro', 'gato'],
    'romina':['camaleon','gatp']
}
print(mi_diccionario)
print(mi_diccionario['daniel'])
for key  in mi_diccionario.keys():
    print (f'key"{key}"')

for value in mi_diccionario.values():
    print (f'value"{value}"')

for key, value in mi_diccionario.items():
    print (f'key"{key}" - value"{value}"')

#funciones 

def suma(a,b):
    print (a+b)

def resta(a,b):
    print (a-b)

def multiplicacion(a,b):
    print (a *b)

def divicion(a,b):
    print (a/b)

suma(5,5)
resta(5,5)
multiplicacion(5,5)
divicion(5,5)

#clases y objetops

class calculadora:
    #Magic Methods
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
        
    def suma(self)-> int:
     return self.a + self.b
    def resta(self)-> int:
     return self.a - self.b
    def multiplicaion(self)-> int:
     return self.a * self.b
    def divicion(self)-> float:
     return self.a /self.b
    def __str__(self):
        return f'####'

   
