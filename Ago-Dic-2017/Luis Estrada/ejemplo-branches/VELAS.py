def birthdayCakeCandles(n):
    lista=[]
    m=0
    mayor=0
    resultado=""
    for i in range(n):
        num=int(input("Ingrese el valor: "))
        lista.append(num)
        
        if lista[i]>mayor:
            mayor=lista[i]
    for i in range(n):
        if lista[i]==mayor:
            m+=1
    resultado+="Los tamaños de las velas son: " + str(lista) + "\n"
    resultado+="Las velas sopladas son: " + str(m)
    return resultado

n=int(input("Ingresa el número de velas: "))
result=birthdayCakeCandles(n)
print(result)
