ejecucion = True

while ejecucion:
    num1 = input("Ingrese el primer numero: ")
    num2 = input("Ingrese el segundo numero: ")
    try:
        resultado = int(num1) + int(num2)
    except ValueError:
        print("No se pueden sumar letras/caracteres.")
    else:
        print(resultado)
    i = input("Ingrese 'q' si ya no quiere calcular mas sumas.")
    if i=='q':
        break