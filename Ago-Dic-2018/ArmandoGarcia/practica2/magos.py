magitos = ['Dumbledore', 'Gandalf', 'Merlin', 'El mago Oscuro', 'La maga Ocuara', 'Tatsuya']
def show_magicians(lista):
    for mago in lista:
        print(mago)

def make_great(lista):
    for i in range(0, len(lista)):
        lista[i] += ' the great'

magitos2 = magitos[:]
make_great(magitos2)
show_magicians(magitos2)
show_magicians(magitos)
