# Abstract Building
class Pizza:
  def __init__(self, inches):
    self.ingredients = ["salsa de tomate", "queso"]
    self.inches = inches
  def __str__(self):
    message = f'Mi pizza es de {self.inches}" con los siguientes ingredientes: ' + ', '.join(self.ingredients)
    # Replace the last comma with "y"
    last_comma = message.rfind(",")
    return message[:last_comma] + " y" + message[last_comma+1:]
    
# Builder.
class PizzaBuilder:
    def __init__(self, inches: int):
      self.pizza = Pizza(inches)
    def addCheese(self):
      self.pizza.ingredients.append('doble queso')
      return self
    def addPepperoni(self):
      self.pizza.ingredients.append('pepperoni')
      return self
    def addSalami(self):
      self.pizza.ingredients.append('salami')
      return self
    def addPimientos(self):
      self.pizza.ingredients.append('pimientos')
      return self
    def addCebolla(self):
      self.pizza.ingredients.append('cebolla')
      return self
    def addChampiñones(self):
      self.pizza.ingredients.append('champiñones')
      return self
    def build(self):
      return self.pizza