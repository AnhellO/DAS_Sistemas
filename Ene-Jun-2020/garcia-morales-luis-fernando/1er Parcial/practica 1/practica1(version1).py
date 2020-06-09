m = input("ingresa valor m: ")
n = input("ingresa valor de n: ")

for i in range(0,int(m)+1):
    print(n + '^' + str(i) +'='+ str(int(n)**i))