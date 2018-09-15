def show_magicians(lista):
    for magos in lista:
        mensaje = magos.title()
        print(mensaje)

def make_great(lista):
    for i in range(0, len(lista)):
        lista[i] = "The Great " + lista[i].title()
    return lista

magos = ['Harry Potter', 'Hermione', 'Dombuldore']
nuevos_magos  = make_great(magos[:])
show_magicians(magos)
show_magicians(nuevos_magos)