class User:
    """9-5. Login Attempts: Add an attribute called login_attempts to your User class
    from Exercise 9-3 (page 166)."""

    def __init__(self, first_name, last_name, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User name: {self.first_name} {self.last_name}\n"
              + f"Contry: {self.country}\n"
              + f"E-mail: {self.email}")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!\n")

# Write a method called increment_ login_attempts() that increments the value
# of login_attempts by 1.
    def increment_login_attempts(self):
        self.login_attempts += 1

# Write another method called reset_login_attempts() that resets the value of
# login_attempts to 0.
    def reset_login_attempts(self):
        self.login_attempts = 0


# Make an instance of the User class and call increment_login_attempts() several
# times. Print the value of login_attempts to make sure it was incremented properly,
# and then call reset_login_attempts(). Print login_attempts again to make sure it
# was reset to 0.
user = User("Alan", "Menchaca", "México", "alanmenchaca@gmail.com")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")
