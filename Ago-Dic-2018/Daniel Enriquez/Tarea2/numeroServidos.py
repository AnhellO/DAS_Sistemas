class numeroServidos:

  def __init__(self,restaurant_name='',cuisine_type='',number_served=0):
      self.restaurant_name=restaurant_name
      self.cuisine_type=cuisine_type
      self.number_served=number_served

  def describe_restaurant(self):
      print('Restaurant_name: {}\nCousine_type: {}\nnumbers_served: {}'.format(self.restaurant_name,self.cuisine_type,self.number_served))

  def set_number_served(self):

      self.number_served = int(input("Cantidad de clientes a ingresar: "))

  def open_restaurant(self):
      print("-----> Abierto!! <-----")


rest_1 = numeroServidos('Vips','Gourmet')
rest_1.describe_restaurant()
rest_1.set_number_served()
rest_1.describe_restaurant()
