class User():
	def __init__(self,keyUs,_name,_lastName,_city):
		self.keyUs=keyUs
		self._name=_name
		self._lastName=_lastName
		self._city=_city

	def describe_user(self):
		print('''
			clave del usuario {} .
			Nombre : {} .
			Apellido :{} .
			Ciudad {} .
			'''.format(self.keyUs,self._name,self._lastName,self._city))

	def greet_user(self):
		print("WELCOME AGAIN user # :" + self.keyUs)

class Admn(User):
	def __init__(self,keyUs,_name,_lastName,_city):
		super().__init__(keyUs,_name,_lastName,_city)
		self.privileges=['can add post','can delete post','can ban user']

	def show_privileges(self):
		for x in self.privileges:
			print(x)

a = Admn("123","estefan","sosa","saltillo")
a.show_privileges()		
