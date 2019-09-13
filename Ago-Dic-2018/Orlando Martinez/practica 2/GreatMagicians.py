nombres_magos=['Luis', 'Pedro', 'Antonio']
def show_magicians(nombres_magos):
    for magos in nombres_magos:
        print (magos)

show_magicians(nombres_magos)

def make_great(nombres_magos):

    for i in range(len(nombres_magos)):
        nombres_magos[i] += " the great"

make_great(nombres_magos)
show_magicians(nombres_magos)
