class User():

    def __init__(self, first_name, last_name, phone, email, twitter, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.twitter = twitter
        self.login_attempts = login_attempts

    def describe_user(self):
        print("The user first name is: {} \nThe user last name is: {} \nThe user phone is: {} \nThe user email is: {} \nThe user Twitter is: {}".format(self.first_name,self.last_name,self.phone,self.email,self.twitter))

    def greet_user(self):
        print("Hey", self.first_name, "have a nice day!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Hugo","Jacobo", 5556444, "HugeJA@gmail.com", "@Hugo_tarugo")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print("Login attempts from {}: ".format(user.first_name), user.login_attempts)

user.reset_login_attempts()
print("Login attempts from {}: ".format(user.first_name), user.login_attempts)
