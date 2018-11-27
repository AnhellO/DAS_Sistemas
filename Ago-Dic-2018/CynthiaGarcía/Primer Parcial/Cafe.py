
class Cafe:
    def getDescription(self):
        return self.__class__.__name__
    def getCosto(self):
        return self.__class__.cost

class CafeSencillo(Cafe):
    cost = 0
class Decorator(Cafe):
    def __init__(self, cofee):
        self.compuesto = cofee
    def getCosto(self):
        return self.compuesto.getCosto() + Cafe.getCosto(self)
    def getDescription(self):
        return self.compuesto.getDescription() +  ' ' + Cafe.getDescription(self)

class Vanilla(Decorator):
    cost = 32
    def __init__(self, cofee):
        Decorator.__init__(self, cofee)

class Leche(Decorator):
    cost = 28
    def __init__(self, cofee):
        Decorator.__init__(self, cofee)

class Canela(Decorator):
    cost = 30
    def __init__(self, cofee):
        Decorator.__init__(self, cofee)

class LecheyCanela(Decorator):
    cost = 33
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)


CafeVainilla=Vanilla(CafeSencillo())
print('Cafe sencillo con Vainilla a solo ' + str(CafeVainilla.getCosto()) + ' pesitos!')

CafeLeche= Leche(CafeSencillo())
print('Cafe sencillo con Leche a solo ' + str(CafeLeche.getCosto()) + ' pesitos!')

CafeCanela= Canela(CafeSencillo())
print('Cafe sencillo con Canela a solo ' + str(CafeCanela.getCosto()) +' pesitos!')

CafeLyC= LecheyCanela(CafeSencillo())
print('Cafe sencillo con Leche y Canela a solo ' + str(CafeCanela.getCosto()) + ' pesitos!')

