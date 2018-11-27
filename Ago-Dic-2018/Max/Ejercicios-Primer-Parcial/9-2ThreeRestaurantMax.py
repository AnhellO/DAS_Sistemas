#Start with your class from Exercise 9-1. Create three
#different instances from the class, and call
#describe_restaurant() for each instance.
class Restaurant: #clase restaurante
    def __init__(self, Name, cuisine_type): #doy atributos al restaurante
        self.Name = Name
        self.cuisine_type = cuisine_type

    def __str__(self): #añadido extra para imprimir bonito XD
        return('Restaurant name: {} \nCuisine type: {}'.format(self.Name, self.cuisine_type))

    def  describe_restaurant(self): #
        Date_restaurant = self.Name + " serves " + self.cuisine_type #metodo que imprimira la informacion
        print(Date_restaurant)

    def open_restaurant(self): #metodo que imprimira que el restaurante esta abierto
        print('"The restauran ' + self.Name + ' is it open"')

Restaurant_1 = Restaurant('The kraken', 'SeaFood') #doy descripcion de los atributos
Restaurant_1.describe_restaurant()
print("\n")
Restaurant_2 = Restaurant('Doña pelos', 'Gorditas') #doy descripcion de los atributos
Restaurant_2.describe_restaurant()
print("\n")
Restaurant_3 = Restaurant('Taquitos', 'Enchiladas') #doy descripcion de los atributos
Restaurant_3.describe_restaurant()
