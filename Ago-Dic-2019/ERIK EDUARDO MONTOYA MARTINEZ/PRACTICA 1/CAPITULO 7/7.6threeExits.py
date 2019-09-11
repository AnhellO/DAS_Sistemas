msj = "\nQue ingrediente quiere en su pizza? "
msj += "\n Cuando termine escribe 'fin'. "

ingredientes = ""
while ingredientes != 'fin':
    ingredientes = input(msj)
    print("Agregaste este ingrediente a tu pizza")
    if ingredientes != 'fin':
        print(ingredientes)

print("---------------------------------------")

active = True
while active:
    mensaje = input(msj)
    if mensaje == 'fin':
        active = False
    else:
        print(input)

print("----------------------------------")

while True:
    mensaje = input(msj)
    if mensaje == 'fin':
        break
    else:
        print("Agregaste este ingrediente a tu pizza: " + ingredientes)


