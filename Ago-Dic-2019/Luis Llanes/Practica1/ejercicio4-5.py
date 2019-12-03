#Hacer una lista del 1 al 1,000,000 y despues usar min y max para verificar

listanumeros=[]
for i in range(0,1000000):
    listanumeros.append(i+1)

print("Numero menor:", min(listanumeros))
print("Numero mayor:", max(listanumeros))
print("Suma de todos:", sum(listanumeros))


#pues el resultado arrojado por sum es casi instantaneo, 500000500000