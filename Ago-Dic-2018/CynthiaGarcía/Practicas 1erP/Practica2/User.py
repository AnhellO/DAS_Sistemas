class User:
	def __init__(self, first_name, last_name, age, sexo, login_attempts):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.sexo=sexo
		self.login_attempts=login_attempts

	def describe_user(self):
		info="Nombre:" + self.first_name + "\nApellido:" + self.last_name + "\nEdad:" + self.age + "\nsexo:"+ self.sexo 
		print (info)

	def great_user(self):
		saludo="Bienvenido " + self.first_name + " "+ self.last_name
		print(saludo)	

	def increment_login(self):
		ix=int((self.login_attempts)+1)
		incremento="Nombre:" + self.first_name + "\nApellido:" + self.last_name + "\nEdad:" + self.age + "\nsexo:"+ self.sexo + "\nLogin:" + str(ix)	
		print(incremento)

	def reset_login(self):
		ix=0
		reset="Nombre:" + self.first_name + "\nApellido:" + self.last_name + "\nEdad:" + self.age + "\nsexo:"+ self.sexo + "\nLogin:" + str(ix)	
		print(reset)

logIn=User('Jaime','Robles','24','Hombre', 0)
logIn.increment_login()
print("\n")
logIn.reset_login()
prit("\n")
usuario=User("Pedrito", "Ramirez", "45", "Hombre", '')
usuario.describe_user()
print("\n")

grUs=User("Pedrito", "Ramirez", "","",'')
grUs.great_user()
print("\n")

us1=User("Mirna","Salas", "45", "Mujer",'')
us1.describe_user()
print("\n")
us1.great_user()

us2=User("Chuy","García", "25", "Hombre",'')
us2.describe_user()
print("\n")
us2.great_user()

us3=User("Alberto","Fonseca", "75", "Hombre",'')
us3.describe_user()
print("\n")
us3.great_user()



