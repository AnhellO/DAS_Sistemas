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
miTupla[1] = []
print(miTupla)
