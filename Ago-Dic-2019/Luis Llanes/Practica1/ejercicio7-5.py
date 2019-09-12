print("bienvenido a nuestro cine \nIngrese su edad para consultar el precio del boleto \nSi desea dejar de agregar introduzca  -1")

edad = int(input("Edad: "))

while edad >= 0:
    
    if edad >= 0 and edad < 3:
        print("El boleto es gratis")
    elif edad >=3 and edad < 12:
        print("El boleto cuesta $10")
    else:
        print("El boleto cuesta $15")

    edad = int(input("Edad: "))