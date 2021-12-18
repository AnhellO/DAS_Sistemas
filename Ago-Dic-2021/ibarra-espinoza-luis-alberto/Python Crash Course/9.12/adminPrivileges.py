from user import  User

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