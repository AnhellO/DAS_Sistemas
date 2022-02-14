class User:
    """9-3. Users: Make a class called User. Create two attributes called first_name
    and last_name, and then create several other attributes that are typically stored 
    in a user profile. Make a method called describe_user() that prints a summary 
    of the user's information. Make another method called greet_user() that prints 
    a personalized greeting to the user."""

    def __init__(self, first_name, last_name, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.email = email

    def describe_user(self):
        print(f"User name: {self.first_name} {self.last_name}\n"
              + f"Contry: {self.country}\n"
              + f"E-mail: {self.email}")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!\n")


# Create several instances representing different users, and call both methods
# for each user.
user_one = User("Alan", "Menchaca", "México", "alanmenchaca@gmail.com")
user_one.describe_user()
user_one.greet_user()

user_two = User("Pedro", "Hernandez", "Chile", "pedrohernandez@hotmail.com")
user_two.describe_user()
user_two.greet_user()

user_three = User("Juan", "Mendoza", "Argentina", "juanmendoza@outlook.com")
user_three.describe_user()
user_three.greet_user()
