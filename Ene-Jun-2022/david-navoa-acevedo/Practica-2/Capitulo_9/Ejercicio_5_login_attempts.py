class user:
    
    def __init__(self, first_name, last_name, phone_number, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_users(self):
        print("this is a sumary of the info: \n First name:" + self.first_name + "\n Last name: " + self.last_name + "\n Phone Number: " + self.phone_number + "\n age: " + self.age + "\n email" + self.email)

    def greath_user(self):
        print("greethings "+self.first_name+" :33333, you're welcome to a new world xDd")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_attempts(self):
        print("attempts: " + str(self.login_attempts))

armando = user('armando', 'casas', '8441234567', '27', 'armandoCasasAveces@potato.com')
armando.read_attempts()
armando.increment_login_attempts()
armando.increment_login_attempts()
armando.read_attempts()
armando.reset_login_attempts()
armando.read_attempts()

