class Pizza:
    def __init__(self,_inches:int,_cheese:bool,_pepperoni:bool,_salami:bool,_pimientos:bool,_cebolla:bool,_champiñones:bool):
        self.inches = _inches
        self.cheese = _cheese
        self.pepperoni = _pepperoni
        self.salami = _salami
        self.pimientos = _pimientos
        self.cebolla = _cebolla
        self.champiñones = _champiñones
        pass
    def __str__(self):
        return f"Mi pizza es de {self.inches}\" con los siguientes ingredientes: " + self.create_description()

    def create_description(self):
        description_str = ''
        words = []
        if self.cheese:
            words.append('doble queso')
        if self.pepperoni:
            words.append('pepperoni')
        if self.salami:
            words.append('salami')
        if self.pimientos:
            words.append('pimientos')
        if self.cebolla:
            words.append('cebolla')
        if self.champiñones:
            words.append('champiñones')
        
        if len(words) == 0:
            return f"salsa de tomate y queso"
        
        description_str = "salsa de tomate, queso"
        counter = len(words)
        point_of_y = counter - 1
        for_auxiliar = 0

        for i in words:
            if for_auxiliar == point_of_y:
                return f"{description_str} y "+ words[for_auxiliar]
            else:
                description_str = description_str + ", "+words[for_auxiliar]
                for_auxiliar = for_auxiliar + 1
        return description_str
            

class PizzaBuilder:
    def __init__(self,_inches:int):
        self.inches = _inches
        self.cheese = False
        self.pepperoni = False
        self.salami = False
        self.pimientos = False
        self.cebolla = False
        self.champiñones = False
               
    def addCheese(self):
        self.cheese = True
        pass
    def addPepperoni(self):
        self.pepperoni = True
        pass
    def addSalami(self):
        self.salami = True
        pass
    def addPimientos(self):
        self.pimientos = True
        pass
    def addCebolla(self):
        self.cebolla = True
        pass
    def addChampiñones(self):
        self.champiñones = True
        pass
    def build(self):
        pizzab = Pizza(self.inches,self.cheese,self.pepperoni,self.salami,self.pimientos,self.cebolla,self.champiñones)
        return pizzab


def main():
    pizzab = PizzaBuilder(20)
    pizzab.addCheese()
    pizzab.addSalami()
    pizzab.addPimientos()
    pizza1 = pizzab.build()
    pizzab2 = PizzaBuilder(18)
    pizzab3 = pizzab2.build()

    print(pizza1)
    print(pizzab3)

if __name__=="__main__":
    main()
    