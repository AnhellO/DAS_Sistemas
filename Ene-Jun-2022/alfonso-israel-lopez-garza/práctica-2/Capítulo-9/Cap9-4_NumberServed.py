class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbrer_served = 0

    
    def describe_restaurant(self):
        '''Describe el restaurante.'''
        print("Nombre del restaurante: " +self.restaurant_name)
        print("Tipo de cocina: " +self.cuisine_type)
        print("Numero de clientes: " +str(self.numbrer_served) +".\n")


    def open_restaurant(self):
        '''Pone el restaurante como abierto'''
        print("El restaurante " +self.restaurant_name +" esta abierto.")

    
    def set_number_served(self,number):
        '''Ingresando el numero de clientes'''
        self.numbrer_served = number
    

    def increment_number_served(self,incremento):
        '''Incrementando el numero de clientes'''
        if incremento>=0:
            self.numbrer_served +=incremento
        else:
            print("No puede disminuir los clientes con orden entrante.")

#Creando la instancia
my_restaurant = Restaurant("Chickenlittle","Casera")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#Cambiando el numero de clientes directamente a la variable
my_restaurant.numbrer_served = 3
my_restaurant.describe_restaurant()

#Cambiando el numero de clientes con el metodo (set_number_served)
my_restaurant.set_number_served(4)
my_restaurant.describe_restaurant()

#Utilizando un incremento en los clientes metodo (increment_number_served)
my_restaurant.increment_number_served(2)
my_restaurant.describe_restaurant()

##Intentando disminuir clientes con orden entrante
my_restaurant.increment_number_served(-3)
my_restaurant.describe_restaurant()