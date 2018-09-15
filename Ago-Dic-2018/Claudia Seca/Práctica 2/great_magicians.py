def show_magicians(lista):
    for nombre in lista:
        msg = nombre.title()
        print(msg)


#Le agrega a mis magos de la lista el "the great"
def make_great(lista):
    for i in range(0, len(lista)):
        lista[i] = "The Great " + lista[i]
    

magicians = ["annie", "morgana", "diana"]
make_great(magicians)
show_magicians(magicians)