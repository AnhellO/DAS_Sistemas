import collections

potenciaPares = 2
potenciaImpares = 3

# print(2 / 3)

#for i in range(0, 10):
    #if i % 2:
        # Estilo de formateo 1:
        # print("Impar: %d" % (i))
        # Estilo de formateo 2:
        # print("El impar #{} ^ {} es = {}".format(i, potenciaImpares, i ** potenciaImpares))
    #else:
        # Estilo de formateo 1:
        # print("Par: %d" % (i))
        # Estilo de formateo 2:
        # print("El par #{} ^ {} es = {}".format(i, potenciaPares, i ** potenciaPares))

# Corchetes [] para las listas
miListilla = [1, 'uai', 3, 'lista', 'puede', 'tener', 'de', 'todo', 'por ejemplo', [7, 777, 77]]
#print(miListilla)
#Hágalo con slicing
#print("Hola"[:2])
#print(miListilla[-2][1])

#for i in miListilla:
#    if isinstance(i, collections.Iterable):
#        for j in i:
#            if j == 777:
#                print("El número de la suerte :D esssss -> {}!!!".format(j))

miListilla.append(777)
miListilla.insert(2, [])
miListilla.insert(2, [])
miListilla.insert(2, 3)
miListilla.remove([])
miListilla[1] = 'Hey!'
miNuevaListilla = miListilla[:]
miNuevaListilla.reverse()
print(miNuevaListilla)
print(miListilla)

miTupla = (1, 2, 3)
# Aquí falla ehhh -> miTupla[1] = []
print(miTupla)

# Sumatoria de Gauss y Números triangulares
# (N * (N + 1)) / 2
# print(int((3 * (3 + 1)) / 2))

# Listas comprimidas
print([2 ** i for i in range(0, 10)])

frase = "Hola Buenas noches A!!!"
print([i.upper() for i in frase if i in 'AEIOUaeiou'])

# Diccionarios
diccionario = {
    'llave': 'valor'
}

elDiccionario = {
    'A': [
        'aguacate',
        'armadura',
        'avanzar'
    ],
    'E': [
        'enfermo',
        'error',
        'elote'
    ],
    'I': [
        'información',
        'imagen',
        'invisible'
    ],
    'O': [
        'oreja',
        'oso',
        'olor'
    ],
    'U': [
        'umbral',
        'unicornio',
        'uva'
    ]
}

# Recorre los elementos del diccionario
for llave, valor in elDiccionario.items():
    print("Llave {} => Valor {}".format(llave, valor))

# Recorre las tuplas que devuelve la función items()
for llave in elDiccionario.items():
    print(llave)

# Recorre las llaves ordenadas e imprime el elemento[llave]
for llave in sorted(elDiccionario.keys()):
    print(elDiccionario[llave])


def formatea(item):
    if isinstance(item, list):
        listaCopia = item[:]
        listaCopia.append('agregao')
        return "Una copia diferente -> {}".format(listaCopia)

    return "Acá lo regresamos formateado -> {}".format(item)

miLista = [1, 2]
print(formatea(miLista))
print(miLista)
miLista2 = [3, 4]
print(formatea(miLista2))
print(miLista2)

print(formatea('String'))
print(formatea(64361349713976972364691))


class Gato:

    def __init__(self, nombre='', colorOjos='', color=''):
        self.nombre = nombre
        self.colorOjos = colorOjos
        self.color = color

    def __str__(self):
        return 'Gatito: {}\nColor: {}\nOjos: {}'.format(self.nombre, self.color, self.colorOjos)

gatito_1 = Gato('Micifus', 'verdes', 'verde')
print(gatito_1)

gatito_2 = Gato('Salem', 'cafes')
print(gatito_2)

gatito_3 = Gato()
print(gatito_3)
