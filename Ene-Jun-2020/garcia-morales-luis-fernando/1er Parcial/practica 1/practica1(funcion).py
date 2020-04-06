def potencia(m,n):
    for i in range(0,int(m)+1):
        print(n + '^' + str(i) +'='+ str(int(n)**i))

m = input("ingresa valor m: ")
n = input("ingresa valor de n: ")

potencia(m,n)
