############Con una función##########################
print('Valor de M:')
M = int(input())
print('Valor de N:')
N = int(input())

def potencia(M, N):

    resultado=1

    for i in range(N):
        resultado *= M

        return resultado
print(M**N)
print(pow(M, N))
print(potencia(M,N))

#########################Con un listas comprimidas########################

print('Valor de M:')
M = int(input())
print('Valor de N:')
N = int(input())

list = [i**N for i in range(0, N)]
print('Potencias, ' + str)

