class User2():
    def __init__(self,first_name,last_name,phone,years):
        #"""Initialize name and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.years = years
        self.login_attempts = 0

    def describe_user(self):
        print("***** [  Data of user ]  ******")
        print("user name: "+ self.first_name.title() +" "+ self.last_name.title())
        print("phone: "+ self.phone.title())
        print("years: "+self.years.title())
        print("login: "+str(self.login_attempts)+"\n")
    
    def greet_user(self):
        print("\nHappy Birthday")
        print("Hello "+self.first_name.title() +" "+ self.last_name.title())
        print("reminder of your birthday number: "+self.years.title())
    
    def incremento_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges2():
    def __init__(self):
        """Initialize attributes of the parent class."""
        self.privileges=["can add post", "can delete post", "can ban user"]
    
    def show_privilege(self):
        print("\n==========script del ejercicio 9-10 para 9-11 ==========")
        print("PRIVILEGES")
        for i in range(len(self.privileges)):
            print(str(i)+"° "+self.privileges[i])

class Admin2(User2):
    def __init__(self,first_name,last_name,phone,years):
        """Initialize attributes of the parent class."""
        super().__init__(first_name,last_name,phone,years)
        #Make a Privileges instance as an attribute in the Admin class
        self.privileges1 = Privileges2()

