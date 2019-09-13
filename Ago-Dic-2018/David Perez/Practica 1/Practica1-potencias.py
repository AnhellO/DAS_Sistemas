# Es necesario convertir n a entero para la operación porque de entrada
# lo maneja como un string
n = int(input('Define N: '))
# La operación pow es el equivalente a usar ** para números enteros

for i in range(0,11):
    print(n**i)
