class Pizza():
    def init(self,inches:int ):
        self._inches = inches
        
    def str(self):
        return f'Mi pizza es de {self._inches}" con los siguientes ingredientes: salsa de tomate, queso, {self._doblequeso}, {self._pepperoni}, {self._salami}, {self._pimientos}, {self._cebolla} y {self._champinones}'

class PizzaBuilder:
    def init(self,inches: int):
        self._inches = inches

    def str(self):
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