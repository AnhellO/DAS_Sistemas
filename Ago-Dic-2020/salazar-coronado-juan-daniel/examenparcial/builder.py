from typing import Any

class PizzaBuilder:
    def __init__(self, pulgadas):
        self.pulgadas = pulgadas
        self.pizza = Pizza()

    def addCheese(self):
        self.pizza.add("doble queso")

    def addPepperoni(self):
        self.pizza.add("pepperoni")

    def addSalami(self):
        self.pizza.add("salami")

    def addPimientos(self):
        self.pizza.add("pimientos")

    def addCebolla(self):
        self.pizza.add("cebolla")

    def addChampiñones(self):
        self.pizza.add("champiñones")

    def build(self):
        #aquí no supe como hacer que la salsa de tomate y el queso siempre salgan y salgan primero
        self.pizza.add("salsa de tomate")
        self.pizza.add("queso")
        pizza = self.pizza
        return pizza

class Pizza:
    def __init__(self) -> None:
        self.ingredientes = []

    def add(self, ingrediente: Any) -> None:
        self.ingredientes.append(ingrediente)

    #No se me ocurrio como implementar lo de las pulgadas
    #No se como hacer que antes del ultimo ingrediente se imprima la y
    def list_ingredientes(self) -> None:
        print(f"Mi pizza viene con los siguientes ingredientes: {', '.join(self.ingredientes)}", end="")