def cicloPotencia(N,M):
    lista=[]
    for i in range(0,M+1):
        lista.append(N**i)
    return lista

def ListaComprimidaPotencia(N,M):
    lista=[N**i for i in range(0,M+1)]
    return lista

N= int(input("Ingresa Numero base:"))
M= int(input("Ingresa Potencia:"))
print("Resultados con el ciclo:")
print(cicloPotencia(N,M))
print("Resultados con lista Comprimida") 
print(ListaComprimidaPotencia(N,M))       