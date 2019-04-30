#Write a function that accepts a list of items a person wants
#on a sandwich. The function should have one parameter that collects as many
#items as the function call provides, and it should print a summary of the sandwich
#that is being ordered. Call the function three times, using a different number
#of arguments each time.

def make_sandwich(*ingredientes):

    print("\nIngredientes del sandwich:")
    for ingrediente in ingredientes:
        print("  ...agregando " + ingrediente + " a tu orden.")
    print("Tu sandwich esta listo!")

make_sandwich('pollo', 'queso', 'lechuga', 'salsa')
make_sandwich('pavo', 'tomate', 'aderezo')
make_sandwich('jamon', 'mayonesa')