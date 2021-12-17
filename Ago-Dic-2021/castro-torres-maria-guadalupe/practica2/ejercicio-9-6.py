class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        msg = f"{self.name} sirve maravillosas {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} esta abierto, pasele!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served  

        

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):
        """"Inicializar un puesto de helado."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Muestra los sabores disponibles."""
        print("\nDisponemos de los siguientes sabores:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


chepo = IceCreamStand('Chepo')
chepo.flavors = ['vanilla', 'chocolate', 'black cherry']

chepo.describe_restaurant()
chepo.show_flavors()    