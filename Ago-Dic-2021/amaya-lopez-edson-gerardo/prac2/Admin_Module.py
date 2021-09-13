
class User():
    def __init__(self,first_name,last_name,age,gender,phone_number,marital_status) -> None:
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age 
        self.gender = gender 
        self.phone_number = phone_number 
        self.marital_status = marital_status 

        self.login_attempts = 0

    def describe_user(self):
        description = f'Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}'
        description+= f'\nGender: {self.gender}\nPhone Number: {self.phone_number}\nMarital Status: {self.marital_status}\n'
        return description.title()

    def greet_user(self):
        return f'Hello {self.first_name.title()} have a nice day!!'


    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


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

