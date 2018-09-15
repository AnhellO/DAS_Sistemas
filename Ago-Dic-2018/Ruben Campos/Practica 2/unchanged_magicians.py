def show_magicians(lista):
    for nombre in lista:
        msg = nombre.title()
        print(msg)

def make_great(lista):
    for i in range(0, len(lista)):
        lista[i] = "The Great " + lista[i].title()
    return lista

magos = ['gandalf', 'harry', 'merlín']
nuevos_magos  = make_great(magos[:])
show_magicians(magos)
show_magicians(nuevos_magos)
