#Ejercicio 9-4
class restaurante:
    def __init__(self, restauran_name, cocina_type, number_served = 0):
        self.restauran_name = restauran_name
        self.cocina_type = cocina_type
        self.number_served = number_served

    def __str__(self):
        return 'Restaurante: {} \nTipo: {} \nClientes servidos: {}'.format(self.restauran_name,self.cocina_type,self.number_served)

    def open_restaurant(self):
         print('Restaurante: {}  "Abierto" c: \n'.format(self.restauran_name))

    def set_number_served(self,n):
        self.number_served = n

    def increment_number_served(self,n):
        self.number_served += n

restaurante_1 = restaurante('Las alitas','Cortes de Carne')
restaurante_2 = restaurante('Italianis','italiana')
restaurante_3 = restaurante('McDonalds','rapida')

restaurante_1.open_restaurant()
restaurante_2.open_restaurant()
restaurante_3.open_restaurant()

print(restaurante_1)
print('\n')
print(restaurante_2)
print('\n')
print(restaurante_3)
print('\n')

restaurante_3.set_number_served(4)
print(restaurante_3)
print('\n')
restaurante_3.increment_number_served(1)
print(restaurante_3)
