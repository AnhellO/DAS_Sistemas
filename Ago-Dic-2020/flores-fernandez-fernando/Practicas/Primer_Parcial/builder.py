from abc import ABC, abstractmethod



class IBuilder(ABC):
    @abstractmethod
    def addCheese(self):
        pass
    @abstractmethod
    def addPepperoni(self):
        pass
    @abstractmethod
    def addSalami(self):
        pass
    @abstractmethod
    def addPimientos(self):
        pass
    @abstractmethod
    def addCebolla(self):
        pass
    @abstractmethod
    def addChampinones(self):
        pass
    @abstractmethod
    def build(self):
        pass

class PizzaBuilder(IBuilder):
    def __init__(self,tamano):
        self._tamano = tamano
 
    def get_tamano(self):
        return self.get_tamano

    def addCheese(self):
       
        return 'doble queso'
    
    def addPepperoni(self):
        return 'pepperoni'
   
    def addSalami(self):
         
        return 'salami'
    
    def addPimientos(self):

        return 'pimientos'
    
    def addCebolla(self):
    
        return 'cebolla'
    
    def addChampinones(self):
        return 'champinones'
    @staticmethod
    def item():
        return PizzaBuilder(18)

    def build(self):
        return      (self.get_tamano,
                     self.addCheese,
                     self.addPepperoni,
                     self.addSalami,
                     self.addPimientos,
                     self.addCebolla,
                     self.addChampinones)


class Pizza:
    def __init__(self,tamano,chesse,pepperoni,salami,pimientos,cebolla,champinones):
        self._tamano = tamano
        self._chesse = chesse
        self._pepperoni = pepperoni
        self._salami = salami
        self._pimientos = pimientos
        self._cebolla = cebolla
        self._champinones = champinones  

    def __str__(self):
        return f'Mi pizza es de {self._tamano}" con los siguientes ingredientes: salsa de tomate, queso, {self._chesse}, {self._pepperoni}, {self._salami}, {self._pimientos}, {self._cebolla} y {self._champinones}'

class PizzaDirector:
    @staticmethod
    def construct():
        return PizzaBuilder(18)\
                .addCheese()\
                .addPepperoni()\
                .addSalami()\
                .addPimientos()\
                .addCebolla()\
                .addChampinones()           