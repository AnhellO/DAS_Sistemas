import abc
#Primero creamos la clase abstracta del café.
class CafeAbstracto(metaclass=abc.ABCMeta):
    def precio(self):
        pass
    def tipo(self):
        pass
#Clase para el tipo de café que implementa la clase Abstracta
#En teoría esta es la clase concreta
class CafeSimple(CafeAbstracto):
    def precio(self):
        return 25
    def tipo(self):
        return 'Cafecito!'
#Clase Abstracta de Decorador, implementa la clase abstracta de Café,todos los
#decoradores(en este caso ingredientes) deben implementar estos metodos
class CafeAbstractoDecorator(CafeAbstracto,metaclass=abc.ABCMeta):
    def __init__(self,decorated_coffee):
        self.decorated_coffee = decorated_coffee
    def precio(self):
        return self.decorated_coffee.precio()
    def tipo(self):
        return self.decorated_coffee.tipo()
#Clases de ingredientes, implementan la clase abstracta de (CafeAbstractoDecorator)
class Vainilla(CafeAbstractoDecorator):
    def __init__(self,decorated_coffee):
        CafeAbstractoDecorator.__init__(self,decorated_coffee)
    def precio(self):
        return self.decorated_coffee.precio() + 7
    def tipo(self):
        return self.decorated_coffee.tipo() + ' con Vainilla !'
class Leche(CafeAbstractoDecorator):
    def __init__(self,decorated_coffee):
        CafeAbstractoDecorator.__init__(self,decorated_coffee)
    def precio(self):
        return self.decorated_coffee.precio() + 3
    def tipo(self):
        return self.decorated_coffee.tipo() + ' con Leche !'
class Canela(CafeAbstractoDecorator):
    def __init__(self,decorated_coffee):
        CafeAbstractoDecorator.__init__(self,decorated_coffee)
    def precio(self):
        return self.decorated_coffee.precio() + 5
    def tipo(self):
        return self.decorated_coffee.tipo() + ' con Canela !'

if __name__ == '__main__':
#Se crea un Café con Vainilla
#Agregando decoradores al objeto llamando una funcion dentro de otra funcion
#Y se llaman los métodos
    cafecito = Vainilla(CafeSimple())
    print(cafecito.tipo()+' a sólo '+str(cafecito.precio())+' pesitos !.')
#Se crea un Café con Leche
    cafecito = Leche(CafeSimple())
    print(cafecito.tipo()+' a sólo '+str(cafecito.precio())+' pesitos !.')
#Se crea un Café con Canela
    cafecito = Canela(CafeSimple())
    print(cafecito.tipo()+' a sólo '+str(cafecito.precio())+' pesitos !.')
#Se crea un Café con Canela
    cafecito = Leche(Canela(CafeSimple()))
    print(cafecito.tipo()+' a sólo '+str(cafecito.precio())+' pesitos !.')
#De esta forma, ya se pueden varios cafés con cualquiera de los ingredientes
