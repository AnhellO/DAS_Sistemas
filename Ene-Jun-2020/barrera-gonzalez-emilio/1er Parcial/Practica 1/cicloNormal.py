N=int(input("Ingresa un numero base pls:"))
M=int(input("Ingresa una potencia pls:"))
print("LOS RESULTADOS SON:")
for i in range(0,M+1):
    print(f"{N}^{i} = " + str(N**i))