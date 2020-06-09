
def calcPotencia(M, N):
    lista = [N**M for M in range(1, M + 1)]
    print(lista)

if __name__ == '__main__':
    M = int(input('Inserta M: \n'))
    N = int(input('Inserta N: \n'))
    calcPotencia(M,N)