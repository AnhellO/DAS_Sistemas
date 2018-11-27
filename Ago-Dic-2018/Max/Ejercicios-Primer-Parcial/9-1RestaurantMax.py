#Make a class called Restaurant. The __init__() method for
#Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#Make a method called describe_restaurant() that prints these two pieces of
#information, and a method called open_restaurant() that prints a message indicating
#that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes
#individually, and then call both methods

class Restaurant: #clase restaurante
    def __init__(self, Name, cuisine_type): #doy atributos al restaurante
        self.Name = Name
        self.cuisine_type = cuisine_type

    def __str__(self): #añadido extra para imprimir bonito XD
        return('Restaurant name: {} \nCuisine type: {}'.format(self.Name, self.cuisine_type))

    def  describe_restaurant(self): #metodo que imprimira la informacion
        Date_restaurant = self.Name + " serves " + self.cuisine_type
        print(Date_restaurant)

    def open_restaurant(self): #metodo que imprimira que el restaurante esta abierto
        print('"The restauran ' + self.Name + ' is it open"')

Restaurant_1 = Restaurant('THE KRAKEN', 'SEAFOOD') #doy descripcion de los atributos
print(Restaurant_1)
print("\n")
Restaurant_1.open_restaurant() #imprimo el mensaje sobre que el restaurante esta abierto
print("\n")
Restaurant_1.describe_restaurant()
print(Restaurant_1.Name) #imprimo solo el nombre del restaurante
print(Restaurant_1.cuisine_type) #imprimo solo el tipo de comida del restaurante
