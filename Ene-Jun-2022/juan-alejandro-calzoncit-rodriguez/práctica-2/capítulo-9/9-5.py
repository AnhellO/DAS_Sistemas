class User(object):

    def __init__(self, first_name, last_name, age, localitation, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.loclitation = localitation
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_use(self):
        print(f"First Name : {self.first_name}.\nLast Name : {self.last_name}.\nAge : {self.age}.\nLocalitation : {self.loclitation}")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name} !!!")


u1 = User("Juan", "Calzoncit", 21, "México", 3)

for x in range(5):
    u1.increment_login_attempts()
print(u1.login_attempts)

u1.reset_login_attempts()
print(u1.login_attempts)