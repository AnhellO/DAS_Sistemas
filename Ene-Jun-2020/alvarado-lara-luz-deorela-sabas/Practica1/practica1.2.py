#LISTAS COMPRIMIDAS
m = int(input("Ingresa un numero (m): "))
n = int(input("Ingresa un numero (n): "))

potencia = [n ** i for i in range(0, m)]
print(potencia)