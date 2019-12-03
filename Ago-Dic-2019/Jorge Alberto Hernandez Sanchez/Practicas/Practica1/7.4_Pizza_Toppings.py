prompt = "\nDame un ingrediente par ala pizza"
prompt += "\n(escribe salir cuando termines de agregar los ingredientes)"
while True:
    ingrediente = input(prompt)
    if ingrediente == "salir":
        break
    else:
        print("Se agregara su ingrediente a la pizza")
