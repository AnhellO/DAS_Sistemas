# Realiza un pequeño script en Python que lea dos números M y N a través de la consola,
# y que para ellos genere una lista que contenga las primeras M potencias del número N
# Crea dos versiones del mismo script, una utilizando ciclos normales, y la otra utilizando listas comprimidas

# Versión 2

M = int(input("Valor para M: "))
N = int(input("Valor para N: "))

r = [N ** i for i in range(1, M+1)]
print("\nResultados =", r)