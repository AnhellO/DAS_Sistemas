#Retomando clase pasada!

#Estructuras de datos
import string
######################################
#Listas
######################################

otra_lista = [1,2,3,4,5,6]
#Accediendo a los elementos de una lista
print(otra_lista[0])
print(otra_lista[-1])
#slicing
print(otra_lista[0:3])
print(otra_lista[:3])
print(otra_lista[3:])
copia_lista = otra_lista[:]
copia_lista.append(7)
print(otra_lista)
print(copia_lista)

#######################################
#Estructuras de control y de iteracion 
#######################################

#IF
if True:
    print("Es verdad!")

semaforo = input("Dame el color del semaforo: ")
if semaforo == "rojo":
    print("Detenido")
elif semaforo == "amarillo":
    print("Detente")
elif semaforo == "verde":
    print("Avanza")

print("Esta en la lista :") if 1 in otra_lista else print ("No esta en la lista :(")

#While
while otra_lista != []:
    elemento_borrado = otra_lista.pop()
    print(f"Extraje elemento {elemento_borrado}") #Interpolacion 
copia_lista.clear()

while copia_lista:
    elemento_borrado = copia_lista.pop()
    print("Extraje elemento de copia lista {}".format(elemento_borrado))
else:
    print("No entro en el while :(")

#For 
vocales = "aeiou"
for vocal in vocales:
    print(vocal)

vocales ="aeiou"
for i in range(0,len(vocales)):
    print(vocales[i])

for n in range (0,101,2):
    print(n)

nueva_lista = [0,1,2,["otra","lista",[3,4,5],"nueva"],6]
print(nueva_lista[3][2][0])
print(isinstance(nueva_lista,list))
print("*"*5)

for i in nueva_lista:
    if isinstance(i,list) == False:
        print(i)
        continue
    for j in i:
        if isinstance(j,list) == False:
            print(f"{' '*2}{j}")
            continue
        for k in j:
            print(f"{' '*4}{k}")

#Listas comprimidas
pares = [i for i in range (0,101,2)if i % 2 == 0]
print(pares)
impares = [i for i in range(1,100,2)if i % 2 != 0]
print (impares)

#Funcion map()
animales = ["gato","perro","oso","leon","ballena"]
print(list(map(str.upper,animales)))

################################
#tuplas
################################
una_tupla = (1,2,3)
print(una_tupla)
tupla_comprimida = tuple(x for x in string.ascii_lowercase if x in 'aeiou')
print(tupla_comprimida)
################################
#Diccionarios
################################
mi_diccionario = {
    "luis":["perro","gato"],
    "daniela":["loro","gato"],
    "romina":["camaleon","geeko"]
}

print(mi_diccionario)
print(mi_diccionario["daniela"])
for key in mi_diccionario.keys():
    print(f"key'{key}'")
for value in mi_diccionario.values():
    print(f"values'{value}'")
for key,value in mi_diccionario.items():
    print(f"key'{key}'- value: '{value}'")

############################
#Funciones
############################

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

############################
#Clases y objetos
############################

class calculadora:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def suma(self)->int:
        print(self.a+self.b)
    
    def resta(self)->int:
        print(self.a-self.b)

    def multiplicacion(self)->int:
        print(self.a*self.b)    

    def division(self)->float:
        print(self.a/self.b)
    def __str__ (self):
        return f"### Numeros ###\nA:|{self.a}\nB:{self.b}"

mi_calculadora=calculadora(5,5)
mi_calculadora.suma()
mi_calculadora.resta() 
mi_calculadora.multiplicacion()
mi_calculadora.division()