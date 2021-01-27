bandas=['Queen','Guns And Roses','Metallica','Linkin Park','The Beatles','DragonForce','Pantera','Thirty Seconds to Mars','Evanescence','Aerosmith']

for i in range(len(bandas)): 
    print(bandas[i])

bandas.append('Avenged Sevenfold')

print("\nLista con una nueva banda agregada al final\n")

for i in range(len(bandas)): 
    print(bandas[i])

print("\nLista con una nueva banda agregada en algun lugar de la lista\n")

bandas.insert(5, 'Mago de Oz')

for i in range(len(bandas)): 
    print(bandas[i])

print("\nLista con una nueva banda eliminada de algun lugar de la lista\n")

del bandas[5]

for i in range(len(bandas)): 
    print(bandas[i])

print("\nLista con una nueva banda eliminada del ultimo lugar de la lista\n")

bandas.pop()

for i in range(len(bandas)): 
    print(bandas[i])

print("\nLista con una nueva banda eliminando por nombre de la banda\n")

bandas.remove('Pantera')

for i in range(len(bandas)): 
    print(bandas[i])

bandas.insert(6,'Pantera')
bandas.insert(5, 'Mago de Oz')
bandas.append('Avenged Sevenfold')
bandas.insert(8,'Slipknot')

print("\nLista Ordenada por el metodo sorted\n")

print(sorted(bandas))

print("\nLista Ordenada por el metodo sorted inverso\n")

print(sorted(bandas,reverse=True))

print("\nLista Ordenada por el metodo sort\n")

bandas.sort()

print(bandas)

print("\nLista Ordenada por el metodo sort inverso\n")

bandas.sort(reverse=True)

print(bandas)

print("\nLista Ordenada por el metodo reverse\n")

bandas.reverse()

print(bandas)

print("\nTamaño de la lista\n")

print("El tamaño de la lista de bandas es: ",len(bandas))