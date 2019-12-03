lugares=["Venecia","Francia","Japon","Alemania","Minessota"]

print("Orden original")
print(lugares,"\n")

print("Ordenados alfabeticamente sin alterar la lista original")
print(sorted(lugares), "\n")

print("No se modifico la original")
print(lugares,"\n")

print("Ordenados alfabeticamente de manera inversa sin alterar la lista original")
print(sorted(lugares,reverse=True),"\n")

print("No se modifico la original")
print(lugares,"\n")

print("Invertir la lista original")
lugares.reverse()
print(lugares,"\n")

print("Regresar la lista que acabamos de invertir a como estaba")
lugares.reverse()
print(lugares,"\n")

print("Ordenar la lista alfabeticamente modificando la lista")
lugares.sort()
print(lugares,"\n")

print("Ordenar la lista alfabeticamente de forma invertida modificando la lista")
lugares.sort(reverse=True)
print(lugares)
