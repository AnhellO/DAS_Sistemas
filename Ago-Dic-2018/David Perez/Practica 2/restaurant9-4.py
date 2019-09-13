#Ejercicio 9-4 ----------------------------------------------------------------
class restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def __str__(self):
        return 'Restaurante: {} \nTipo: {} \nClientes servidos: {}'.format(self.restaurant_name,self.cuisine_type,self.number_served)
    def open_restaurant(self):
         print('Restaurante: {}  "Abierto" \n'.format(self.restaurant_name))
    def set_number_served(self,n):
        self.number_served = n
    def increment_number_served(self,n):
        self.number_served += n

restaurant_1 = restaurant('Kyourest','Japonesa')
restaurant_2 = restaurant('KFC','Rápida')
restaurant_3 = restaurant('Little Caesars','Italiana')

restaurant_1.open_restaurant()
restaurant_2.open_restaurant()
restaurant_3.open_restaurant()

print(restaurant_1)
print('\n {}'.format(restaurant_2))
print('\n {}'.format(restaurant_3))

restaurant_3.set_number_served(4)
print('\n {}'.format(restaurant_3))
restaurant_3.increment_number_served(1)
print(restaurant_3)
