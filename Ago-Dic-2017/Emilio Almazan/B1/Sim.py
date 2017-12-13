import random

Lista = []

suma=0
sumaV=0
varianza=0
for rand in range(100):
    r = round(random.uniform(10,20), 3)
    Lista.append(r)
    suma += r
print(Lista)
media = suma/100

for x in Lista:
    sumaV += ((x - media)**2)

varianza = sumaV /99
print(suma)
print ( "la media es = ", media)
print(sumaV)
print ("la varianza es =", varianza)


