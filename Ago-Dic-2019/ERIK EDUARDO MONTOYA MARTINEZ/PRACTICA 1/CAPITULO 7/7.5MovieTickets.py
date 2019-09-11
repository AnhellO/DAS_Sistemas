mensaje=("Bienvenido ingresa tu edad: ")
mensaje+="\nCuando termine seleccione '0'"

while True:
    edad = input(mensaje)
    if int(edad) <3 and int(edad)>1:
        print("Tu boleto es gratis")

    elif (int(edad))>=3 and int(edad)<=12:
        print("Tu boleto cuesta $10")

    else: print("tu boleto cuests $15")
