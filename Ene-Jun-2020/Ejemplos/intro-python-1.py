import json

####################
# Listas
####################

# Simple lista con los números del 0 al 10
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creamos una lista vacía y la llenamos con los números pares existentes en lista1
lista2 = []
for i in lista1:
	if i % 2 == 0:
		lista2.append(i)

# 1er ejemplo de listas comprimidas. Todos los pares del 0 al 10 usando range
lista3 = [i for i in range(0, 10, 2)]

# 2do ejemplo de listas comprimidas. Todos los pares del 0 al 10 usando condicional
lista4 = [i for i in lista1 if i % 2 == 0]

# 3ro ejemplo de listas comprimidas. Todos los caracteres de un string
lista5 = [i for i in 'hola mundo']

# 4to ejemplo de listas comprimidas. Solamente las vocales y '-' en caso contrario
lista6 = [i if i =='a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' else 'x' for i in 'hola mundo']

# 5to ejemplo de listas comprimidas. Igual que el anterior pero mejorado
lista7 = [i if i in 'aeiou' else '-' for i in 'hola mundo']

# 6to ejemplo de listas comprimidas. Potencias de 2
lista8 = [2**i for i in range(0, 100)]
 
lista_principal = [lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8]

for i in lista_principal:
	print(i)

####################
# Diccionarios
####################

diccionario1 = {'a': 1, 'b': 22, 'c': 3, 'd': 4, 'casa': 5}

diccionario2 = {
	'a': ['alfajor', 'alfombra', 'alemanes'],
	'b': ['borracho', 'bueno', 'balón'],
	'c': ['casa', 'cable', 'crema']
}

diccionario3 = {
	'123': {
		'nombre': 'Emilio',
		'edad': 22
	},
	'124': {
		'nombre': 'Fernando',
		'edad': 20
	},
	'125': {
		'nombre': 'Angela',
		'edad': 19
	}
}

lista_diccionarios = [diccionario1, diccionario2, diccionario3]

for i in lista_diccionarios:
	print(i)

print(json.dumps(lista_diccionarios, indent=4))