"""7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza."""

cadena = "\n¿Que relleno te gustaria en tu pizza?"
cadena += "\nPresione enter cuando haya terminado: "

while True:
    topping = input(cadena)
    if topping != 'quit':
        print("  Añadire " + topping + " a tu pizza.")
    else:
        break