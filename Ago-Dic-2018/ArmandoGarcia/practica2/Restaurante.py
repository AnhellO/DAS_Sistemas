# Ejercicio 9-1 , 9-2
class restaurante:
    def __init__(self, restauran_name, cocina_type):
        self.restauran_name = restauran_name
        self.cocina_type = cocina_type

    def __str__(self):
        return 'Restaurante: {} \nTipo: {}'.format(self.restauran_name,self.cocina_type)

    def open_restaurant(self):
         print('Restaurante: {}  "Abierto" c: \n'.format(self.restauran_name))

restaurante_1 = restaurante('Las alitas','Cortes de Carne')
restaurante_2 = restaurante('Italianis','italiana')
restaurante_3 = restaurante('McDonalds','rapida')
#Apertura de Restaurantes
restaurante_1.open_restaurant()
restaurante_2.open_restaurant()
restaurante_3.open_restaurant()

print(restaurante_1)
print('\n')
print(restaurante_2)
print('\n')
print(restaurante_3)
