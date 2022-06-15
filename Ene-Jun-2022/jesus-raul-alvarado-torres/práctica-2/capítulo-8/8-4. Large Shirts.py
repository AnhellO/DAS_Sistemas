""" Practica 8-4 - Large Shirts

Modify the make_shirt() function so that shirts are
large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default
message, and a shirt of any size with a different message."""

def make_shirt(talla='grande', texto='I love Python!'):
    print(f"Resumen: Una camiseta {talla}, con el texto: {texto}")

    #   Usuario solo hace una camisa
make_shirt()
    #   Usuario solo elije talla
make_shirt(talla='mediana')
    #   Usuario elije talla y texto
make_shirt('chica', 'I hate Python! xd')