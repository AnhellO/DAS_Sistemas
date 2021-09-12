class Users():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_User(self):
        desc = (
            f'Name: {self.first_name} {self.last_name}\nAge: {self.age}\nCountry: {self.location}')
        return desc

    def greet_user(self):
        return(f'Nice to see you again {self.first_name} {self.last_name}')

# 9.5 Login Attempts
    def increment_login_attempts(self):
        self.login_attempts += 1
        return(f'Attempt Number: {self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        return(f'Attempts are now: {self.login_attempts}')


class Admin(Users):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = []

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'This user can: {privilege}')