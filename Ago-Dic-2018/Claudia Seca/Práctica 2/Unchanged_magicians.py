def show_magicians(lista):
	for nombre in lista:
		msg = nombre.title()
		print(msg)

def make_great(lista):
    for i in range(0, len(lista)):
        lista[i] = "The Great " + lista[i].title()
    return lista

magicians = ["annie", "morgana", "diana"]
show_magicians(magicians)
#ya me genera una copia de la lista de mis magos
magicians2 = make_great(magicians[:])
show_magicians(magicians2)