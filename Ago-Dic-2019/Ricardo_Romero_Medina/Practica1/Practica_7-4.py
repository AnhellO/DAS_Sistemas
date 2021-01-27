ingred=""
while ingred != "salir":
    ingred=input("Da un ingrediente para la pizza: ")

    if ingred != "salir":
        print("Se le agregara a la pizza el ingrediente: ",ingred)

    else:
        print("Espere su orden")