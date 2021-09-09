### 9.5: Login Attempts ###

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

    ### 9.5 ###
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# New instance
lupita = User('Lupita', 'Espinoza', 60, 'Mexicana')
lupita.increment_login_attempts()
lupita.increment_login_attempts()
lupita.increment_login_attempts()
lupita.increment_login_attempts()
print('The number of login attempts is: ' + str(lupita.login_attempts))

lupita.reset_login_attempts()
print('The number of login attempts is: ' + str(lupita.login_attempts))