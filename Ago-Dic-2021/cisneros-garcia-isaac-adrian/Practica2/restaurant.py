#Practica 9.10
class Restaurant():
    
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} tiene los mejores {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} Está Abierta. ¡Adelante! \n"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served #Aquí establecemos la cantidad de clientes atendidos

    def increment_number_served(self, additional_served):
        self.number_served += additional_served #Aquí incrementamos la cantidad de clientes atendidos