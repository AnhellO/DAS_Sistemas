

class user:
    
    def __init__(self, first_name, last_name, phone_number, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age
        self.email = email

    def describe_users(self):
        print("this is a sumary of the info: \n First name:" + self.first_name + "\n Last name: " + self.last_name + "\n Phone Number: " + self.phone_number + "\n age: " + self.age + "\n email" + self.email)

    def greath_user(self):
        print("greethings "+self.first_name+" :33333, you're welcome to a new world xDd")

pedro = user('pedro', 'casas', '8441234567', '22', 'pedro@potato.com')
#the calls are commented to use this class for other things. If u want to check the uses uncomment the calls
#pedro.describe_users()
#pedro.greath_user()

roberto = user('roberto', 'rodrigues', '8441234567', '25', 'roberto69@potato.com')

#roberto.describe_users()
#roberto.greath_user()

armando = user('armando', 'casas', '8441234567', '27', 'armandoCasasAveces@potato.com')

#armando.describe_users()
#armando.greath_user()


    