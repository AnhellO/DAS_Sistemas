class user:

	def __init__ (self, first_name, last_name, sexo, edad):

			self.first_name = first_name
			self.last_name = last_name
			self.sexo = sexo
			self.edad = edad
			
	def describe_user(self):
		print("Nombre"+ self.first_name.title() + "Apellido" + self.last_name.title() + "Sexo" + self.sexo.title() + "Edad" + self.edad.title())


	def greet_user(self):
		print("Hola Bienvenido" + self.nombre.title())


usuario1= user(' Andrés ', ' Carranza ', ' Masculino ' , ' 23 años ')
usuario2= user(' Pablo ', ' Gutierrez ', ' Masculino ' , ' 43 años ')
usuario3= user(' Gabriela ', ' Lucio ', ' Femenino ' , ' 25 años ')
usuario4= user(' Vanessa ', ' Garibay ', ' Femenino ' , ' 19 años ')

usuario1.describe_user() and greet_user()
usuario2.describe_user() and greet_user()
usuario3.describe_user() and greet_user()
usuario4.describe_user() and greet_user()