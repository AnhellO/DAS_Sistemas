class Pizza():
    

    def __init__(self, inches):
        self.inches = inches
        self.ingredientes = ["salsa de tomate","queso"]

    def __str__(self):
        lastIngredient = self.ingredientes[-1:][0]
        self.ingredientes.remove(lastIngredient)

        return f'Mi pizza es de {self.inches}" con los siguientes ingredientes: {", ".join(self.ingredientes)} y {lastIngredient}'

class PizzaBuilder():
    
    def __init__(self, inches):
        self.pizza = Pizza(inches)

    def addCheese(self):
        self.pizza.ingredientes.append("doble queso")

    def addPepperoni(self):
        self.pizza.ingredientes.append("pepperoni")

    def addSalami(self):
        self.pizza.ingredientes.append("salami")

    def addPimientos(self):
        self.pizza.ingredientes.append("pimientos")

    def addCebolla(self):
        self.pizza.ingredientes.append("cebolla")

    def addChampiñones(self):
        self.pizza.ingredientes.append("champiñones")

    def build(self):
        return self.pizza

####

if __name__ == "__main__":

    builder = PizzaBuilder(20)
    builder.addCheese()
    builder.addPepperoni()
    builder.addSalami()
    builder.addPimientos()
    builder.addCebolla()
    builder.addChampiñones()
    pizza = builder.build()

    print(str(pizza))
