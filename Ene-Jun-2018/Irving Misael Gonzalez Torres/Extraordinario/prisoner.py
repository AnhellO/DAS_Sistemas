#la clase pricioner es logico que herede de persona pero ene ste caso no ya que la posicion del prsionero
#esta dada por PRISON_LOCATION y al estar usando las funciones de caminar al norte y al este el prisionero 
#ya no seria logico que el prisionero haga eso.
class Person(object):

    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist

#la relacion de un pricionero es una persona ya no se cumpliria al no heredar de persona ya que es 
#incongruente que este salga de la ubicacion dada en PRSION_LOCATION.
class Prisoner(object):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        self.position = type(self).PRISON_LOCATION

def main():

    prisoner = Prisoner()
    print("The prisoner trying to walk to north by 10 and east by -3.")
    
    try:
        prisoner.walk_north(10)
        prisoner.walk_east(-3)
    except:
        pass
    
    print("The location of the prison: {}".format(prisoner.PRISON_LOCATION))
    print("The current position of the prisoner: {}".format(prisoner.position))

if __name__ == "__main__":
    main()