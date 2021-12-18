class User():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("User's Name: {} - User's Last Name: {} - User's login attempts: {}".format(
            self.first_name, self.last_name, self.login_attempts))

    def greet_user(self):
        print('Hello {}!'.format(self.first_name))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0        
