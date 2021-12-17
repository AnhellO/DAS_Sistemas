class Usuario:
  def __init__(self, first_name,last_name,nacionalidad, edad, sexo):
      self.first_name=first_name
      self.last_name=last_name
      self.nacionalidad=nacionalidad
      self.edad=edad
      self.sexo=sexo
  def descripcio_usuario(self):
      print('nombre: '+self.first_name + ' ' + self.last_name +'\n edad: '+self.edad + ' \n sexo: ' + self.sexo +'\n nacionalidad: '+ self.nacionalidad )
  def greet_usuario(self):
      print('hola mi nombre es '+self.first_name+' mucho gusto¡¡¡')

