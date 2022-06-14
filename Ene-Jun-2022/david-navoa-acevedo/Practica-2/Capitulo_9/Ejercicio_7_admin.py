import imp
from Ejercicio_3_user import user

class admin(user):

    def __init__(self, first_name, last_name, phone_number, age, email, privileges):

        super().__init__(first_name, last_name, phone_number, age, email)
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges of the user are :")
        print(self.privileges)

privileges = ['add User', 'Delete User', 'delete Archives', 'Create Archives']
pedro = admin('pedro', 'casas', '8441234567', '22', 'pedro@potato.com', privileges)
#the calls are commented to use this class for other things. If u want to check the uses uncomment the calls

#pedro.show_privileges()