m = input("ingresa valor m: ")
n = input("ingresa valor de n: ")

lista_potencias = [(int(n)**i) for i in range(0,int(m)+1) ]
print(lista_potencias)