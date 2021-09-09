### 9.3: Users ###

# Crear clase
class User():
    def __init__(self, first_name: str, last_name: str, age: int, nacionality: str) -> None:
        ## Initialize attributes to describe a user.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nacionality = nacionality
        self.login_attempts = 0

    def describe_user(self):
        print(
            'First Name: ' + self.first_name + '\nLast Name: ' + self.last_name + 
            '\nAge: ' + str(self.age) + '\nNacionality: ' + self.nacionality
        )

    def greet_user(self):
        print('Welcome again ' + self. first_name + ' ' + self.last_name + '!')

# Instances
luis = User('Luis', 'Ibarra', 18, 'Mexicana')
marcelo = User('Marcelo', 'Correa', 10, 'Mexicana')
leo = User('Leo', 'Messi', 33, 'Argentina')

# Calling Methods
luis.describe_user()
luis.greet_user()
marcelo.describe_user()
marcelo.greet_user()
leo.describe_user()
leo.greet_user()