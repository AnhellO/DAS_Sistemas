def show_magicians(magos):
    for magos in magos:
        print(magos)
#8.11
def make_great(magos):
    great_magos = []
   
    while magos:
        mago= magos.pop()
        great_mago = mago + ' the grate'
        great_magos.append(great_mago)

    for great_mago in great_magos:
        magos.append(great_mago)

    return magos

magos = ['Altar', 'Rodagast', 'Gandalf']
show_magicians(magos)        

print("\nGreat magos:")
great_mago = make_great(magos[:])
show_magicians(great_mago)

print("\nmagos originales:")
show_magicians(magos)