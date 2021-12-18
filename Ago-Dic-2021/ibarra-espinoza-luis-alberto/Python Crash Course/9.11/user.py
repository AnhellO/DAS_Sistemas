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

class Admin(User):

    def __init__(self, first_name: str, last_name: str, age: int, nacionality: str) -> None:
        super().__init__(first_name, last_name, age, nacionality)
        self.privileges = Privileges()

### 9.8: Privileges ###

class Privileges():

    def __init__(self) -> None:
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user']

    def show_privileges(self):
        print('This administator has the following privileges: ')
        for i in self.privileges:
            print('- ' + i)