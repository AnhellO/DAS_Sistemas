class User():

	def __init__(self, first_name, last_name, email, birthday, mascota_favorita):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.birthday = birthday
		self.mascota_favorita = mascota_favorita

	def describe_user(self):
		print("The user first name is: {} \nThe user last name is: {} \nThe user e-mail is: {} \nThe user birthday is: {} \nThe user mascota_favorita is: {}".format(self.first_name, self.last_name, self.e-mail, self.birthday, self.mascota_favorita))

	def greet_user(self):
		print("Holiii", self.first_name, "SONRIEEEE")

user1 = User("Nicolas", "Seca", "negrito_esponjocito@catmeow.com", "13 Septiembre ", "pajaritos")
user2 = User("Ale", "Seca", "alix@wiz.com", "03 Enero ", "perritos")
user3 = User("Lindsey", "Seca", "lili@lovs.com", "13 Febrero ", "gatitos")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()