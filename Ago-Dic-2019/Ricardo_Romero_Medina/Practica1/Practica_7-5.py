edad=input("¿Que edad tienes?")
edad=int(edad)

while True:
    if edad < 3:
        print("Su boleto es gratis")
        break
    elif edad >= 3 and edad <=12:
        print("Su boleto tiene un valor de $10")
        break
    else:
        print("Su boleto tiene un valor de $15")
        break