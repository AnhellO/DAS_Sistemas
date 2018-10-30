class Usuarios:

  def __init__(self,first_name='',last_name='',city='',ocupation='',login_attemps=0):
      self.first_name=first_name
      self.last_name=last_name
      self.city=city
      self.ocupation=ocupation
      self.login_attemps=login_attemps

  def increment_login_attemps(self):

      self.login_attemps=self.login_attemps+1

  def reset_login_attemps(self):
      self.login_attemps=0

  def describe_user(self):
      print('First_name: {}\nLast_name: {}\nCity: {}\nOcupation: {}\nlogin_attemps: {}'.format(self.first_name,self.last_name,self.city,self.ocupation,self.login_attemps))

  def greet_user(self):
    print('Hola {} {} que vive en {} y es {} :)'.format(self.first_name,self.last_name,self.city,self.ocupation))


usuario_1 = Usuarios('Daniel','Enriquez','Saltillo','Estudiante')
usuario_1.describe_user()
usuario_1.increment_login_attemps()
usuario_1.describe_user()
usuario_1.increment_login_attemps()
usuario_1.describe_user()
usuario_1.increment_login_attemps()
usuario_1.describe_user()
usuario_1.reset_login_attemps()
usuario_1.describe_user()
usuario_1.increment_login_attemps()
usuario_1.describe_user()
