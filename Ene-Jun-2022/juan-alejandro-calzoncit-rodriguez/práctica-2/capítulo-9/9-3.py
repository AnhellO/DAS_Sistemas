class User(object):

    def __init__(self, first_name, last_name, age, localitation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.loclitation = localitation

    def describe_use(self):
        print(f"First Name : {self.first_name}.\nLast Name : {self.last_name}.\nAge : {self.age}.\nLocalitation : {self.loclitation}")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name} !!!")


u1 = User("Juan", "Calzoncit", 21, "México")
u2 = User("Roberto", "Rodríguez", 18, "España")
u3 = User("Fernando", "Puente", 25, "Colombia")

u1.describe_use()
u1.greet_user()
print()
u2.describe_use()
u2.greet_user()
print()
u3.describe_use()
u3.greet_user()