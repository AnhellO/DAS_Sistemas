""" Practica 8-12 - Sandwiches

Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the
sandwich that is being ordered. Call the function three times, using a different
number of arguments each time."""

def make_sandwich(*items):
    print("\nHaciendo sandwich:")
    for item in items:
        print(f"    Se añade {item} al sandwich.")
    print("Sandwich listo!")

make_sandwich('Pan blanco', 'jamón de cerdo', 'queso manchego', 'lechuga')
make_sandwich('Pan integral', 'pollo a la plancha', 'tomate')
make_sandwich('Pan baguette', 'jamón de pavo')