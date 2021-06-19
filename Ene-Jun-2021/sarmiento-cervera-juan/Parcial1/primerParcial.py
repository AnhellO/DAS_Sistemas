import math;

def Triangular(n):
    r=math.sqrt(8*n+1)
    if (r - int (r) > 0):
        return False
    else:
        return True
trian = int(input("ingresa el numero triangular que deseas conocer: "))

for i in range(trian):
    if(Triangular (i)):
        print(i)
## Es el unico que termine he hice lo que pude pero ya de aqui no supe que hacer lo sigo analisando igual que el segundo problema