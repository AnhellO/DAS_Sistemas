class Restaurant: #clase restaurante
    def __init__(self, Name, cuisine_type): #doy atributos al restaurante
        self.Name = Name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def  describe_restaurant(self): #
        Date_restaurant = self.Name + " serves " + self.cuisine_type #metodo que imprimira la informacion
        print(Date_restaurant)

    def open_restaurant(self): #metodo que imprimira que el restaurante esta abierto
        print('"The restauran ' + self.Name + ' is it open"')

    def set_number_served(self, number_served): #permite establecer el número de clientes atendidos
        self.number_served = number_served

    def increment_number_served(self, additional_served): #permite incrementar la cantidad de clientes atendidos
        self.number_served += additional_served

Restaurant_1 = Restaurant('THE KRAKEN', 'SEAFOOD')
Restaurant_1.open_restaurant()
print("\nNumero de clientes atendidos: " + str(Restaurant_1.number_served)) #por defaul los clientes servidos on 0
Restaurant_1.number_served = 430 #agregamos una cantidad de clientes atendidos
print("Numero de cientes atendidos: " + str(Restaurant_1.number_served)) #imprimo el total de clientes servidos modificado
