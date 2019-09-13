class Usuarios:

  def __init__(self,first_name='',last_name='',city='',ocupation=''):
      self.first_name=first_name
      self.last_name=last_name
      self.city=city
      self.ocupation=ocupation

  def describe_user(self):
      print('First_name: {}\nLast_name: {}\nCity: {}\nOcupation: {}'.format(self.first_name,self.last_name,self.city,self.ocupation))

  def greet_user(self):
    print('Hola {} {} que vive en {} y es {} :)'.format(self.first_name,self.last_name,self.city,self.ocupation))


usuario_1 = Usuarios('Daniel','Enriquez','Saltillo','Estudiante')
usuario_1.describe_user()
usuario_1.greet_user()
