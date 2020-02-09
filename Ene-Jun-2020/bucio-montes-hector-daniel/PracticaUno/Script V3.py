# Crea otra nueva versión del script en la que encapsules la lógica anterior en una función

# Versión 3

M = int(input("Valor para M: "))
N = int(input("Valor para N: "))


def potencias(M, N):
    print("\nResultados:")

    for i in range(1, M + 1):
        print(N, "^", i, " = ", N ** i)


potencias(M, N)
