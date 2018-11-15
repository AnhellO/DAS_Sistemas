class Restaurante:

  def __init__(self,restaurant_name='',cuisine_type=''):
      self.restaurant_name=restaurant_name
      self.cuisine_type=cuisine_type

  def describe_restaurant(self):
      print('Restaurant_name: {}\nCousine_type: {}'.format(self.restaurant_name,self.cuisine_type))

  def open_restaurant(self):
      print("-----> Abierto!! <-----")

 # def __str__(self):
#     return 'Nombre: {}\nOjos: {}\nColor: {}'.format(self.nombre,self.colorOjos,self.color)

rest_1 = Restaurante('Vips','Gourmet')
rest_1.describe_restaurant()
rest_1.open_restaurant()
