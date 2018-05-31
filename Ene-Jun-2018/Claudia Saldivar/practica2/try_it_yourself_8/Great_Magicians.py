def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):

    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' El mejor'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)
