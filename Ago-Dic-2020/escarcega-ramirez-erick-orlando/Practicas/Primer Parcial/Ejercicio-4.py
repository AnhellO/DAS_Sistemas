class Pizza:
    def __init__(self, size):
        self.size = size
        self.extras = []
    
    def __str__(self):
        return f'Mi pizza es de {self.size}" con los siguientes ingrediente: salsa de tomate, queso + {self.extras}'

class PizzaBuilder():
    def __init__(self, size: int, cheese, pepperoni, cebolla, salami, pimpientos, champinones):
        self.pizza = Pizza(size)

    def addCheese(self):
        self.pizza.extras = 'doble queso'
        return self

    def addPepperoni(self):
        self.pizza.extras = 'pepperoni'
        return self

    def addSalami(self):
        self.pizza.extras = 'salami'
        return self
    
    def addCebolla(self):
        self.pizza.extras = 'cebolla'
        return self
    
    def addPimientos(self):
        self.pizza.extras = 'pimientos'
        return self

    def addChampinones(self):
        self.pizza.extras = 'champinones'
        return self

    def build(self):
        return self.pizza