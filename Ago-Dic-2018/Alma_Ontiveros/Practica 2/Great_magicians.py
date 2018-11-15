def show_magicians(lista):
    for magos in lista:
        mensaje = magos.title()
        print(mensaje)

def make_great(lista):
    for i in range(0, len(lista)):
        lista[i] = "The Great " + lista[i]

magos = ['Harry Potter', 'Hermione', 'Dombuldore']
make_great(magos)
show_magicians(magos)