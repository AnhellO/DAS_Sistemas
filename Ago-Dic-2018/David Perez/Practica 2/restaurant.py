# Ejercicios 9-1 a 9-2
class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def __str__(self):
        return 'Restaurante: {} \nTipo: {}'.format(self.restaurant_name,self.cuisine_type)
    def open_restaurant(self):
         print('Restaurante: {}  "Abierto" \n'.format(self.restaurant_name))
restaurant_1 = restaurant('Kyourest','Japonesa')
restaurant_2 = restaurant('KFC','Rápida')
restaurant_3 = restaurant('Little Caesars','Italiana')

#Abrir restaurantes
restaurant_1.open_restaurant()
restaurant_2.open_restaurant()
restaurant_3.open_restaurant()

print(restaurant_1)
print('\n {}'.format(restaurant_2))
print('\n {}'.format(restaurant_3))
