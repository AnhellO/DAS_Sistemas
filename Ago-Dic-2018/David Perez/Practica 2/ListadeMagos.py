
#----Ejercicio 8-9 ------------------------------------------------------------
Lista=['Houdinni','Harry Potter','Mago Loso']
def show_magicians(magos):
    for mago in magos:
        print (mago)

show_magicians(magos)
#----Ejercicio 8-10 ------------------------------------------------------------
def make_great(magos):
    for i in range(0, len(magos)):
        magos[i] += ' The Great'

make_great(magos)
show_magicians(magos)
#-----Ejercicio 8-11 -----------------------------------------------------------
magos2= magos[:]
make_great(magos2)
show_magicians(magos2)
show_magicians(magos)
