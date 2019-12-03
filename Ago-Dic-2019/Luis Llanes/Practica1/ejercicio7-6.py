print("Por favor, ingrese los ingredientes que quiere añadir a su pizza \nSi no desea un elemento mas, introduzca 'quit'\n")
numero = int(input("Cuantos Ingredientes quiere en su pizza: "))

while numero > 0:
    mensaje = input("Nuevo ingrediente: ")
    mensaje = mensaje.lower()

    if mensaje != "quit":
        print("Hemos agregado el ingrediente '"+ mensaje +"' a su pizza")
    else:
        break
    numero -= 1