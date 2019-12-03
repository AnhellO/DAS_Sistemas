"""7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket."""

cadena = "¿Cuántos años tienes?"
cadena += "\nIngrese 'salir' cuando haya terminado. "

while True:
    edad = input(cadena)
    if edad == 'salir':
        break
    edad = int(edad)

    if edad < 3:
        print("  Entra gratis!")
    elif edad < 13:
        print("  Tu ticket cuesta $10.")
    else:
        print("  Tu ticket cuesta $15.")