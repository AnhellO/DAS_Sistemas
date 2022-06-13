def show_magicians(magos):
    for magos in magos:
        print(magos)
#8.10
def make_great(magos):
    great_magos = []
   
    while magos:
        mago= magos.pop()
        great_mago = mago + 'the grate'
        great_magos.append(great_mago)

    for great_mago in great_magos:
        magos.append(great_mago)

magos = ['Altar', 'Rodagast', 'Gandalf']
show_magicians(magos)

print("\n")
make_great(magos)
show_magicians(magos)