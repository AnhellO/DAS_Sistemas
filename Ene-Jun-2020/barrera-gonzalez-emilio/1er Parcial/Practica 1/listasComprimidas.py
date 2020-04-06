N=int(input("Ingresa base:"))
M=int(input("Ingresa Potencia: "))
listaComprimida=[N**i for i in range(0,M+1)]

print(f"Estos son los resultados de las potencias:\n{listaComprimida}")