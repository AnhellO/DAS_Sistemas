
class User():
    def __init__(self, first_name, last_name, id, username):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.username = username
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        return  f"ID: {self.id}\nUsername: {self.username}\nName:{self.first_name} {self.last_name}"
    
    def greet_user(self):
        return f"Hello {self.first_name}, Welcome!!!! :)"
