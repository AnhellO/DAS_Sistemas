class PizzaBuilder():
    def __init__(self, tamanio) -> None:
        self.tamanio = tamanio

    def addCheese(self):
        self.addCheese = "doble queso"
        return self
    
    def addPepperoni(self):
        self.addPepperoni = 'pepperoni'
        return self
    
    def addSalami(self):
        self.addSalami = "salami"
        return self
    def addPimientos(self):
        self.addPimientos = "pimientos"
        return self
    
    def addCebolla(self):
        self.addCebolla = "cebolla"
        return self

    def addChampinones(self):
        self.addChampiñones = "champinones"
        return self

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
