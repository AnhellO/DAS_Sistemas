from users import User2
class Privileges2():
    def __init__(self):
        """Initialize attributes of the parent class."""
        self.privileges=["can add post", "can delete post", "can ban user"]
    
    def show_privilege(self):
        print("\n==========script del ejercicio 9-10 para 9-12 ==========")
        print("PRIVILEGES")
        for i in range(len(self.privileges)):
            print(str(i)+"° "+self.privileges[i])

class Admin2(User2):
    def __init__(self,first_name,last_name,phone,years):
        """Initialize attributes of the parent class."""
        super().__init__(first_name,last_name,phone,years)
        #Make a Privileges instance as an attribute in the Admin class
        self.privileges1 = Privileges2()

