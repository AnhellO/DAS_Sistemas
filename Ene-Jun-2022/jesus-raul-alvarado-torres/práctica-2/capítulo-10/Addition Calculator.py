print("Escribe 'exit' para detener el programa")

while True:
    try:
        x = input("Dame un numero entero: ")
        if x == 'exit':
            break
        x = int(x)

        y = input("Dame otro numero entero: ")
        if y == 'exit':
            break
        y = int(y)

    except ValueError:
        print("Error, eso no es un numero entero")

    else:
        sum = x + y
        print("La suma de " + str(x) + " y " + str(y) + " es " + str(sum))