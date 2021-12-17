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

usuario_1=Usuario('Jotaro','Kuyo','japonesa','17','hombre')      
usuario_1.descripcio_usuario()
usuario_1.greet_usuario()

usuario_2=Usuario('Joseft','Jostar','ingles','16','hombre')
usuario_2.descripcio_usuario()
usuario_2.greet_usuario()

usuario_3=Usuario('Dio','Brendo','inglesa','1000','hombre')
usuario_3.descripcio_usuario()
usuario_3.greet_usuario()

usuario_4=Usuario('Josilin','kuyo','japonesa','18','mujer')
usuario_4.descripcio_usuario()
usuario_4.greet_usuario() 
