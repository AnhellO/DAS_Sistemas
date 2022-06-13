class Restaurante:
    #9.1 Restaurante

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

class IceCreamStand(Restaurante):
    
    def __init__(self, nombre, cuisine_type='ice_cream'):
        super().__init__(nombre, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nhelados dispobibles:")
        for flavor in self.flavors:
            print("- " + flavor.title())


heladochico = IceCreamStand('Helado chico')
heladochico.flavors = ['fresa', 'nuez', 'napolitano']

heladochico.describe_restaurante()
heladochico.show_flavors()        

restaurante = Restaurante('bibs', 'hamburguesas')
print(restaurante.nombre)
print(restaurante.cuisine_type)

restaurante.describe_restaurante()
restaurante.abierto_restaurante()

# 9.2 Tres Restaurantes

mrs_hamburger= Restaurante('mrs', 'hamburguer')
mrs_hamburger.describe_restaurante()

condado_papas = Restaurante('condado papas','papas francesas')
condado_papas.describe_restaurante()

Chesse_Factory = Restaurante('Chesse Factory','Macarron con queso' )
Chesse_Factory.describe_restaurante()

# 9.4 Numero Servido
   
restaurante = Restaurante('bibs', 'hamburguesa')
restaurante.describe_restaurante()

print("\nNumber served: " + str(restaurante.number_served))
restaurante.number_served = 120
print("Number served: " + str(restaurante.number_served))

restaurante.set_number_served(1000)
print("Number served: " + str(restaurante.number_served))

restaurante.increment_number_served(540)
print("Number served: " + str(restaurante.number_served))