from abc import ABCMeta, abstractproperty

class person(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def accion(self):
        pass

class Programmer(person):

    def __init__(self, coding):
        self.coding = coding

    @property
    def accion(self):
        return coding

class Tester(person):

    def __init__(self, test):
        self.test = test

    @property
    def accion(self):
    
        return test

class ProjectManagement(object):

    def __init__(self, tester, programmer):
        self.tester = tester
        self.programmer = programmer


    @property
    def accion(self):
        
        return self.tester, self.programmer


def main():
    testeo = Tester("im Testing")
    programador = Programmer("Im coding")
    proyector = ProjectManagement()

    print(proyector.accion())
    print(proyector.accion())

if __name__ == '__main__':
    main()