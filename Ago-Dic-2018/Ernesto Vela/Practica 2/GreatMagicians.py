magos = ['Merlyn', 'Ryze', 'Gandalf']

def show_magicians(lista):
    for magos in lista:
        print(magos)

def make_great(lista):
    for i in range(0, len(lista)):
        lista[i] += ' the great <:D'


make_great(magos)
show_magicians(magos)
