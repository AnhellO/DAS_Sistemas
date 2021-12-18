from usuariosmod import Usuarios
class Admin(Usuarios):
    def __init__(self, first_name, last_name, age, job, company):
        super().__init__(first_name, last_name, age, job, company)
        self.privileges = Privileges()

    

class Privileges():
    def __init__(self,privileges=[]):
        super().__init__()
        self.privileges = privileges

    def show_privileges(self):
        print("\n Estos son tus privilegios:")
        if self.privileges:
            for i in range(len(self.privileges)):
                print(i+1, self.privileges[i])
        else:
            print("\n Este usuario no tiene ningun privilegio")