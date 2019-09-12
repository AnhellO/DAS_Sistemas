print("Por favor, ingrese los ingredientes que quiere añadir a su pizza \nCuando ya no desee ningun elemento mas introduzca 'quit'\n")
mensaje = ""

while mensaje != "quit":
    mensaje = input("Nuevo ingrediente: ")
    mensaje = mensaje.lower()

    if mensaje != "quit":
        print("Hemos agregado el ingrediente '"+ mensaje +"' a su pizza")