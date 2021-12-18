class Restaurant():

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served_number = 0

    def describe_restaurant(self):
        print("Restaurant's Name: {} - Cuisine Type: {} ".format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("The restaurant has opened!")

    def number_served(self):
        print("Curstomers served: {}".format(self.served_number))

    def set_number_served(self, number_served):
        self.served_number = number_served

    def increment_number_served(self, increment):
        self.served_number += increment

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

class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can modify post']

    def show_privileges(self):
        print("Admin's Privileges: {}".format(self.privileges))

class Admin(User):

    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.privileges = Privileges()