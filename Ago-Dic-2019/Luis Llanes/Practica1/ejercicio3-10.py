comida = ["tacos", "pozole", "pan de muerto", "pastel", "spaghetti", "gorditas"]

print("Acceder a los elementos de la lista individualmente")
print(comida[0])
print(comida[2])
print(comida[5])
print("Mostrar todos los elementos")
print(comida)

print()

print("Eliminar algun elemento")
del comida[3]
comida.pop()
print(comida)

print()

print("Agregar elementos en distintos puntos de la lista")
print("Al inicio burritos")
comida.insert(0,"burritos")
print("Al medio sopa")
comida.insert(2, "sopa")
print("Al final con .append tostadas")
comida.append("tostadas")

print("Asi quedaria ahora")
print(comida)

print()

print("Ahora a jugar con el orden de la lista")
print("Orden original")
print(comida,"\n")

print("Ordenados alfabeticamente sin alterar la lista original")
print(sorted(comida), "\n")

print("No se modifico la original")
print(comida,"\n")

print("Ordenados alfabeticamente de manera inversa sin alterar la lista original")
print(sorted(comida,reverse=True),"\n")

print("No se modifico la original")
print(comida,"\n")

print("Invertir la lista original")
comida.reverse()
print(comida,"\n")

print("Regresar la lista que acabamos de invertir a como estaba")
comida.reverse()
print(comida,"\n")

print("Ordenar la lista alfabeticamente modificando la lista")
comida.sort()
print(comida,"\n")

print("Ordenar la lista alfabeticamente de forma invertida modificando la lista")
comida.sort(reverse=True)
print(comida)

print()

print("Al final mostrar la longitud de esta lista que es de:",len(comida))