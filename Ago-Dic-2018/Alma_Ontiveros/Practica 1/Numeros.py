tamaño=int(input('Escribe el total de números para evaluar: '))
impares=0
pares= 0
negativos= 0
positivos=0
lista=[]
entrada=input('Escribe los números a evaluar (separados con un espacio entre ellos): ')
lista=[int(tamaño) for tamaño in entrada.split(" ")]

for i in range(0,tamaño):
    num=lista[i]
    if num % 2:
        impares= impares + 1
    else:
         pares= pares + 1
    if num < 0:
        negativos= negativos + 1
    else:
          positivos= positivos + 1

print(str(pares) + " Numero(s) Pares")
print(str(impares) + " Numero(s) Impares")
print(str(negativos) + " Numero(s) Negativos")
print(str(positivos) + " Numero(s) Positivos")
print(lista)