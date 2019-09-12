cuenta = []
for i in range(0,20):
    cuenta.append(i+1)


print("Primeros 3 elementos en la lista")
print(cuenta[slice(3)])

print()

print("3 elementos del medio")
print(cuenta[slice(7,10)])

print()

print("ultimos 3 elementos de la lista")
print(cuenta[slice(len(cuenta)-3,len(cuenta))])