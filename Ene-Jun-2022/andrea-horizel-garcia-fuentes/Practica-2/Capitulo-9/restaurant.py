class Restaurante:
    
    def __init__(self, nombre, cuisine_type):
        
        self.nombre = nombre.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurante(self):
        
        mensaje = self.nombre + " sirve deliciosas " + self.cuisine_type + "."
        print("\n" + mensaje)

    def abierto_restaurante(self):
        
        mensaje = self.nombre + " Disponible ya!"
        print("\n" + mensaje)

    def set_number_served(self, number_served):
        self. number_served= number_served

    def increment_number_served(self,number_served ):
        self.number_served += number_served
