import copy

class Person(object):

    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist

class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False

class Guardia(Person):
    PRISON_LOCATION = [1, 2]
    def __init__(self):
        super(Guardia, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.trabajando = False


def main():
    prisoner = Prisoner()
    guardia = Guardia()
    print("The prisoner trying to walk to north by 10 and east by -3.")

    try:
        prisoner.walk_north(10)
        prisoner.walk_east(-3)
        guardia.walk_east(1)
        guardia.walk_north(5)

    except:
        pass

    print("The location of the prison: {}".format(prisoner.PRISON_LOCATION))
    print("The current position of the prisoner: {}".format(prisoner.position))
    print("The location of the prison: {}".format(guardia.PRISON_LOCATION))
    print("The current position of the guardia: {}".format(guardia.position))

if __name__ == "__main__":
    main()
