import abc

class CafeAbstracto(metaclass=abc.ABCMeta):
    def precio(self):
        pass

    def tipo(self):
        pass

class CafeSimple(CafeAbstracto):
    def precio(self):
        return 25

    def tipo(self):
        return 'Cafecito!'

class Decorator(CafeAbstracto,metaclass=abc.ABCMeta):
    def __init__(self,cafe_dec):
        self.cafe_dec = cafe_dec

    def precio(self):
        return self.cafe_dec.precio()

    def tipo(self):
        return self.cafe_dec.tipo()

class Leche(Decorator):
    def __init__(self,cafe_dec):
        Decorator.__init__(self,cafe_dec)

    def precio(self):
        return self.cafe_dec.precio() + 3

    def tipo(self):
        return self.cafe_dec.tipo() + ' con Leche!'

class Vainilla(Decorator):
    def __init__(self,cafe_dec):
        Decorator.__init__(self,cafe_dec)

    def precio(self):
        return self.cafe_dec.precio() + 7

    def tipo(self):
        return self.cafe_dec.tipo() + ' con Vainilla!'

class Canela(Decorator):
    def __init__(self,cafe_dec):
        Decorator.__init__(self,cafe_dec)

    def precio(self):
        return self.cafe_dec.precio() + 5

    def tipo(self):
        return self.cafe_dec.tipo() + ' con Canela!'

class Crema(Decorator):
    def __init__(self,cafe_dec):
        Decorator.__init__(self,cafe_dec)

    def precio(self):
        return self.cafe_dec.precio() + 4

    def tipo(self):
        return self.cafe_dec.tipo() + ' con Crema!'

if __name__ == "__main__":
    cafecito = Vainilla(CafeSimple())
    print(cafecito.tipo() + ' A solo ' + str(cafecito.precio()) + ' pesitos!\n')

    cafecito2 = Leche(CafeSimple())
    print(cafecito2.tipo() + ' A solo ' + str(cafecito2.precio()) + ' pesitos!\n')

    cafecito3 = Canela(CafeSimple())
    print(cafecito3.tipo() + ' A solo ' + str(cafecito3.precio()) + ' pesitos!\n')

    cafecito4 = Leche(Canela(CafeSimple()))
    print(cafecito4.tipo() + ' A solo ' + str(cafecito4.precio()) + ' pesitos!\n')

    cafecito5 = Crema(CafeSimple())
    print(cafecito5.tipo() + ' A solo ' + str(cafecito5.precio()) + ' pesitos!\n')

    cafecito6 = Crema(Vainilla(CafeSimple()))
    print(cafecito6.tipo() + ' A solo ' + str(cafecito6.precio()) + ' pesitos!\n')

    cafecito7 = Vainilla(Leche(CafeSimple()))
    print(cafecito7.tipo() + ' A solo ' + str(cafecito7.precio()) + ' pesitos!\n')

    cafecito8 = Crema(Vainilla(Canela(CafeSimple())))
    print(cafecito8.tipo() + ' A solo ' + str(cafecito8.precio()) + ' pesitos!\n')



#LOGICA IMPLEMENTADA DETRAS DE MI ENFOQUE
#Lo que hacemos con el patron decorador, de la categoria estruturales, es evitarnos las herencias
#lo que hice con mi programa fue crear un cafe "base" y crear los decoradores
#que en este caso son los ingredientes, la facilidad que nos da es que podemos
#agregarle SOLO el/los que nosotros queramos, "este si, pero este otro no"
