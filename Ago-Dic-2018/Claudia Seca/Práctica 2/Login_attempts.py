class User():

	def __init__(self, first_name, last_name, email, birthday, mascota_favorita, login_attempts=0):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.birthday = birthday
		self.mascota_favorita = mascota_favorita
		self.login_attempts =login_attempts

	


	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user1 = User("Nicolas", "Seca", "negrito_esponjocito@catmeow.com", "13 Septiembre ", "pajaritos")
user1.increment_login_attempts() 
user1.increment_login_attempts()
user1.increment_login_attempts() 
user1.increment_login_attempts() 
user1.increment_login_attempts()
user1.increment_login_attempts()


print("El usuario: {} intentó conectarse: {} veces:".format(user1.first_name, user1.login_attempts))

user1.reset_login_attempts()

print("El usuario: {} intentó conectarse: {} veces:".format(user1.first_name, user1.login_attempts))



