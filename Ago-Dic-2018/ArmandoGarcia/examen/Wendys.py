from abc import ABCMeta, abstractmethod

class Burger(object):
    def __init__(self, carne='', salsa='', pan=''):
            self.carne=carne
            self.salsa=salsa
            self.pan=pan
    def __str__(self):
        return ('Burger: \nCarne: {} \ncon salsa: {} \nde pan: {}'.format(self.carne, self.slasa, self.pan)
class HotDog(object):
    def __init__(self, salchicha='', salsa='', pan=''):
            self.salchicha=salchicha
            self.salsa=salsa
            self.pan=pan
    def __str__(self):
        return ('HotDog: \nSalchicha: {} \ncon salsa: {} \nde pan: {}'.format(self.salchicha, self.slasa, self.pan)
class BuilderBurger:
    __metaclass__ = ABCMeta  #Especifique una clase abstracta para crear partes de un Producto objeto
    def set_carne(self, value):
        pass
    def set_salsa(self, value):
        pass
    def set_pan(self,value):
        pass
    def get_result(self):
        pass
class BuilderHotDog:
    __metaclass__ = ABCMeta  #Especifique una clase abstracta para crear partes de un Producto objeto
    def set_salchicha(self, value):
        pass
    def set_salsa(self, value):
        pass
    def set_pan(self,value):
        pass
    def get_result(self):
        pass
class BurgerBuilder(BuilderBurger):
    def __init__(self):
        self.burger=Burger()
    def set_carne(self, value):
        self.burger.carne=value
    def set_salsa(self, value):
        self.burger.salsa=value
    def set_pan(self, value):
        self.burger.pan=value
    def get_result(self):
        return self.burger
class HotBuilder(BuilderHotDog):
    def __init__(self):
        self.HotDog=HotDog()
    def set_Salchicha(self, value):
        self.HotDog.salchicha=value
    def set_salsa(self, value):
        self.HotDog.salsa=value
    def set_pan(self, value):
        self.HotDog.pan=value
    def get_result(self):
        return self.HotDog
class Wendys(object): #se encarga de recibir para hacer la construcción
    def construct():
        BurgerBuilder=BuilderBurger()
        BurgerBuilder.set_carne('sirlon')
        BurgerBuilder.set_salsa('bufalo')
        BurgerBuilder.set_pan('normal')
        return BurgerBuilder.get_result()
    def jochos():
        HotBuilder=BuilderHotDog()
        HotBuilder.set_salchicha('pavo')
        HotBuilder.set_salsa('captsup')
        HotBuilder.set_pan('multigrano')
        return HotBuilder.get_result()
burger=Wendys.construct()
print(burger)
