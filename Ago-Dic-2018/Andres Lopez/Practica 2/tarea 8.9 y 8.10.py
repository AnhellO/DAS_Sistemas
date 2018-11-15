#8.9

magos=["veigar","brand","lulu","heimerdinger"]
def show_magicians(magos):
    for mago in magos:
        print (mago)

show_magicians(magos)

#8.10
def make_great(magos):
    for i in range(0, len(magos)):
        magos[i] += ' The Great'

make_great(magos)
show_magicians(magos)

#8.11
magos2= magos[:]
make_great(magos2)
show_magicians(magos2)
show_magicians(magos)
