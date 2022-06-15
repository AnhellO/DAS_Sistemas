try:
    x = input("Dame un numero entero: ")
    x = int(x)

    y = input("Dame otro numero entero: ")
    y = int(y)

except ValueError:
    print("Error, eso no es un numero entero")

else:
    sum = x + y
    print("La suma de " + str(x) + " y " + str(y) + " es " + str(sum))