class Pizza():
    def __init__(self,inches = '',salsa = '', queso = '', doblequeso = '', pepperoni = '', salami = '', pimientos = '', cebolla = '', champinones = ''):
        self._inches = inches
        self._salsa = salsa
        self._queso = queso
        self._doblequeso = True
        self._pepperoni = pepperoni
        self._salami = salami
        self._pimientos = pimientos
        self._cebolla = cebolla
        self._champinones = champinones

    def __str__(self):
        return f'Mi pizza es de {self._inches}" con los siguientes ingredientes: salsa de tomate, queso, {self._doblequeso}, {self._pepperoni}, {self._salami}, {self._pimientos}, {self._cebolla} y {self._champinones}'

class PizzaBuilder:
    def __init__(self,inches: int):
        self._inches = inches
    
    def __str__(self):
        return f"{self._inches}"
    def addCheese(self):
        self._doblequeso = True
        return self
    
    def addPepperoni(self):
        self._pepperoni = True
        return self

    def addSalami(self):
        self._salami = True
        return self

    def addPimientos(self):
        self._pimientos = True
        return self

    def addCebolla(self):
        self._cebolla = True
        return self

    def addChampinones(self):
        self._champinones = True
        return self

    def build(self):
        return Pizza(self)

def main():
    pizza = PizzaBuilder(18).addCheese().build()
    print(pizza)

if __name__ == "__main__":
    main()