
#retomando clase pasada



#*******************listas************************

otra_lista = [1,2,3,4,5,6]

#acediendo a los terminos de una lista

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

#*******************************
# estructura de control y de iteración

#IF
if True:
    print("Es verda")

semaforo = input("Dame color de semaforo")
if semaforo == "rojo":
    print("DEtenerte")
elif semaforo == "Amarillo":
    print("ir deteniendote")
else:
    print("Avanza")


#print("Esta en la lista") if a > b else print("No esta en la lista") 


#while
while otra_lista != []:
    elemento_borrado = otra_lista.pop()
    print("Extraje elemento: {elemento_borrado}") # interpolación

copia_lista.clear()


#while  [] evalua a false
while copia_lista:
    elemento_borrado = copia_lista.pop()
    print('Extraje elemento copia_lista: {}'.format(elemento_borrado)) # interpolación



# for

vocales ='aeiou'
for vocal in vocales:
    print(vocal)

vocales = 'aeiou'
for i in range(0,len(vocales)):
    print(vocales[i])


# para impar '1'
for n in range(0,100,2):
    print(n)


nueva_lista = [0,1,2,['otra','lista',[3,4,5]]]
print(nueva_lista[3][2][0])
print(isinstance(nueva_lista,list))
print('*'*5)


for i in nueva_lista:
    if isinstance(i,list)==False:
        print(i)
        continue

    for j in i:
        if isinstance(j,list)==False:
            print(f"{' '*2}{j}")
            print(j)
            continue

        for k in j:
            print(k)



#listas comprimidas
pares = [i for i in range(0,101,2) if i %2 == 0]
print(pares)
print('________________________________________________________')
impares = [i for i in range(1,101,2) if i %2 !=0]
print(impares)


# funcion map()
animales = ['gato','perro','oso','leon','ballena']
print(list(map(str.upper,animales)))


#************** tuplas **********************

una_tupla = (1,2,3)
print(una_tupla)




#****************** diccionarios *******************
mi_diccionario = {
        'luis':['perro','gato'],
        'daniela':['loro','gato'],
        'carlos':['perro','jirafa']
        }

print(mi_diccionario)
print(mi_diccionario['daniela'])

for key in mi_diccionario.keys():
    print(f'key "{key}"')
for value in mi_diccionario.values():
    print(f'value "{value}"')
for key,value in mi_diccionario.items():
    print(f'key: "{key}" - value:"{value}"')


#**************** funciones ********************
def suma(a,b):
    print(a+b)

def resta(a,b):
    print(a-b)

def multiplicacion(a,b):
    print(a*b)

def division (a,b):
    print(a/b)

suma(5,5)
resta(5,5)
multiplicacion(5,5)
division(5,5)



#************ clase y objeto ********************

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
