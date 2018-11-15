def show_magicians(lista):
    for magicians in lista:
        mensaje = magicians.title()
        print(mensaje)

magos = ['Harry Potter', 'Hermione', 'Dombuldore']
show_magicians(magos)