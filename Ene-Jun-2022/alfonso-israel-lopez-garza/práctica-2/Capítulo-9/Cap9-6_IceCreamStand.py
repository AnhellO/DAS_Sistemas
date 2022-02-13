class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    
    def describe_restaurant(self):
        '''Describe el restaurante.'''
        print("Nombre del restaurante: " +self.restaurant_name)
        print("Tipo de cocina: " +self.cuisine_type)

    def open_restaurant(self):
        '''Pone el restaurante como abierto'''
        print("El restaurante " +self.restaurant_name +" esta abierto.")


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        '''Agregando sabores'''
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = {'Fresa','Chocolate','mango','coco'}


    def describe_flavors(self):
        print('Sabores disponibles:')
        for sabores in self.flavors:
            print('- ' +sabores)


#Instancia de Helado
heladeria = IceCreamStand('Michoacana','Heladeria')

heladeria.describe_restaurant()
heladeria.describe_flavors()