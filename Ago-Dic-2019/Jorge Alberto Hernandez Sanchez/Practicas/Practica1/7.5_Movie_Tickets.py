edad = int(input("Dame la edad"))
while True:
    if edad < 3:
        print("El boleto es gratis")
        break
    elif edad >= 3 and edad <= 12:
        print("El boleto cuesta $10")
        break
    elif edad > 12:
        print("El boletpo cuesta $15")
        break