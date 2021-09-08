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