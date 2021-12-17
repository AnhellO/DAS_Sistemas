from User_multiple_module import User

class Admin(User):
    def __init__(self,first_name,last_name,age,gender,phone_number,marital_status):
        super().__init__(first_name,last_name,age,gender,phone_number,marital_status)

        self.privileges = Privileges()



class Privileges():  
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print('-----The admin -----')        
        for privilege in self.privileges:
            print("- " + privilege)
