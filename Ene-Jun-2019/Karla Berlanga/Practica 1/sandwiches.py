"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that is being ordered. Call the function three times, using a different num-
ber of arguments each time.
"""

def make_sandwich(*ingredientes):
    """ Imprime una lista de ingredientes que han sido ordenados """
    print("\nSandwich con los siguientes ingredientes: ")
    for ingrediente in ingredientes:
        print("- "+ingrediente)


make_sandwich('jamon')
make_sandwich('jamon', 'pepperoni')
make_sandwich('jamon', 'pepperoni', 'champiñones')
