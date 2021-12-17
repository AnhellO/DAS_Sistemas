class Restaurante:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self) -> str:
        print('\n##### DATOS DEL RESTAURANTE #####\nNombre:',self.restaurant_name,'\nTipo de cocina:',self.cuisine_type,'\n')

    def open_restaurant(self) -> str:
        print("El restaurante está abierto\n")

    def set_number_served(self, number_served) -> int:
        self.number_served = number_served

    def increment_number_served(self, additional_served) -> int:
        self.number_served += additional_served

class IceCreamStand(Restaurante):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.sabores = []

    def ver_sabores(self):
        print("\nSabores de helado:")
        for sabor in self.sabores:
            print("-" + sabor.title())

print('-----------------9-1-------------------------')
restaurante = Restaurante('Las Vegas','Mexicana')
print(restaurante.restaurant_name)
print(restaurante.cuisine_type)
restaurante.describe_restaurant()
restaurante.open_restaurant()
print('\n-----------------9-2-------------------------')
restaurante_1 = Restaurante('Las Brazas','Mexicana')
restaurante_1.describe_restaurant()
restaurante_2 = Restaurante('La Canasta','Mexicana')
restaurante_2.describe_restaurant()
restaurante_3 = Restaurante('Bistro Republique','Francesa')
restaurante_3.describe_restaurant()
print('\n-----------------9-4-------------------------')
restaurante_4 = Restaurante('Las Vegas','Mexicana')
restaurante_4.describe_restaurant()
print("Clientes atendidos:", str(restaurante_4.number_served))
restaurante_4.number_served = 10
print("Clientes atendidos:", str(restaurante_4.number_served))
restaurante_4.set_number_served(20)
print("Clientes atendidos:", str(restaurante_4.number_served))
restaurante_4.increment_number_served(34)
print("Clientes atendidos:", str(restaurante_4.number_served))
print('\n-----------------9-6-------------------------')
ejemplo = IceCreamStand('Michoacana','Helados')
ejemplo.sabores = ['nuez', 'pistache', 'vainilla','chicle']
ejemplo.describe_restaurant()
ejemplo.ver_sabores()



