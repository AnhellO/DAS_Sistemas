
#una relación ya no se cumple porque un Prisionero no es un Hombre Libre.

class HombreLibre(object):

    def __init__(self, position):
        self.position = position

    def walk_North(self, dist):
        self.position[1] += dist

    def walk_East(self, dist):
        self.position[0] += dist

.
class Prisoner(object):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        self.position = type(self).PRISON_LOCATION

#En el codigo pasado Prisoner hereda de persona los metodos "walk_Nort" y "Walk_East" los cuales no tiene nada que ver que 
#con la clase Persona y ahora lo cambie por hombre libre lo cual hace que sus metodos tenga coherencia.
def main():

    prisoner = Prisoner()
    print "The prisoner trying to walk to north by 10 and east by -3."
    
    try:
        prisoner.walk_North(10)
        prisoner.walk_East(-3)
    except:
        pass
    
    print "The location of the prison: {}".format(prisoner.PRISON_LOCATION)
    print "The current position of the prisoner: {}".format(prisoner.position)

if __name__ == "__main__":
    main()