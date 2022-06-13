#8.9
magos = ["merlin", "hermayoni", "Harry potter"]

def mostrar_magos(magos):
    for nombre in magos:
        print(nombre)

mostrar_magos(magos)

#8.10

def hacer_magia(magos):
    for nombre in magos:
        print("Genial " + nombre)

hacer_magia(magos)

#8.11
def intercambio_lista(magos):
    mostrar_magos(magos)
    hacer_magia(magos)

intercambio_lista(magos)
