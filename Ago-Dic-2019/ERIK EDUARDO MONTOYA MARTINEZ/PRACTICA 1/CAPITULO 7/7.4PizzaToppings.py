msj="\nQue ingrediente quiere en su pizza? "
msj+="\n Cuando termine escribe 'fin'. "

ingredientes=""
while ingredientes != 'fin':
    ingredientes=input(msj)
    print("Agregaste este ingrediente a tu pizza")
    if ingredientes!='fin':
        print(ingredientes)


