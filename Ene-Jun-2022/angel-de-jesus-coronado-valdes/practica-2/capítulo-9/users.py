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

